def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return x / y
def power(x, y):
    return x ** y

while True:
    print("Выберите операцию:")
    print("1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n5 - возведение в степень\n6 - выход из программы")
    operation = input()
    if operation == '6':
        break
    elif operation not in ['1', '2', '3', '4', '5', '6']:
        raise ValueError("Wrong value")
    print("Введите два числа над которыми хотите провести операцию:")
    x = input()
    y = input()
    if not (x.isdigit() or not(x[0] == '-' and x[1:].isdigit())) or (not y.isdigit() or not(y[0 == '-' and y[1:].isdigit()])):
        raise TypeError("Wrong datatype")
    x = int(x)
    y = int(y)
    match operation:
        case '1':
            print(add(x, y))
        case '2':
            print(subtract(x, y))
        case '3':
            print(multiply(x, y))
        case '4':
            print(divide(x, y))
        case '5':
            print(power(x, y))