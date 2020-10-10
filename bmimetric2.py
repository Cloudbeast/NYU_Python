import math
print("Enter price of the first item:")
data = input()
p1 = float(data)
print ("Enter price of the second item:")
data = input()
p2 = float(data)
base = p1 + p2
print("Does customer have a club card? (Y/N):")
data=input()
discount = 0.0
print("Enter tax rate, e.g. 5.5 for 5.5% tax:")
data = input()
tax = float(data)
if(data='y' or data='Y') :
    discount = base * .10

price = base - discount
print("Base price = ",base,sep="")
print("Price after discounts = ",price)