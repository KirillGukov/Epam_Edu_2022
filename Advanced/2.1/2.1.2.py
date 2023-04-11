a, b = float(input()), float(input())
if a / (b**2) < 18.5:
    print('Недостаточная масса')
elif a / (b**2) > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
