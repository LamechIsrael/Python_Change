#######################################
# CS 1110A - Programming in Python    #
# Module 1 - Exercise 2 - Change      #
# Author: Lamech Israel               #
# Date:   01/09/2022                  #
#######################################



print('Dollar Store - Change for a purchase')

# Input

purchase_price = int(input('What is the purchase price?'))

# Processing

change = 100 - purchase_price

# Output

print('\nYour change is',  change, 'cents')

print('\nDone')