# import libraries here. Use the following ones only.
from operator import truediv
import time, sys, random

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
    option = int(input("Choose between puzzles 1-4:  "))

    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    elif option == 3:
        sudoku = sudoku3
    elif option == 4:
        sudoku = sudoku4
    else:
        raise ValueError('Invalid choice!')

    # add code here to solve the sudoku

    start_time = time.time()



    def computer_play(sudoku):
        find = find_space(sudoku)
        if not find:
            return True
        else:
            row, col, = find
        
        for i in range(1,10):
            if is_valid(sudoku, str(i), (row, col)):
                sudoku[row][col] = str(i)

                if computer_play(sudoku):
                    return True
                
                sudoku[row][col] = ' ' #resets value if incorrect
        return False   
        
    

    def is_valid(sudoku, num, pos):
        for i in range(len(sudoku[0])):  #checks row
            if sudoku[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(sudoku)): #checks column
            if sudoku[i][pos[1]] == num and pos[0] !=i:
                return False

        box_x = pos[1] // 3  #checks positions 
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y*3 + 3 ):
            for j in range(box_x*3, box_x*3 +3):
                if sudoku[i][j] == num and (i,j) != pos:
                    return False
        return True
        
    def print_board(sudoku):
        for i in range(9):
            print(sudoku[i][0:3],'|',sudoku[i][3:6],'|',sudoku[i][6:9])
            if i==5 or i==2:
                print('-'*51)      
    
    def find_space(sudoku):
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                if sudoku[i][j] == ' ':
                    return (i, j) #row, column
        return None          
            
    print_board(sudoku)

    def update_board():

        pass

    def game_state():

        pass










    def human_play():

        pass

end_time = time.time()

print(" ")

computer_play(sudoku)

print_board(sudoku)

execution_time = end_time - start_time

print("\nThis sudoku puzzle was completed in:","%.4f" % execution_time, "seconds!" )