import database


#main function and basic menu
if __name__ == '__main__':


    while True:
        userChoice = int(input("Type 1 to add datasets to the database)\nType 2 to remove data from the database)\nType 3 to exit the program)"))

        if userChoice == 1:
            fileLocation = (input("Enter the name of the file you wish to read (Example: C:/TSE datasets/CoL_LGS_21-22.tab)"))
            database.database.insertData(fileLocation)
            #files will be read in and added to the DB using this function

        elif userChoice == 2:
            print("Implement deleting data here") #files can be selected for deletion from the DB here

        elif userChoice == 3:
            print("Closing down")
            break

        else:
            print("Invalid input")

        

    

    
