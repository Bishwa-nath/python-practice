marks = {
    'math': 83,
    'english': 78,
    'cs': 89,
    'eee': 70,
    'chy': 67
}

for key in sorted(marks.keys()):
    print(key, "->", marks[key])
marks.pop('cs')
print()
for key in sorted(marks.keys()):
    print(key, "->", marks[key])
print()
marks['eee'] = 97
print(marks)
marks['algo'] = 80
marks['ai'] = 75
print(marks)
