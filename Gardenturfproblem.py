#Euan McElhoney
#12/09/2014
#Assignment Exercises - Challenge Exercises

width = float(input("What is the width of the garden in metres? "))
length = float(input("Wat is the length of the garden in metres? "))

true_width = width - 2
true_length = length - 2
area = true_width*true_length
cost = area*10

print("Your garden will have an area of {0}, and will cost £{1}".format(area, cost))



