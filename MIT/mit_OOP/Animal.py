<<<<<<< HEAD
import random


class Animal():
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, name=""):
        self.name = name

    def __str__(self):
        return "Animal: " + str(self.name) + ": " + str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow...")

    def __str__(self):
        return "Cat: " + str(self.name) + ": " + str(self.age)


class Rabbit(Animal):
    def speak(self):
        print("meep...")

    def __str__(self):
        return "Rabbit: " + str(self.name) + ": " + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def set_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("Hello...")

    def age_diff(self, other):
        # diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < .5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age) + ": " + str(self.major)

# a1 = Animal(4)
# print(a1)
# a1.set_name("Puppy")
# print(a1)
# print(a1.get_age())
#
# c1 = Cat(1)
# print(c1)
# c1.set_name("Tomus")
# print(c1)
# print(c1.speak())
#

eric = Person("Eric", 34)
peter = Student("Peter", 24, "CSE 413")
print(peter)
print(peter.speak())
print(peter.speak())
print(peter.speak())
print(peter.speak())
print(peter.speak())
=======
import random


class Animal():
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, name=""):
        self.name = name

    def __str__(self):
        return "Animal: " + str(self.name) + ": " + str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow...")

    def __str__(self):
        return "Cat: " + str(self.name) + ": " + str(self.age)


class Rabbit(Animal):
    def speak(self):
        print("meep...")

    def __str__(self):
        return "Rabbit: " + str(self.name) + ": " + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def set_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("Hello...")

    def age_diff(self, other):
        # diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < .5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age) + ": " + str(self.major)

# a1 = Animal(4)
# print(a1)
# a1.set_name("Puppy")
# print(a1)
# print(a1.get_age())
#
# c1 = Cat(1)
# print(c1)
# c1.set_name("Tomus")
# print(c1)
# print(c1.speak())
#

eric = Person("Eric", 34)
peter = Student("Peter", 24, "CSE 413")
print(peter)
print(peter.speak())
print(peter.speak())
print(peter.speak())
print(peter.speak())
print(peter.speak())
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
