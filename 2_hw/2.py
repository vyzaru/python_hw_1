string = input("Введите вашу строку: ")
dict = {}
for i in range(len(string)):
    if string[i].isspace():
        continue
    else:
        dict[string[i].lower()] = string.lower().count(string[i])
print(dict)
