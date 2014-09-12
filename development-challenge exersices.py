#Euan McElhoney
#12/09/2014
#Assignment Exercises - Development + Challenge Exercises

import math

#Challenge task 1
number1 = float(input("What is your first number? "))
number2 = float(input("What is your second number? "))

division = number1 // number2
remainder = number1 % number2

print("{1} goes into {0} {2} times with a remainder of {3}".format(number1, number2, division, remainder))

#Start of challenge exercise
width = float(input("What is the width of the garden in metres? "))
length = float(input("Wat is the length of the garden in metres? "))

true_width = width - 2
true_length = length - 2
area = true_width*true_length
cost = area*10

print("Your garden will have an area of {0}, and will cost £{1}".format(area, cost))
