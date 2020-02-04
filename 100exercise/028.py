def recursion(n):
    return 10 if n == 1 else recursion(n-1)+2
print(recursion(5))