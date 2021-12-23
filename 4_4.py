list_of_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

dict_numbers = {number: 0 for number in list_of_numbers}
for number in list_of_numbers:
    dict_numbers[number] += 1

print([number for number in dict_numbers if dict_numbers[number] == 1])
