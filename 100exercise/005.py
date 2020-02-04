l = []
for i in range(3):
    x = int(input('input an integer:'))
    l.append(x)
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)