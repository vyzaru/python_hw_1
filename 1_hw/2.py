user_num = int(input("Введите число: "))
sum_neg = 0
sum_pos = 0
for i in range(-user_num, user_num + 1, 1):
    print(i)
    if(i < 0):
        sum_neg += i
    if(i >= 0):
        sum_pos += i
print(f"Сумма отрицательных чисел равна: {sum_neg}, сумма положительных чисел равна: {sum_pos}.")