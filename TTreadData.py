from sqliteConnect import *
GoFDeck=[]
def readGoF():
    cursor.execute("SELECT * FROM gobletoffire")
    row = cursor.fetchall()
    for record in row:
        GoFDeck.append(record)
    return GoFDeck
#readGoF()
#print(GoFDeck)

roaldDahl1Deck=[]
def readroalddahl1():
    cursor.execute("SELECT * FROM roalddahl1")
    row = cursor.fetchall()
    for record in row:
        roaldDahl1Deck.append(record)
#readroalddhal1()
#print(roaldDahl1Deck)

sportsCarsDeck=[]
def sportscars():
    cursor.execute("SELECT * FROM sportscars")
    row = cursor.fetchall()
    for record in row:
        sportsCarsDeck.append(record)
#sportscars()
#print(sportsCarsDeck)


