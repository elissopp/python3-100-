a = input("a:")
n = int(input("n:"))
list = []
for i in range(1,n+1):
    list.append(int(a[0]*i))
sum = sum(list)
print(sum)