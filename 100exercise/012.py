from math import sqrt

num = 0
for i in range(100,200):
    j = int(sqrt(i))
    for k in range(2,j+1):
        if i%k == 0:
            break
    else:
        print(i)
        num += 1
print(num)