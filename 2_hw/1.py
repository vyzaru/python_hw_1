n = input("Введите количество чисел в списке: ")
exponent = int(input("Введите степень: "))
if not n.isdigit():
    print("Некорректный ввод. Введите целое число.")
else:
    n = int(n)
    numbers = []
    for i in range(n):
        num = input("Введите число: ")
        if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
            numbers.append(int(num) ** exponent)
        else:
            numbers.append(num * exponent)
print(f'Список после преобразований: {numbers}')