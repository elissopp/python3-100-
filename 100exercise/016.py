from datetime import *

print(date.today())
my_day = date(1941,1,5)
print(my_day)
my_day2 = my_day+timedelta(days=3)
print(my_day2)
my_day3 = my_day.replace(year = my_day.year+5)
print(my_day3)