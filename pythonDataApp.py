from database import *
import glob
import os

#main function and basic menu
if __name__ == '__main__':


    while True:
        userChoice = int(input("Type 1 to add a file to the database)\nType 2 to remove a site from the database)\nType 3 to display all data from the DB)\nType 4 to exit the program)"))

        if userChoice == 1:
            fileLocation = (input("Enter the name of the file you wish to read (Example: C:/TSE datasets/CoL_LGS_21-22.tab)"))
            database.insertData(fileLocation)
            #files will be read in and added to the DB using this function

        elif userChoice == 2:
            siteID = int(input("Enter the site number for the site you wish to remove:"))
            database.removeData(siteID) 
            #entries can be selected for deletion from the DB here

        elif userChoice == 3:
            database.displayData()
            #prints everything currently in the DB
            
        elif userChoice == 4:
            print("closing down")
            break

        else:
            print("Invalid input")

        

    
#This project was the combined work of the Biodiversity Net Gain Data Integration team software engineering group at UOL
    
