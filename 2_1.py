list_of_elements = [25, "Hello", [1, 2, "Frankfurt"],
                    (3, 78, 89), {"s", "b", 15}, {"a": 2, "b": 3},
                    True, bytearray(b"some text"), bytes(2)]

for element in list_of_elements:
    print(f'{element} is {type(element)}')
