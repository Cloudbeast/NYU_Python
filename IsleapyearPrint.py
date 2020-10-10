def isleapyear(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0:
           return True
    elif year % 100 == 0:
        return False

    elif year % 400 == 0:
        return True
    else:
        return False


 x = int(input())
if isleapyear(x):
    print ("yep")
else: print ("Nope")