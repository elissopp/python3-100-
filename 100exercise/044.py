X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
for i in range(len(X)):
    for j in range(len(X[0])):
        X[i][j] += Y[i][j]
print(X)