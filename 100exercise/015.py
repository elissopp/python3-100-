score = int(input('please input score:'))
if score >= 90:
    level = 'A'
elif score >= 60:
    level = 'B'
else:
    level = 'C'
print(level)