a = 2
b = 1
sum = 0
for i in range(1,21):
    sum += a/b
    a,b = a+b,a
print(sum)