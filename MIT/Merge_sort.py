def merge_sort(ls):
    if len(ls) < 2:
        return ls[:]
    else:
        mid = len(ls)//2
        left = merge_sort(ls[:mid])
        right = merge_sort(ls[mid:])
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


ls = [3, 1, 9, 4, 2, 8, 6, 7, 29, 10]
print(merge_sort(ls))
