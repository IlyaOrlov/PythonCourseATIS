word = input("Введите слово: ")

def palindrome(a):
    if a.lower() == a[::-1].lower():
        return True
    else:
        return False

print(palindrome(word))
print(type(word))