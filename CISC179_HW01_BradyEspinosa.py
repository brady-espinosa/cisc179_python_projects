''' Brady Espinosa
     Date: 10/23/2024
     Homework 01
     This program takes an input from the user and validates that it is between
     7 and 10 inclusive. It then generates a pattern of Astericks based on the
     number of rows entered.
'''


rows = 0

#take input and validate in range 7 - 10
while rows < 7 or rows > 10:
    rows = int(input("Enter a number of rows between 7 and 10: "))
    if rows < 7 or rows > 10:
        print("--- Incorrect Entry Please enter a number between 7 and 10.---")

#get number of cols and find center
cols = (2 * rows) + 1
center = cols // 2

#nested loops to print astericks on the first and last index of the ranges
#address the first row case of 3 Astericks
#print middle astericks based on the number of the current row
for row in range(rows):
    star = '*'
    for col in range(cols):
        if row == 0:
            if col == 0 or col == cols - 1 or col == center:
                print(star, end='')
            else:
                print(' ', end='')
        else:
            if col == 0 or col == cols - 1 or (col - 1 == center - (row + 1)) or col + 1 == center + (row + 1):
                print(star, end='')
            else:
                print(' ', end='')
    print()
