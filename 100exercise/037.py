l = []
print("please input 10 numbers:")
for i in range(1,11):
    num = int(input('{}:'.format(i)))
    l.append(num)
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
print(l)