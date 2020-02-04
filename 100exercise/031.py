t = {
    'u':'tuesday',
    'h':'thursday'
}
s = {
    'a':'saturday',
    'u':'sunday'
}
weeks = {
    'm':'monday',
    't': t,
    'w':'wensday',
    'f':'friday',
    's': s
}
day = input('please input the first letter:')
if weeks[day] == t:
    day2 = input('please input the second letter:')
    print(t[day2])
elif weeks[day] == s:
    day2 = input('please input the second letter:')
    print(s[day2])
else:
    print(weeks[day])