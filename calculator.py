

a = int(input("Введите а "))
b = int(input("Введите b "))
c = input("Введите оператор ")
if c == '/':
    if b == 0:
        print('На ноль делить нельзя')
    else:
        print(a / b)
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '==':
    print(a == b)
elif c == '>=':
    print(a >= b)
elif c == '<=':
    print(a <= b)
elif c == '**':
    print(a ** b)
elif c == '!=':
    print(a != b)
elif c == '%':
    print(a % b)
elif c == '//':
    print(a //b)
else:
    print('Ошибка')

