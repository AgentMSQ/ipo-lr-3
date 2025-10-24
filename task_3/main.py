day = int(input("Введите день: ")) #ввод дня 
month = int(input("Введите месяц: ")) #ввод месяца
if (month == 12 and day >= 1 and day <= 31) or (month == 1 and day >= 1 and day <= 30) or (month == 2 and day >= 1 and day <= 28): #условия зимы, чек месяца и дня
    print("Зима") #вывод зимы
elif (month == 3 and day >= 1 and day <= 30) or (month == 4 and day >= 1 and day <= 31) or (month == 5 and day >= 1 and day <= 30): #условия весны, чек месяца и дня
    print("Весна") #вывод весны
elif (month == 6 and day >= 1 and day <= 31) or (month == 7 and day >= 1 and day <= 30) or (month == 8 and day >= 1 and day <= 31): #условия лета, чек месяца и дня
    print("Лето") #вывод лета
elif (month == 9 and day >= 1 and day <= 30) or (month == 10 and day >= 1 and day <= 31) or (month == 11 and day >= 1 and day <= 30): #условия осени, чек месяца и дня
    print("Осень") #вывод осени
else:
    print("Введена неверная дата") #вывод неверной даты, если ошибка в введенных данных