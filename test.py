# import libraries here. Use the following ones only.
from ast import While
from operator import truediv
import time, sys, random
from turtle import pos

# add your implementation of the required functions here

            
if __name__ == '__main__':

    # Don't change the layout of the following sudoku examples
    sudoku1 = [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ]
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]
    sudoku3 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]
    sudoku4 = [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]

    # make sure 'option=2' is used in your submission
    # add code here to solve the sudoku


    #creates a variable for storing the amount of turns taken
    turns_taken = 0

    #function for recursive computer solution
    #calls find to detect empty boxes, then fills the box with an integer between 1-9, and checks if it is a valid input
    #if not, value is reset to ' ' and the function keeps calling itself until all boxes are filled or a solution cannot be found    
    def computer_play(sudoku):
        find = find_space(sudoku)
        if not find:     #this ends the program when there are no more blanks 
            return True
        else:
            row, col, = find
        for i in range(1,10):
            if is_valid(sudoku, str(i), (row, col)):
                sudoku[row][col] = str(i)
                if computer_play(sudoku):
                    global turns_taken
                    turns_taken += 1
                    return True
                sudoku[row][col] = ' ' #resets value if incorrect 
        return False 
        
    #this function ensures that all numbers are valid 
    def is_valid(sudoku, num, pos):
        for i in range(len(sudoku[0])):  #checks row
            if sudoku[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(sudoku)): #checks column
            if sudoku[i][pos[1]] == num and pos[0] !=i:
                return False

        box_x = pos[1] // 3  #determines which 3x3 box the program is in
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y*3 + 3 ):    #checks the 3x3 box to make sure all is valid
            for j in range(box_x*3, box_x*3 +3):
                if sudoku[i][j] == num and (i,j) != pos:
                    return False
        return True
        
    #prints board with lines
    def print_board(sudoku):
        for i in range(9):
            print(sudoku[i][0:3],'|',sudoku[i][3:6],'|',sudoku[i][6:9])
            if i==5 or i==2:
                print('-'*51)      
    
    #iterates through the selected board to find elements containing ' ' 
    def find_space(sudoku):
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                if sudoku[i][j] == ' ':
                    return (i, j) #row, column
        return None          
            

    def update_board(row,col,num):
        sudoku[row-1][col-1] = num
        print_board(sudoku)

    def game_state(sudoku):
        for i in range(9):
            for j in sudoku[i]:
                if j != ' ':
                    return "The puzzle has been solved."
                else:
                    return "The puzzle could not be solved."

    def human_play():
        row = int(input("Select the row you wish to edit: "))
        col = int(input("Select which column you wish to edit: "))
        num = str(input("Select the number you wish to insert to this position: "))
        pos = [col][row]

    #The main menu, first the user selects which board they would like to solve, then selects whether they want computer play or human play (not implimented)
    #1-4 selects board while 5 exits the program
    while True:
        print("Welcome to the main menu!\n")
        option = int(input("Choose between puzzles 1-4 or press 5 to exit:\n"))
        if option == 1:
            sudoku = sudoku1
        elif option == 2:
            sudoku = sudoku2
        elif option == 3:
            sudoku = sudoku3
        elif option == 4:
            sudoku = sudoku4
        elif option == 5:
            print("\nThank you for playing!")
            break
        else:
            raise ValueError('Invalid choice!')
        #1 selects computer play, 2 selects human play(not implemented) and 3 returns to the above menu
        while True:
            game_type = int(input("Computer = 1, Human = 2, return to menu = 3:\t\n"))
            start_time = time.time() #takes the time which the program starts at
            if game_type == 1:
                print_board(sudoku)
                print(" ")
                computer_play(sudoku)
                print_board(sudoku)
                print(game_state(sudoku))
                end_time = time.time()      # takes the time computer play ends at
                execution_time = end_time - start_time
                print("\nThis sudoku puzzle was completed in:","%.4f" % execution_time, "seconds!" )     #prints execution time for the program to 4 decimal figures
                print("This sudoku puzzle was completed in:", turns_taken ,"turns!\n")
            elif game_type == 2:
                human_play()
            elif game_type == 3:
                break
            else:
                raise ValueError('invalid choice2')

            #BW

        
