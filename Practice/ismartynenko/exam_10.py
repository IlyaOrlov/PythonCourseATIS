class Money:
    def __init__(self, num):
        self.num = num
        self.spl = str(self.num).split('.')

        self.rub = int(self.spl[0])
        if len(self.spl[1]) == 1:
            self.kop = float(self.spl[1] + '.0')
        elif self.spl[1].startswith('0'):
            self.kop = float(self.spl[1].replace('0', '0.'))
        else:
            self.kop = int(self.spl[1]) / 10

    def exchange(self):
        _ex_rate = 116.40
        return f"${str(round(self.num / _ex_rate, 2)).replace('.', ',')}"

    def __add__(self, other):
        self.sum_rub = self.rub + other.rub
        self.sum_kop = self.kop + other.kop

        if self.sum_kop >= 10:
            self.sum_rub += 1
            self.sum_kop = str(self.sum_kop - 10).replace('.', '')
        else:
            self.sum_kop = str(self.sum_kop).replace('.', '')
        return f"{self.sum_rub},{self.sum_kop}"

    def __sub__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __str__(self):
        return f"{self.rub},{int(self.kop * 10)}"


s1 = Money(10000.21)
s2 = Money(20000.99)

print(s1.exchange())
print(s2.exchange())

print(s1)
print(s2)
s = s1 + s2
print(s)
