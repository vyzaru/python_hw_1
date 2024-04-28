dictionary = {"Имя": ["Андрей", "Кирилл", "Анна", "Евгений", "Евгений", "Александр", "Татьяна", "Аркадий", "Игорь", "Кирилл"],
              "Фамилия": ["Иванов", "Лазарев", "Петрова", "Надобников", "Никитин", "Иванов", "Никитина", "Лихачев", "Никитин", "Левашев"],
              "Город проживания": ["Москва", "Омск", "Псков", "Псков", "Москва", "Псков", "Москва", "Омск", "Псков", "Москва"],
              "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
              "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
              "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
              "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия", "Работает", "Студент"]
              }

updated_dictionary = {}

for first_name, last_name, city, birth_year, birth_month, birth_day, status in zip(
        dictionary["Имя"], dictionary["Фамилия"], dictionary["Город проживания"],
        dictionary["Год рождения"], dictionary["Месяц рождения"], dictionary["Число рождения"],
        dictionary["Статус"]):

    if first_name == "Кирилл":
        first_name = "Кириллл"
    if first_name == "Александр" and last_name == "Иванов":
        status = "Работает"
    if last_name == "Лихачев":
        continue

    if last_name == "Никитин" or last_name == "Никитина" and city == "Москва":
        city = "Махачкала"

    updated_dictionary.setdefault("Фамилия Имя", []).append(first_name + " " + last_name)
    updated_dictionary.setdefault("Дата рождения", []).append(f"{birth_year}-{birth_month:02d}-{birth_day:02d}")
    updated_dictionary.setdefault("Город проживания", []).append(city)
    updated_dictionary.setdefault("Статус", []).append(status)

print(updated_dictionary)
