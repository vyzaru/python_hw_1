def multiply_list(list_to_mlp : list, multiplicator: float | int = 2) -> list:
    new_list= []
    for x in list_to_mlp:
        x *= multiplicator
        new_list.append(x)
    return new_list

print(multiply_list([1,2,3]))
print(multiply_list([1,2,3], 1.5))

multiply_list_lambda = lambda list_to_mlp, multiplicator = 2: [x * multiplicator for x in list_to_mlp]

res = multiply_list_lambda([1, 2, 3])
res2 = multiply_list_lambda([1, 2, 3], 3)

print(res)
print(res2)