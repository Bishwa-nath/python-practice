<<<<<<< HEAD
eps = 0.00001
y = 64
guess = y / 2.0
numGuess = 0

while abs(guess*guess - y) >= eps:
    numGuess += 1
    guess = guess - (((guess**2) - y) / (2*guess))

print('numGuess: ', numGuess)
print('Square root of', y, 'is about', guess)
=======
eps = 0.00001
y = 64
guess = y / 2.0
numGuess = 0

while abs(guess*guess - y) >= eps:
    numGuess += 1
    guess = guess - (((guess**2) - y) / (2*guess))

print('numGuess: ', numGuess)
print('Square root of', y, 'is about', guess)
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
