from math import sqrt
def judge(n):
    s=int(sqrt(n))
    if n == 2 or n == 3:
        print(n)
    else:
        for i in range(2, s+1):
            if n % i == 0:
                n = n//i
                print("{}*".format(i),end='')
                judge(n)
                break
        else:
            print(n)


n = int(input('please input a number:'))
print("{} = ".format(n),end='')
if n<0:
    n = -n
    print("-1*",end='')
judge(n)
