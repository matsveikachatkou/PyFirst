number_1 = input("Please provide number 1: ")
number_2 = input("Please provide number 2: ")

while True:
    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
        break
    except ValueError:
        print("Both values should be numbers!")
        number_1 = input("Please provide number 1: ")
        number_2 = input("Please provide number 2: ")


def division(num_1, num_2):
    if num_2 == 0:
        print("Can't divide by zero!")
    else:
        result = num_1 / num_2
        print(result)


division(number_1, number_2)
