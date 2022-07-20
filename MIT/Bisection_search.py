<<<<<<< HEAD
def bisection_search(L, e):
    l = 0
    h = len(L)
    while(l<h):
        mid = (l+h)//2
        if L[mid] == e:
            return True
        elif L[mid] < e:
            l = mid+1
        else:
            h = mid
    return False


L = [2, 3, 4, 7, 8, 14, 15]
print(bisection_search(L, 15))
print(bisection_search(L, 10))
=======
def bisection_search(L, e):
    l = 0
    h = len(L)
    while(l<h):
        mid = (l+h)//2
        if L[mid] == e:
            return True
        elif L[mid] < e:
            l = mid+1
        else:
            h = mid
    return False


L = [2, 3, 4, 7, 8, 14, 15]
print(bisection_search(L, 15))
print(bisection_search(L, 10))
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
