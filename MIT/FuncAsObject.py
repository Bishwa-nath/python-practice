def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def func_as_obj(L, f):
    for e in range(len(L)):
        L[e] = f(L[e])
    print(L)


L = [1, 4.5, -3.9, 7.5, 6.2]
func_as_obj(L, abs)
func_as_obj(L, int)
func_as_obj(L, fact)
