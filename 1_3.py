initial_number = int(input("Please insert a number: "))
number = initial_number
decimals = 0
divisor = 10
floor = True

# we divide the number by 10 to find rhe number of decimals
while floor:
    floor = number // divisor
    number = floor
    decimals += 1

# works not only for n <= 10
result = initial_number + (initial_number * 10**decimals + initial_number) + \
         (initial_number * 10**(decimals * 2) + initial_number * 10**decimals + initial_number)

print(result)
