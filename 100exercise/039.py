list = [1,3,5,7,9]
num = int(input('please input a number:'))
list.append(num)
p = list.index(num)
for i in range(len(list)-2,0,-1):
    if num<list[i]:
        list[p],list[i] = list[i],list[p]
        p = i
print(list)