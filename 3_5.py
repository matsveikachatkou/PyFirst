def sum_of_string():
    continue_program = True
    sum_of_list = 0
    while continue_program:
        print("Add 'Q' if you want to stop")
        string_of_numbers = input("Please provide a string of numbers: ")
        floats_list = []
        for item in string_of_numbers.split():
            if item.upper() != "Q":
                try:
                    floats_list.append(float(item))
                except ValueError:
                    print("All items must be numbers separated by space.")
                    break
            else:
                continue_program = False
        sum_of_list += sum(floats_list)
        print(f"Sum: {sum_of_list}")


sum_of_string()
