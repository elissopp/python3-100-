def reverse(s):
    if len(s) == 1:
        print(s,end='')
    else:
        reverse(s[1:])
        print(s[0],end='')
reverse(input("please input a string:"))