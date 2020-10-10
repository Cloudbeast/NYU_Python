import math

data = input()
k = float(data)
data = input()
h = float(data)
bmi = k / (h * h)
status="Underweight"
if(bmi>30.0):
    status="Obese"
elif(bmi >= 25):
    status="Overweight"
elif(bmi>18.5 and bmi <25):
    status="Normal"
print("BMI is: ", bmi, " Status is ",status,sep="")
