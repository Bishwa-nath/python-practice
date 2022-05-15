n = int(input('Enter n (1-6): '))


def towerofhanoi(n, src, dest, auxi):
    if n == 1:
        print('Move disk 1 from source', src, 'to destination', dest)
        return
    towerofhanoi(n-1, src, auxi, dest)
    print('Move disk', n, 'from source', src, 'to destination', dest)
    towerofhanoi(n-1, auxi, dest, src)


towerofhanoi(n, 'A', 'B', 'C')
