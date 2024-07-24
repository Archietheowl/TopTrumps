from sqliteConnect import *
import TTreadData
import time

def deleteCardsGoF():
    TTreadData.readGoF()
    #songID to be deleted
    idField = input("\nEnter the cardID of the card to be deleted: ")
    
    cursor.execute(f"DELETE FROM gobletoffire WHERE cardID = {idField}") 

    conn.commit()
    print(f"Card {idField} deleted from Goblet of Fire table")

    time.sleep(3)
    TTreadData.gobletoffire() #invoke the gobletoffire subrouting from the TTreadData python app

#deleteCardsGoF()