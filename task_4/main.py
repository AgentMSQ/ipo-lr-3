a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
if a >= b:
    if a >= c:
        d = a
    else:
        d = c
else:
    if b >= c:
        d = b
    else:
        d = c
print(f"Наибольшее число - {d}")