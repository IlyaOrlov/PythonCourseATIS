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
        return res

    def __sub__(self, other):
        self.sub_rub = self.rub - other.rub
        self.sub_kop = self.kop - other.kop

        if self.sub_kop < 0:
            self.sub_rub -= 1
            self.sub_kop = self.sub_kop + 100
        res = self.sub_rub + self.sub_kop / 100
        return res

    def __truediv__(self, other):
        res = (self.num * 100) / (other.num * 100)
        return res

    def __str__(self):
        return f"{self.rub},{self.kop}"

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass


s1 = Money(2500.50)
s2 = Money(500.00)
s3 = Money(499.50)

print(s1.exchange())
print(s2.exchange())
print(s3.exchange())

print(f'{s1 + s3 = }')
print(f'{s2 - s3 = }')
print(f'{s1 / s2 = }')
