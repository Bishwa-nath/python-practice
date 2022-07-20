<<<<<<< HEAD
s = "bobbobobmeodlobobdob"
ss = 'bob'


def subsequence(s, ss):
    n = len(s)
    m = len(ss)
    res = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if s[i+j] != ss[j]:
                break
            j += 1

        if j == m:
            res += 1
            j = 0

    return res


ans = subsequence(s, ss)
print(ans)
=======
s = "bobbobobmeodlobobdob"
ss = 'bob'


def subsequence(s, ss):
    n = len(s)
    m = len(ss)
    res = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if s[i+j] != ss[j]:
                break
            j += 1

        if j == m:
            res += 1
            j = 0

    return res


ans = subsequence(s, ss)
print(ans)
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
