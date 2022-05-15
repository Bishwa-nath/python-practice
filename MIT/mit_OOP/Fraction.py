class Fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenum(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenum() * self.getNumer() + other.getNumer() * self.getDenum()
        denumNew = other.getDenum() * self.getDenum()
        return Fraction(numerNew, denumNew)

    def __sub__(self, other):
        numerNew = other.getDenum() * self.getNumer() - other.getNumer() * self.getDenum()
        denumNew = other.getDenum() * self.getDenum()
        return Fraction(numerNew, denumNew)

    def convert(self):
        return self.getNumer() / self.getDenum()


f1 = Fraction(1, 2)
f2 = Fraction(3, 5)
add = f1 + f2
sub = f1 - f2
print(f1)
print(f2)
print(add)
print(sub)
print(add.convert())
print(sub.convert())
