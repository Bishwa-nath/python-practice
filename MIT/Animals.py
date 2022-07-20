<<<<<<< HEAD
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(animals):
    big = 0
    for k in animals:
        if len(animals[k]) > big:
            big = len(animals[k])

    for k in animals:
        if len(animals[k]) == big:
            return k

print(how_many(animals))
=======
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(animals):
    big = 0
    for k in animals:
        if len(animals[k]) > big:
            big = len(animals[k])

    for k in animals:
        if len(animals[k]) == big:
            return k

print(how_many(animals))
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
