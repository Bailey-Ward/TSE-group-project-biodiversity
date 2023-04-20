from database import *

#main function and basic menu
if __name__ == '__main__':

    try:
        while True:
            userChoice = input("Type 1 to add a file to the database)\nType 2 to remove a site from the database)\nType 3 to display all data from the DB)\nType 4 to exit the program\nInput:)")
            try:
                userChoice = int(userChoice)
            except ValueError:
                print("Input should be a number between 1 and 4.")
                continue

            if userChoice == 1:
                fileLocation = (input("Enter the name of the directory you wish to read .tab files from (Example: C:/TSE_datasets):\t"))
                try:
                    database.insertData(fileLocation)
                except FileNotFoundError:
                    print("File was not found.")
                    continue
                except IOError:
                    print("Error reading file.")
                    continue
                #files will be read in and added to the DB using this function

            elif userChoice == 2:
                siteID = input("Enter the site number for the site you wish to remove:")
                database.removeData(siteID) 
                #entries can be selected for deletion from the DB here

            elif userChoice == 3:
                try:
                    database.displayData()      #prints everything currently in the DB
                except:
                    print("Error accessing the database.")

            elif userChoice == 4:
                print("Closing down")
                break

            else:
                print("Input should be a number between 1 and 4.\n")
                
    except Exception as e:
        print("An error has occurred:", e)
        
#This project was the combined work of the Biodiversity Net Gain Data Integration team software engineering group at UOL
    
