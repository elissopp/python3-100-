s = input("please input a string:")
letters = 0
space = 0
numbers = 0
others = 0
for i in range(len(s)):
    if s[i].isalpha():
        letters+=1
    elif s[i].isspace():
        space+=1
    elif s[i].isdigit():
        numbers+=1
    else:
        others+=1
print("letters:",letters)
print("space:",space)
print("numbers:",numbers)
print("others:",others)