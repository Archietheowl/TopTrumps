import TTreadData
import TTinsertData
import TTupdateData
import TTdeleteData
import TTsearch

#Create a function
def menuOptions():
    options = 0 # flag variable options = 0
    #check if the value held in the flag variable is a match with the list of items
    while options not in ["1", "2", "3", "4", "5","6"]:
        print("Songs Menu Options:\nEnter \n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Search\n6. To Exit")
    #re-assign the options variable with a different value
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5","6"]:
            print(f"{options} is not a valid choice!")
    return options

# create a boolean flag variable and set it to True
mainProgram = True

while mainProgram ==True:
    mainMenu = menuOptions() # We assigned the menuOptions() function to a variable
    # if options = 1/2/3/4/5/6 then call the respective app and it's subroutine
    if mainMenu == "1":
        TTreadData.readGoF()
    elif mainMenu == "2":
        TTinsertData.addCardsGoF()
    elif mainMenu == "3":
        TTupdateData.updateCardsGoF()
    elif mainMenu == "4":
        TTdeleteData.deleteCardsGoF()
    elif mainMenu == "5":
        TTsearch.searchCardGoF()
    else: #re-assign the value held in the mainProgram to False = exit
        mainProgram = False
input("press Enter to Exit:")
#menuOptions()
