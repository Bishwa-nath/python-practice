<<<<<<< HEAD
def gcd(a, b):
    if b > a:
        a, b = b, a
    i = b
    while i > 0:
        if a%i == 0 and b%i == 0:
            return i
        i -= 1


print(gcd(9, 2))
=======
def gcd(a, b):
    if b > a:
        a, b = b, a
    i = b
    while i > 0:
        if a%i == 0 and b%i == 0:
            return i
        i -= 1


print(gcd(9, 2))
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
