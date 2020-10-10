import math
dollars=0
print("Please enter the number of coins:")
print("# of quarters:")
data = input()
q = int(data)
cents = q * 25
print("# of dimes:")
data = input()
d = int(data)
cents += (d * 10)

print("# of nickels:")
data = input()
n = int(data)
cents += (n*5)
print("# of pennies:")
data = input()
p = int(data)
cents += p
dollars = cents // 100
cents = cents % 100
print("The total is ", dollars, " dollars and ",cents," cents", sep="")
