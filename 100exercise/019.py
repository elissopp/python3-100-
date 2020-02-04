from math import sqrt
for i in range(2,1001):
    list = []
    for j in range(1,int(sqrt(i))+1):
        if i%j == 0:
            list.append(j)
            list.append(i / j)
    if sum(list)-i == i:
        print(i)
