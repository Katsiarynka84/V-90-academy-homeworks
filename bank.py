summa = int(input())
year = int(input())
for i in range(year):
    money = summa / 100 * 10 + summa
    summa = money
print(summa)
