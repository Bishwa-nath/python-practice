animals = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse', 'dog']

for word in words:
    if word in animals:
        print(word, '->', animals[word])
    else:
        print(word, 'is not in dictionary!')
