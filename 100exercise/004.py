year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
num = 0
months = [0,31,28,31,30,31,30,31,31,30,31,30]
if month>2:
    if (year%400==0) or ((year%4==0) and (year%100!=0)):
        num+=1
for i in range(month):
    num+=months[i]
num+=day
print(num)

