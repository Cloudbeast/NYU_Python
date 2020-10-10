print("Enter a character: ")
s = input()
result = "a digit."
if s.isalpha():
    if s.isupper():
        result= "an upper case  letter."
    else:
        result="a lower case  letter."
elif s.isdigit()== False:
    result="a non-alphanumeric  character."
print(s, " is ", result, sep="")
