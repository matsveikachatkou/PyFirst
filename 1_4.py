number = int(input("Please insert a number: "))
max_number = 0
divisor = 10
floor = True

while floor:  # if remainder < 10, floor will be equal to 0, "while" loop stops
    remainder = number % divisor
    floor = number // divisor
    number = floor
    if remainder > max_number:
        max_number = remainder

print(max_number)
