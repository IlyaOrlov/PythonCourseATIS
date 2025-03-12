num = int(input("Введите пятизначное число: "))
for i in range(4, -1, -1):
    n = (num % 10**(i + 1)) // 10**i
    print(5 - i, "цифра равна", n)