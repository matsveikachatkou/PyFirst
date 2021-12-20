def my_func(x, y):
    if (type(x) != int and type(x) != float) or x <= 0:
        return
    elif type(y) != int or y >= 0:
        return
    else:
        return x ** y


print(my_func(2, "ty"))
print(my_func(2, -3))
