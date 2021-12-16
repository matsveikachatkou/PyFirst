string_arr = input("Please write your text here: ")
string_list = string_arr.split(" ")
print(string_list)
for ind, element in enumerate(string_list):
    if len(element) >= 10:
        print(ind + 1, element[0:10])
    else:
        print(ind + 1, element)
