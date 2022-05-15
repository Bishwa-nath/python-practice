import datetime as dt


class Person(object):
    def __init__(self, name):
        """Creates a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """returns self's last name"""
        return self.lastName

    def setBirthday(self, day, month, year):
        """Sets self's birthday to birthDate"""
        self.birthday = dt.date(year, month, day)

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (dt.date.today() - self.birthday).days

    def __lt__(self, other):
        """ returns True if self's name is lexicographically less
        than other's name, and False otherwise """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName  # sorted according to lastName

    def __str__(self):
        """ Returns self's name """
        return self.name


class MITperson(Person):
    nextID = 1

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITperson.nextID
        MITperson.nextID += 1

    def getIDnum(self):
        return self.idNum

    def __lt__(self, other):
        # Sort by id number
        return self.idNum < other.idNum

    def speak(self, utterance):
        return self.getLastName() + " says " + utterance


# p1 = Person('Bishwa Nath')
# p1.setBirthday(20, 9, 1997)
# p2 = Person("Akash Ahmed")
# p2.setBirthday(5, 6, 1996)
# p3 = Person('Rezaul Karim')
# p3.setBirthday(7, 8, 1997)
# p4 = Person("Eric Saha")
# p5 = Person("Dhonesh Saha")
# personList = [p1, p2, p3, p4, p5]
# print(p1)
# print()
# for p in personList:
#     print(p)
# print()
# personList.sort()
# for p in personList:
#     print(p)
# print()
# for x in personList:
#     print(x.getLastName())

m3 = MITperson('John China')
Person.setBirthday(m3, 5, 5, 1985)
m2 = MITperson('Bill Gates')
Person.setBirthday(m2, 8, 12, 1978)
m1 = MITperson('Eric Crimson')
Person.setBirthday(m1, 23, 6, 1982)

mitList = [m1, m2, m3]

print(m2)
print()
for m in mitList:
    print(m.idNum, m)
print()
mitList.sort()
for m in mitList:
    print(m.idNum, m)
print(m3.speak('Hello Public...'))
