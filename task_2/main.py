a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = "Два числа равны" if a == b else f"Наименьшее число: {a if a < b else b}"
print(c)