from sqliteConnect import *
import TTreadData
import time

def searchCardGoF():
    searchField = input(
        "\nWhich field would you like to search: (CardID, CardName, Courage, Cunning, Info, Magic, Temper, Wisdom)?  "
    ).title()
    searchValue = input(f"\nEnter the value for the {searchField} you want to search:  ")
    print(f"\nThe search value entered is {searchValue} ")

    #  add single quotes  
    searchValue = "'" + searchValue +"'"
    print(f"\nThe amended search value entered is {searchValue} ")

    #  search database
    cursor.execute(f"SELECT * FROM  gobletoffire WHERE {searchField} = {searchValue}")
    conn.commit()
    time.sleep(3)

    row = cursor.fetchall()

     # convert/cast(row) to a string datatype
    strRow = str(row)
    if searchValue in strRow:
        for record in row:
            print(record)
    else:
        print(f"\nThe field {searchField} does not contain a {searchValue} in the database! ")

#searchCardGoF()