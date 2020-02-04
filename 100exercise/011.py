def rabbits(n):
    if n<=2:
        num = 1
    else:
        num = rabbits(n-1)+rabbits(n-2)
    return num

for i in range(1,10):
    print(rabbits(i))