set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

common_elements = list(set1 & set2 | set1 & set3 | set2 & set3)

merged_set = set1 | set2

final_set = merged_set | set3
difference = len(final_set) - len(common_elements)

print("Множество:", final_set)
print("Элементы, которые не вошли в множества:", common_elements)
print(f"Разница между множеством и списком в {difference} элементов.")
