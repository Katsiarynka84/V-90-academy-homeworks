a = int(input())
last = a % 10
first = a // 100
second = a // 10 - first * 10
print(first + second + last)