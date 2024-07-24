from sqliteConnect import *
import TTreadData
import time

def updateCardsGoF():
    TTreadData.readGoF()  #Show user list of cards for their reference
    # CardID to be updated
    idField = input("\nEnter the CardID of the card to be updated: ")
    #enter the name of the field to be updated
    fieldName = input("Which field would you like to update: (CardName, Courage, Cunning, Info, Magic, Temper, Wisdom)? ")
    #enter the value of the field to be updated
    newFieldValue = input(f"Enter the new field value for {fieldName}: ")
    print(f"The new value entered is {newFieldValue} ")

    # add single quotes around the new field value entered by the user
    newFieldValue = " '" + newFieldValue + "' "
    print(f"The new value entered is {newFieldValue} ")
    cursor.execute(f"UPDATE gobletoffire SET {fieldName} = {newFieldValue}  WHERE CardID = {idField}")
    conn.commit()
    print(f"Record {idField} updated from Goblet of Fire deck")

    time.sleep(3)
    TTreadData.readGoF() 

#updateCardsGoF()