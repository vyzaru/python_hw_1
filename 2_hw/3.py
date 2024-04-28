dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
value_set = set()
key_set = set()
for key, value in dct.items():
    value_set.add(value)
    key_set.add(key)
sum_set = value_set | key_set
print(sum_set)