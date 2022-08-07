time = int(input("введите количество секунд"))
days = time // 86400
hours = (time % 86400) // 3600
minutes = (time - ((days * 86400) + (hours * 3600))) // 60
seconds = time % 60

print(days, hours, minutes, seconds, sep=':')
