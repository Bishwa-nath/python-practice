<<<<<<< HEAD
def bubble_sort(L):

    swap = False
    while not swap:
        swap = True
        for i in range(1, len(L)):
            if L[i] < L[i-1]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]
                # temp = L[i-1]
                # L[i-1] = L[i]
                # L[i] = temp
    return L


L = [5, 2, 3, 7, 1, 10, 9, 2]
print(bubble_sort(L))
=======
def bubble_sort(L):

    swap = False
    while not swap:
        swap = True
        for i in range(1, len(L)):
            if L[i] < L[i-1]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]
                # temp = L[i-1]
                # L[i-1] = L[i]
                # L[i] = temp
    return L


L = [5, 2, 3, 7, 1, 10, 9, 2]
print(bubble_sort(L))
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
