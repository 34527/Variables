#Euan McElhoney
#variable improvement exercise
#



radius = int(input("Please enter the radius of the circle: "))

import math

circumference = 2* math.pi * radius
circumference2 = round(circumference,2)

area = math.pi * radius**2
area2 = round(area,2)

print("The circumference of this circle is {0}.".format(circumference2))
print("The area of this circle is {0}.".format(area2))
