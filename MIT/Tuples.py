def quotient_and_reminder(x, y):
    q = x // y
    r = x % y
    return q, r


(quot, rem) = quotient_and_reminder(17, 3)

print(quot, rem)
