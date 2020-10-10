print("Enter an odd length string: ")
s = input()

size = len(s)
mid = size // 2

print("Middle character: ", s[mid])
print("First half: ", s[0: mid])
print("Second half: ", s[mid+1:size])

