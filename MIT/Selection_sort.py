def selection_sort(ls):
    for i in range(len(ls) - 1):
        print(ls)
        minIndx = i
        minVal = ls[i]
        j = i+1
        while j < len(ls):
            if ls[j] < minVal:
                minIndx = j
                minVal = ls[j]
            j += 1
        ls[i], ls[minIndx] = ls[minIndx], ls[i]


ls = [4, 1, 9, 20, 3, 11, 7, 6]
print(selection_sort(ls))
