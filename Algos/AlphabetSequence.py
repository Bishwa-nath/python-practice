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

