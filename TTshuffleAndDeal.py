from pip import main
from sqliteConnect import *
from TTreadData import *
import time
import random

#USER SELECT DECK
chosenDeck = None
def userSelection():
    print("TEST USERSELECTION CALLED")
    deckChoice = int(input("Select the number of the deck you would like to play with...\n1= Harry Potter and The Goblet of Fire\n2= Roald Dahl vol1\n3=Sports Cars\nDeck choice: "))
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
    print(f"You selected deck number {deckChoice}, {deckName}. Loading Deck...")
    time.sleep(2)
    return(chosenDeck)
chosenDeck = userSelection()
#TEST print(chosenDeck)


#GET SELECTED THE DECK & SHUFFLE
currentDeck = []
def selectDeck():
    print("TEST SELECT DECK CALLED")
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
#selectDeck()
#TEST print (selectDeck())



#Assign Correct Attributes for Deck
attributesGoF = ["CardID", "CardName", "Info", "Courage", "Cunning", "Magic", "Temper", "Wisdom"]
attributesRDV1 = ["CardID", "CardName", "Info", "Brains", "Cunning", "Greed", "Kindness", "Mischief"]
attributesSC = ["CardID", "CardName", "Info", "Cool Factor", "Engine Size", "Innovation", "Top Speed(mph)", "Year Launched", "Years In Production"]

def assignAttributes():
    print("TEST ASSIGNATTRIBS CALLED")
    tempAttributes = []
    if chosenDeck == 1:
        tempAttributes = attributesGoF
    elif chosenDeck == 2:
        tempAttributes = attributesRDV1
    else:
        tempAttributes = attributesSC
    time.sleep(2)
    return(tempAttributes)
currentAttributes = assignAttributes()
#TEST - print(currentAttributes)


##############Deal Half The Shuffled Deck to Player#################
p1Cards = []
cpu1Cards = []
def dealP1():
    print("TEST dealP1 CALLED")
    chunk_size = 15
    result = [selectDeck()[i:i + chunk_size] for i in range(0, len(selectDeck()), chunk_size)]
    #(f"Test result = {result[0]}")
    playerCards = (result[0])
    return(playerCards)
    #print("\n----Player's Cards ------\n")
    #for i, p1Cards in enumerate(playerCards, 14):
        #return(p1Cards)
        #print(p1Cards)
    #time.sleep(2)
dealP1()
p1Cards = dealP1()
#TEST print(f"Players cards are: {p1Cards}")

#Deal Half The Shuffled Deck to CPU
def dealCPU():
    print("TEST dealCPU CALLED")
    chunk_size = 15
    result = [selectDeck()[i:i + chunk_size] for i in range(0, len(selectDeck()), chunk_size)]
    #print(result[1])
    cpuCards = (result[1])
    return(cpuCards)
    #print("\n----Computer's Cards ------\n")
    #for i, cpu1Cards in enumerate(cpuCards, 14):
        #return(cpu1Cards)
        #print(cpu1Cards)
dealCPU()
cpu1Cards = dealCPU()
#TEST print(f"The computer's cards are:{cpu1Cards}")

#Flag variable for player's and CPU's number of cards
p1DeckCount = len(dealP1()) 
cpuDeckCount = len(dealCPU())
#TEST print(p1DeckCount)
#TESTprint(cpuDeckCount)

#Flag variable for who's turn it is
playerTurn = False
def whoStarts():
    bool(random.getrandbits(1))

playerTurn = whoStarts()
#Test print(playerTurn)

############CAN I WORK THIS OUT SO ONE FUNCTION CAN TAKE attribs and Cards as args???????
def p1CurrentCard():
    p1Card = p1Cards[0]
    return p1Card
    #print(p1Card)
p1Card=p1CurrentCard()
#print(p1Card)

def cpuCurrentCard():    
    cpuCard = cpu1Cards[0]
    return cpuCard
    #print (cpuCard)
cpuCard = cpuCurrentCard()
#print(cpuCard)


def p1DictConvert():
    p1CardDictionary = dict(zip(currentAttributes,p1CurrentCard()))
    return(p1CardDictionary)
p1CardDict = p1DictConvert()
#print(p1CardDict)

def cpuDictConvert():
    cpuCardDictionary = dict(zip(currentAttributes,cpuCurrentCard()))
    return cpuCardDictionary
cpuCardDict=cpuDictConvert()
#print(cpuCardDict)
########################################################################################

def chooseAttribute():
    if playerTurn == True:
        turn = input(f"Choose your attribute {currentAttributes[2:]}: ")
    else:
        turn = random.choice(currentAttributes[2:])
    return turn
turn = chooseAttribute()
#print(turn)

####What happens each turn when someone wins?
def playerWinsTurn():
    playerTurn = True
    p1Cards.append(cpu1Cards.pop(0))
    p1Cards.append(p1Cards.pop(0))
    return playerTurn
playerWinsTurn()

def cpuWinsTurn():
    playerTurn = False
    cpu1Cards.append(p1Cards.pop(0))
    cpu1Cards.append(cpu1Cards.pop(0))
    return playerTurn
cpuWinsTurn()

'''
def turnIsDraw()
'''
print(f"p1 cards before\n {p1Cards}")
print(f"cpu cards before\n {cpu1Cards}")
def compare():
    if p1CardDict[turn] > cpuCardDict[turn]:
        print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
        print("player wins")
        turnResult = playerWinsTurn()
    elif cpuCardDict[turn] > p1CardDict[turn]:
        print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
        print("CPU wins")
        turnResult = cpuWinsTurn()
    else:
        print(f"Player: {turn} {p1CardDict[turn]} CPU: {turn} {cpuCardDict[turn]}")
        print("It's a draw")
        #turnResult = turnIsDraw()
compare()
print(f"p1 cards after\n {p1Cards}")
print(f"cpu cards after\n {cpu1Cards}")




#main function bringing it all together for overall gameplay
def main():
    print("TEST MESSAGE MAIN FUNC CALLED")
    chosenDeck = userSelection()
    currentDeck = selectDeck()
    currentAttributes = assignAttributes()
    p1Cards = dealP1()
    cpu1Cards = dealCPU()
    while p1DeckCount > 1 and cpuDeckCount > 1:
        playerTurn = True
        p1Card=p1CurrentCard()
        cpuCard = cpuCurrentCard()
        p1CardDict = p1DictConvert()
        cpuCardDict=cpuDictConvert()
        turn = chooseAttribute()
        print(f"p1 cards before\n {p1Cards}")
        print(f"cpu cards before\n {cpu1Cards}")
        compare()
        print(f"p1 cards after\n {p1Cards}")
        print(f"cpu cards after\n {cpu1Cards}")



main()

    




'''


def gameplay():
    # play until either cpu or player has 0 cards left
    while len(p1DeckCount)>=1 and len(cpuDeckCount)>=1:
        takeTurn()



if playerTurn == True:
    turnAttribute = ("Enter your card's chosen attribute.\n1.Courage\nCunning\nMagic\nTemper\nWisdom\nSelect: ")
else:
     turnAttribute = (cpuCardDictionary.Temper)

def p1Win():
    print(f"")

def cpuWin
cardDictionary = dict(zip(p1Card,atributesGoF))
p1Attribute = input("Enter your card's chosen attribute. Select:\n1. For Courage\n2. For Cunning\n3. For Magic\n4. For Temper\n5. For Wisdom")
cpu1Attribute = p1Attribute
if p1Attribute >= cpu1Attribute:
    p1Win()
else: 
    cpuWin()


def selectAndCompare():
    
    p1Attribute = None
    
    cpuAttribute = None
    
selectAndCompare()
'''