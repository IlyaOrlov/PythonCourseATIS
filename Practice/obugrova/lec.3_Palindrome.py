w = input("Введите слово: ")
w = w.lower()

def palindrome(w):
    if len(w) == 1 or len(w) == 0:
        return 0
    if w[0] == w[-1]:
        return palindrome(w[1:-1])
    else:
        return 1

test = palindrome(w)
if test == 0:
    print("Это палиндром")
elif test == 1:
    print("Введённое слово не является палиндромом")