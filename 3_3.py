def my_func(one, two, three):
    list_of_values = [one, two, three]
    for element in list_of_values:
        if type(element) != int and type(element) != float:
            return
    list_of_values.sort(reverse=True)
    return list_of_values[0] + list_of_values[1]


print(my_func("adf", 5, 6))
print(my_func(11, 5, 7))
