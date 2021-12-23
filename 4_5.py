from functools import reduce

list_20 = [number for number in range(100, 1001) if number % 2 == 0]
print(reduce(lambda a, b: a+b, list_20))
