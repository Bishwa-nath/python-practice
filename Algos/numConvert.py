n = 12
bi = ''

while n:
    x = n % 2
    bi = str(x) + bi
    n //= 2

print(bi)