length = []
h = 100
for i in range(1,11):
    if i == 1:
        length.append(h)
    else:
        length.append(2*h)
    h/=2
print(sum(length))
print(h)
