<<<<<<< HEAD
a = "abcbcd"
res = ''
c = ''
for char in a:
    if c == '':
        c += char
    elif c[-1] <= char:
        c += char
    else:
        if len(res) < len(c):
            res = c
            c = char
        else:
            c = char

if len(res) < len(c):
    res = c

print(res)

=======
a = "abcbcd"
res = ''
c = ''
for char in a:
    if c == '':
        c += char
    elif c[-1] <= char:
        c += char
    else:
        if len(res) < len(c):
            res = c
            c = char
        else:
            c = char

if len(res) < len(c):
    res = c

print(res)

>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
