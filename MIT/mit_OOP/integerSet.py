<<<<<<< HEAD
class IntSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def delete(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' does not exist!')

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        return '{' + result[:-1] + '}'


s = IntSet()
print(s)
s.insert(4)
s.insert(3)
s.insert(5)
s.insert(3)
print(s)
print(s.member(7))
print(s.member(4))
s.delete(5)
s.delete(9)
print(s)
=======
class IntSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def delete(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' does not exist!')

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        return '{' + result[:-1] + '}'


s = IntSet()
print(s)
s.insert(4)
s.insert(3)
s.insert(5)
s.insert(3)
print(s)
print(s.member(7))
print(s.member(4))
s.delete(5)
s.delete(9)
print(s)
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
