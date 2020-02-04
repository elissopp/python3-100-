profit = int(input('please input the profit:'))
money_award = 0
standard = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
for i in range(len(standard)):
    if profit>standard[i]:
        money_award+=(profit-standard[i])*rate[i]
        profit = standard[i]
print(money_award)
