import string
s = string.ascii_lowercase
l = ['e', 'i', 'k', 'p', 'r', 's']
for i in l:
    s = s.replace(i, "")
print(s)
