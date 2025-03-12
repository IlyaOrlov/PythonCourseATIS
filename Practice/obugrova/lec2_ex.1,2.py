def biggest(a, b):
    if a > b:
        print(a)
    else:
        print(b)
biggest(2, 3)


def returnbiggest(a, b):
    if a > b:
        return a
    else:
        return b


c = returnbiggest(8, 7)
print(c)
