import csv

def mergeSort(medalTable):   
    # Breaks the list into two halves 
        if len(medalTable) > 1:
            mid = len(medalTable) // 2
            left = medalTable[:mid]
            right = medalTable[mid:]

            # Calls each half recursively for sorting
            mergeSort(left)
            mergeSort(right)

            # Iterators for the two halves
            i = 0
            j = 0

            # Iterator for the list as a whole
            k = 0

            while i < len(left) and j < len(right):
                if left[i][1:] >= right[j][1:]:
                    # The left side has moved
                    medalTable[k] = left[i] 
                    i += 1
                else:
                    # The right side has moved
                    medalTable[k] = right[j]
                    j += 1
                # The next medal list is moved to
                k += 1
            # For the rest of the lists
            while i < len(left):
                medalTable[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                medalTable[k] = right[j]
                j += 1
                k += 1


def rank_team(file_name):
    # Opens the medal.csv file in read mode
    with open('medal.csv', 'r') as file:
        #creates the csv reader
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows = []
        #below for loop iterates through the nested list and appends each element to the new list
        for row in csvreader:
            rows.append(row)
    print(header)
    print(rows, "\n")
    
    #sorts the nested list by golds, then silvers, then bronzes, and prints the result to the console 
    mergeSort(rows)
    print(header)
    print(rows)
    
    #Opens/creates the new file in write mode with '' as the delimiter
    with open('medal_table.csv', 'w', newline='') as file2:
        writer = csv.writer(file2)
        writer.writerow(header)
        writer.writerows(rows)

# Program main --- Do not change the code below but feel free to comment out 
# Calling Task 1 function

rank_team('medal.csv')
