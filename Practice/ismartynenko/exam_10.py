class Money:
    def __init__(self, num):
        self.num = num
        self.spl = str(self.num).split('.')

        self.rub = int(self.spl[0])
        if len(self.spl[1]) == 1:
            self.kop = int(self.spl[1]) * 10
        else:
            self.kop = int(self.spl[1])

    def exchange(self):
        _ex_rate = 116.40
        return round(self.num / _ex_rate, 2)

    def __add__(self, other):
        self.sum_rub = self.rub + other.rub
        self.sum_kop = self.kop + other.kop

        if self.sum_kop >= 100:
            self.sum_rub += 1
            self.sum_kop = self.sum_kop - 100
        res = self.sum_rub + self.sum_kop / 100
        return Money(res)

    def __sub__(self, other):
        self.sub_rub = self.rub - other.rub
        self.sub_kop = self.kop - other.kop

        if self.sub_kop < 0:
            self.sub_rub -= 1
            self.sub_kop = self.sub_kop + 100
        res = self.sub_rub + self.sub_kop / 100
        return Money(res)

    def __truediv__(self, other):
        if isinstance(other, Money) and other != 0:
            res = self.num / other.num
            return res
        elif other != 0:
            res = self.num / other
            return Money(res)
        else:
            print("can't divide by zero")
            return None

    def __str__(self):
        return f"{str(round(self.num, 2)).replace('.', ',')}"

    def __lt__(self, other):
        return self.num < other.num

    def __le__(self, other):
        return self.num <= other.num

    def __gt__(self, other):
        return self.num > other.num

    def __ge__(self, other):
        return self.num >= other.num


s1 = Money(2500.05)
s2 = Money(500.02)
s3 = Money(499.50)
a = s1 + s2 + s3
s = s2 - s3
d = s1 / 500.01

print(a)
print(s)
print(d)
print(s1 < s2)
