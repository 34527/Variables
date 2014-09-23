#Euan McElhoney
#19/09/2014
#Money problem

total_money = int(input("Please enter the total amount of money held: "))

output1 = total_money//20
mod1 = total_money%20

output2 = mod1//10
mod2 = mod1%10

output3 = mod2//5
mod3 = mod2%5

output4 = mod3//2
output5 = mod3%2 

print("The way to make up this sum with the least amount of cash is {0} £20 note(s), {1} £10 note(s), {2} £5 note(s), {3} £2 coin(s), {4} £1 coin(s)".format(output1, output2, output3, output4, output5)) 
