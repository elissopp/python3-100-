a = set(['x','y','z'])
b = set(['x','y','z'])
c = set(['x','y','z'])
a -= set(['x'])
c -= set(['x','z'])
for i in a:
    for j in b:
        for k in c:
            if len(set([i,j,k])) == 3:
                print("a:{} b:{} c:{}".format(i,j,k))