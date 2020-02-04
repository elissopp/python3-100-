def recursion(n):
    return n*recursion(n-1) if n>1 else 1
print(recursion(5))