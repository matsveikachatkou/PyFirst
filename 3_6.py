def int_func():
    string_of_items = input("Please provide a string: ")
    for ind in range(len(string_of_items)):
        if ord(string_of_items[ind]) < 65 | (ord(string_of_items[ind]) > 90 & ord(string_of_items[ind]) < 97) | \
                (ord(string_of_items[ind]) > 122):
            return

    print(string_of_items[0].upper() + string_of_items[1:])


int_func()
