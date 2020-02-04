a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(input('input a number:')))
for i in range(3):
    sum += a[i][i]
print(a)
print(sum)