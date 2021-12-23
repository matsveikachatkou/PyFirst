def fact(number):
    factor = 1
    for i in range(number + 1):
        yield factor
        factor = factor * (i + 1)


for el in fact(5):
    print(el)
