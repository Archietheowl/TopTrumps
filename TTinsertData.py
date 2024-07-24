from sqliteConnect import *
import time
"""
deck = 0

while deck == 0:
    try:
        deck = int(input("Available Decks:\n1) Harry Potter and The Goblet of Fire\n2) Roald Dahl Vol 1\n3)Sports Cars\nPlease select the number of the deck you would like to play with: "))
        if deck == 1:
            deck = "gobletoffire"
            print("Finding Deck...")
            time.sleep(2)
            print("Deck Selected: 'Harry Potter and The Goblet of Fire'")
        elif deck == 2:
            deck = "roalddhal1"
            print("Finding Deck...")
            time.sleep(2)
            print("Deck Selected: 'Roald Dahl Vol 1'")
        elif deck == 3:
            deck = "sportscars"
            print("Finding Deck...")
            time.sleep(2)
            print("Deck Selected: 'Sports Cars'")
        else:
            deck = 0
            print("Please enter just the number of the deck you would like to pay with")
            time.sleep(2)
    except:
        print("Please enter only a numeric value of the deck you wish to ammend")
        time.sleep(2)
"""

#create a subroutine to add Cards to Table gobletoffire
def addCardsGoF():
    Courage = None
    Cunning = None
    Magic = None
    Temper = None
    Wisdom = None
    #create an emtpy list
    cards= []
    #capture data inputted by the user
    CardName = input("Enter Card Name: ") 
    while Courage == None:
        try:
            Courage = int(input("Enter value for Courage: "))
        except:
            print("Please enter a numeric value for Courage.")
    while Cunning == None:
        try:
            Cunning = int(input("Enter value for Cunning: "))
        except:
            print("Please enter a numeric value for Cunning.")
    Info = input("Enter value for Info: ")
    while Magic == None:
        try:
            Magic = int(input("Enter value for Magic: "))
        except:
            print("Please enter a numeric value for Magic.")
    while Temper == None:
        try:
            Temper = int(input("Enter value for Temper: "))
        except:
            print("Please enter a numeric value for Temper.")
    while Wisdom == None:
        try:
            Wisdom = int(input("Enter value for Wisdom: "))
        except:
            print("Please enter a numeric value for Wisdom.")
    
    #append captured data from the user to the card list []
    "cards.CardID is set to autoincrement and would be added automatically"
    #listName.append(variableName)
    cards.append(CardName)
    cards.append(Courage)
    cards.append(Cunning)
    cards.append(Info)
    cards.append(Magic)
    cards.append(Temper)
    cards.append(Wisdom)
    
    #insert data from the list into the gobletoffire table
    cursor.execute("INSERT INTO gobletoffire VALUES(NULL, ?,?,?,?,?,?,?)",cards)
    conn.commit() # commit/write changes to the gobletoffire table in the database
    print(f"{CardName} added to the deck: Harry Potter and The Goblet Of Fire") # display the name of the card that was added
    time.sleep(3) # delay for 3 seconds then execute the code below
    
    cursor.execute("SELECT * FROM gobletoffire") # select all Goblet of Fire records
    row = cursor.fetchall() #fetch all cards that was retrieved and pass it to the row variable
    for record in row: #iterate through the records()
        print(record)

#addCardsGoF()