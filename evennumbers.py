import math

print("Please enter a positive integer: ")
n = int(input())

for x in range(n + (n+1)):
    y = (x)
    if (y % 2 == 0) and x != 0:
        print(y)
