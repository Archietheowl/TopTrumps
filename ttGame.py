#Required libraries and modules
from multiprocessing.connection import wait
from sqliteConnect import *
from TTreadData import *
import time
import random

#Global Variables
chosenDeck = None
deckChoice = None

#Randomly decides if the Player or CPU has first turn
def whoStarts():
    playerTurn = bool(random.getrandbits(1))
    return playerTurn

###### FUNCTIONS TO SET UP THE GAME #####
#USER SELECT DECK
def userSelection(deckChoice):
    #print("TEST USERSELECTION CALLED")#####
    if deckChoice == 1:
        chosenDeck = 1
        deckName = "Harry Potter and The Goblet of Fire"
    elif deckChoice == 2:
        chosenDeck = 2
        deckName = "Roald Dahl Vol 1"
    elif deckChoice == 3:
        chosenDeck = 3
        deckName = "Sports Cars"
    else:
        print("You're selection is not valid, please enter the number of one of the decks from the menu.")
    print(f"You selected deck number {chosenDeck}, {deckName}. Loading Deck...")
    time.sleep(2)
    return chosenDeck

#GET SELECTED THE DECK & SHUFFLE
currentDeck = []
def selectDeck(chosenDeck):
    #print("TEST SELECT DECK CALLED")#####
    if chosenDeck == 1:
        readGoF()
        tempDeck = GoFDeck
    elif chosenDeck == 2:
        readroalddahl1()
        tempDeck = roaldDahl1Deck
    else: 
        sportscars()
        tempDeck = sportsCarsDeck
    random.shuffle(tempDeck)
    return(tempDeck)

#Assign Correct Attributes for Deck
attributesGoF = ["CardID", "CardName", "Info", "Courage", "Cunning", "Magic", "Temper", "Wisdom"]
attributesRDV1 = ["CardID", "CardName", "Info", "Brains", "Cunning", "Greed", "Kindness", "Mischief"]
attributesSC = ["CardID", "CardName", "Info", "Cool Factor", "Engine Size", "Innovation", "Top Speed(mph)", "Year Launched", "Years In Production"]

def assignAttributes(chosenDeck):
    #print("TEST ASSIGNATTRIBS CALLED")#####
    tempAttributes = []
    if chosenDeck == 1:
        tempAttributes = attributesGoF
    elif chosenDeck == 2:
        tempAttributes = attributesRDV1
    else:
        tempAttributes = attributesSC
    time.sleep(2)
    return(tempAttributes)

#Deal Half The Shuffled Deck to Player
p1Cards = []
def dealP1(currentDeck):
    #print("TEST dealP1 CALLED")#####
    chunk_size = 15
    result = [currentDeck[i:i + chunk_size] for i in range(0, len(currentDeck), chunk_size)]
    playerCards = (result[0])
    return playerCards
    #for i, p1Cards in enumerate(playerCards, 14):
        #return(p1Cards)
        #print(p1Cards)
    #time.sleep(2)
#p1Cards = dealP1(currentDeck)

#TEST print(f"Players cards are: {p1Cards}")

#Deal Half The Shuffled Deck to CPU

cpu1Cards = []
def dealCPU(currentDeck):
    #print("TEST dealCPU CALLED")#####
    cpuCards = []
    chunk_size = 15
    result = [currentDeck[i:i + chunk_size] for i in range(0, len(currentDeck), chunk_size)]
    cpuCards = (result[1])
    return cpuCards
    #for i, cpu1Cards in enumerate(cpuCards, 14):
        #return(cpu1Cards)
        #print(cpu1Cards)
###print(f"The computer's cards are:{cpu1Cards}")
#cpu1Cards = dealCPU(currentDeck)

#Chooses the first card in each deck as the card that is being played
x = None
def CurrentCard(x,y):
    x = y[0]
    return x
    #print(p1Card)
#print(p1Card)

#Combines the list list of attributes and list of card into a dictionary
#This is to aid user selection of attributes

def DictConvert(cA,cC):    
    cD = dict(zip(cA,cC))
    return(cD)

#If user's turn they pick the attribute
#If coputer's turn randomly picks from relevent attributes(some atts not relevent to game)
def chooseAttribute(playerTurn,currentAttributes):
    if playerTurn == True:
        turn = input(f"Choose your attribute {currentAttributes[3:]}: ")
    else:
        turn = random.choice(currentAttributes[3:])
    return turn

#What happens each turn when someone wins or if there is a draw?
#Called inside the compare() function
drawContainer = []
def playerWinsTurn(p1Cards,cpu1Cards,playerTurn):
    playerTurn = True
    if drawContainer == []:
        p1Cards.append(cpu1Cards.pop(0))
        p1Cards.append(p1Cards.pop(0))
    else:
        p1Cards.append(cpu1Cards.pop(0))
        p1Cards.append(p1Cards.pop(0))
        p1Cards.append(drawContainer.pop())
    return playerTurn


def cpuWinsTurn(p1Cards,cpu1Cards,playerTurn):
    playerTurn = False
    if drawContainer == []:
        cpu1Cards.append(p1Cards.pop(0))
        cpu1Cards.append(cpu1Cards.pop(0))
    else:
        cpu1Cards.append(p1Cards.pop(0))
        cpu1Cards.append(cpu1Cards.pop(0))#####GOT TO SORT THIS AS ISN@T WORKING DON@T THINK I CAN DO PLAYER TURN AND DRAW CONTAINER TOGETHER
        cpu1Cards.append(drawContainer.pop())
    return playerTurn

def turnIsDraw(p1Cards,cpu1Cards,playerTurn):
    drawContainer.append(p1Cards.pop(0))
    drawContainer.append(cpu1Cards.pop(0))
    return playerTurn

#Compares the chosen attribute from the cpu and p1 one card in play
#Selects which function to run based on outcome
'''
def compare(p1CardDict,cpuCardDict,turn):
    if p1CardDict[turn] > cpuCardDict[turn]:
        print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
        print("player wins")
        return playerWinsTurn(p1Cards,cpu1Cards)
    elif cpuCardDict[turn] > p1CardDict[turn]:
        print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
        print("CPU wins")
        return cpuWinsTurn(p1Cards,cpu1Cards)
    else:
        print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
        print("It's a draw")
        return turnIsDraw(p1Cards,cpu1Cards)
'''
def playAgain():
    print("This game has finished.")
    newGame = str(input("Play again? y / n: ")).lower
    if newGame == "y":
        print("Great! Here we go again. Loading new game...")
        time.sleep(2)
        return
        main()
    else:
        print("Thanks for playing. Goodbye!")
        time.sleep(2)
        exit()




def declareWinner(p1DeckCount,cpuDeckCount): #This could be used for completed game but also called on button click to quit game at any point and see who had more cards and is the
    if p1DeckCount > cpuDeckCount:
        print("Player Wins! That's one for humanity! Well done")
        playAgain()
    elif cpuDeckCount > p1DeckCount:
        print("Computer wins! Today we lose a game of Top Trumps. Tomorrow skynet becomes self aware!")
        playAgain()
    else:
        print("It's a draw. Stalemate!")
        playAgain()



def main():  
    #Flag variable for who's turn it is
    playerTurn = whoStarts()
    print(playerTurn)
    time.sleep(2)
    #Player chooses which deck to play with
    deckChoice = int(input("Select the number of the deck you would like to play with...\n1 = Harry Potter and The Goblet of Fire\n2 = Roald Dahl vol1\n3 = Sports Cars\nDeck choice: "))
    chosenDeck = userSelection(deckChoice)
    #print(f"Chosen deck = {chosenDeck}")######
    currentDeck = selectDeck(chosenDeck)
    #print(currentDeck)######
    currentAttributes = assignAttributes(chosenDeck)
    #print(currentAttributes)#####
    #print("\n PLAYER'S CARDS\n")######
    p1Cards = dealP1(currentDeck)
    #print(p1Cards)#####
    time.sleep(2)
    #print("\n COMPUTER'S CARDS\n")#####
    cpu1Cards = dealCPU(currentDeck)
    #print(cpu1Cards)#####
    #print(playerTurn)#####
    
    gameOn = True
    
    while gameOn == True:
        time.sleep(1)
        #Flag variable for player's and CPU's number of cards
        p1DeckCount = len(p1Cards) 
        cpuDeckCount = len(cpu1Cards)

        if p1DeckCount < 1 or cpuDeckCount < 1:
            gameOn = False
            declareWinner(p1DeckCount,cpuDeckCount)
        else:
            gameOn = True 
        p1Card = CurrentCard(x,p1Cards)
        #print(f"Your Card is: {p1Card}")#####
        cpu1Card = CurrentCard(x,cpu1Cards)
        #print(f"This is player one's card {cpu1Card}")#####
        p1CardDict = DictConvert(currentAttributes,p1Card)
        print("Your card for this turn is:\n")
        for key, value in p1CardDict.items():
            print(key, ':', value)
        print(" ")
        cpuCardDict = DictConvert(currentAttributes,cpu1Card)
        
        #print(cpuCardDict)#####
        turn = chooseAttribute(playerTurn,currentAttributes)
        #print(turn)#####


        '''
        deckCountDict = {'Player 1 cards remaining = ' : p1DeckCount, 'Computer cards remaining =  ': cpuDeckCount }
        for key, value in deckCountDict.items():
            print(key, ':', value)
        '''
        print(" ")
        print(f"Player cards remaining {p1DeckCount} : {cpuDeckCount} Computer cards remaining")

        ###############################################################################
        #print(f"p1 cards before\n {p1Cards}")#####
        #print(f"cpu cards before\n {cpu1Cards}")#####
        
        #NESTED FUNCTION
        #Compares the chosen attribute from the cpu and p1 one card in play
        #Selects which function to run based on outcome
        def compare(p1CardDict,cpuCardDict,turn,playerTurn):
            if p1CardDict[turn] > cpuCardDict[turn]:
                print(" ")
                print("This Turn...")
                print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
                time.sleep(1)
                print(" ")
                print("player wins")
                playerTurn = playerWinsTurn(p1Cards,cpu1Cards,playerTurn)
                return playerTurn
            elif p1CardDict[turn] < cpuCardDict[turn]:
                print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
                print("CPU wins")
                playerTurn = cpuWinsTurn(p1Cards,cpu1Cards,playerTurn)
                return playerTurn
            else:
                print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
                print("It's a draw")
                playerTurn =  turnIsDraw(p1Cards,cpu1Cards,playerTurn)
                return playerTurn
        playerTurn = compare(p1CardDict,cpuCardDict,turn,playerTurn)
        
        #print(f"p1 cards after\n {p1Cards}")#####
        #print(f"cpu cards after\n {cpu1Cards}")#####
        ################################################################################
main()

######Things to fix
"""
-Ending of the game
-Deck count registerined to end game
-Funct to manually end game
-Check error message: Having issues with cpu or player turn??????
"""