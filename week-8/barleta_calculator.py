"""
============================================
; Title:  Exercise 8.3 - Python in action
; Author: Professor Krasso
; Date: 06 December 2020
; Modified By: Marie Nicole Barleta
; Description:  Python in action (calculator)
;===========================================

"""

# function that adds two numbers

def add(number01, number02):

    sum = number01 + number02
    return (sum)

#functions that subtracts two numbers

def subtract(number01, number02):

    difference = number01 - number02
    return (difference)


#function that divides two numbers
def divide(number01, number02):

    quotient = number01 / number02
    return (quotient)



"""
this is a variable input that prompts the user to choose from add, sub or div to print the user's desired result.

"""

value = input("Enter the following to calculate: ---- add for addition -----  sub for subtraction ---- div for division ----- ")

"""
"""


#this is the print value once the user enter the word " add " , it shows the sum value of two numbers.
if value == "add":
    print(("The sum of two numbers is: ") + str(add(1,2)))

#this is the print value once the user enter the word " sub " , it shows the difference value of two numbers
elif value == "sub":
    print(("The difference of two numbers is: ") + str(subtract(4, 1)))

#this is the print value once the user enter the word " sub " , it shows the quotient value of two numbers
elif value == "div":
    print(("The quotient of two numbers is: ") + str(divide(8, 2)))

#this will show the user that their input is invalid if the input is not among the three valid input
else:
    print("Invalid input try again")



#P.S. for some reason in the very first run of the code it will prompt you invalid input but after the first run and trying it again the program will work fine