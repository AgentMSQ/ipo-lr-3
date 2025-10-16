day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
if (month == 12 and day >= 1 and day <= 31) or (month == 1 and day >= 1 and day <= 30) or (month == 2 and day >= 1 and day <= 28):
    print("Зима")
elif (month == 3 and day >= 1 and day <= 30) or (month == 4 and day >= 1 and day <= 31) or (month == 5 and day >= 1 and day <= 30):
    print("Весна")
elif (month == 6 and day >= 1 and day <= 31) or (month == 7 and day >= 1 and day <= 30) or (month == 8 and day >= 1 and day <= 31):
    print("Лето")
elif (month == 9 and day >= 1 and day <= 30) or (month == 10 and day >= 1 and day <= 31) or (month == 11 and day >= 1 and day <= 30):
    print("Осень")
else:
    print("Введена неверная дата")