entered_characters = str()
while 1:
    x = input("Введите число: ")
    if x.isdigit():
        entered_characters += x
    elif x.lower() == "stop":
        print(x)
        break
    else:
        print(f"Введен не числовой символ: {x}")

print(entered_characters)

