"""
============================================
; Title:  Exercise 8.3
; Author: Professor Krasso
; Date: 06 December 2020
; Modified By: Marie Nicole Barleta
; Description:  Python in action exercise
;===========================================

"""

first_name = 'Marie Nicole'
last_name = 'Barleta'

print(first_name + ' ' + last_name)

even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,5,7,9]

number01 = 4
number02 = 7

if number01 in even_numbers:
    print(str(number01) + " is an even number")

else: 
    print(str(number01) + " is an odd number")

if number02 in odd_numbers:
    print(str(number02) + " is an odd number")

else:
    print(str(number02) + " is an even number")


def hello_world():
    return "Hello World"
print(hello_world())

def my_world(name):
    return "You are now in {} world".format(name)
print(my_world("Barleta's"))