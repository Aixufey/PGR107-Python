class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return f"{self.num} / {self.denom}"

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bot = self.denom * other.denom
        return Fraction(top, bot)

    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bot = self.denom * other.denom
        return Fraction(top, bot)

    # To get precision, overide function float
    def __float__(self):
        return self.num / self.denom

    def inverse(self):
        return Fraction(self.denom, self.num)


a = Fraction(2, 3)
b = Fraction(4, 6)

print(a)
print(b)

c = a + b
print(c)
print("%.2f " % float(c))

d = a - b
print(d)
print("%.2f " % float(d))

print(a.inverse())
