user_input = input("Введите трехзначное число: ")
if not user_input.isdigit() or len(user_input) != 3:
    input("Введено не трехзначное число.")
else:
    number = int(user_input)
    digits = [int(digit) for digit in str(number)]

    if len(set(digits)) != 3:
        print("Число должно состоять из трех различных цифр!")
    else:
        permutations = set()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k and i != k:
                        permutation = str(digits[i]) + str(digits[j]) + str(digits[k])
                        permutations.add(permutation)

        print("Перестановки:", ", ".join(permutations))