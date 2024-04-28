while True:
    num = input("Введите число: ")
    if num == "exit":
        print("Работа программы завершена.")
        break
    elif not num.isdigit():
        print("Введенный тип данных не является числом!")
        continue
    else:
        print("Длина введенного числа: ", len(num), ".", sep="")