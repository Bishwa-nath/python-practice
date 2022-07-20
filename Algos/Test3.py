<<<<<<< HEAD
strr = 'abdpstuxy'
char = 'v'


def isin(char, strr):
    if strr == '':
        return False
    mid = len(strr)//2
    if char == strr[mid]:
        return True
    elif char > strr[mid]:
        return isin(char, strr[mid+1:])
    else:
        return isin(char, strr[:mid])


print(isin(char, strr))
=======
strr = 'abdpstuxy'
char = 'v'


def isin(char, strr):
    if strr == '':
        return False
    mid = len(strr)//2
    if char == strr[mid]:
        return True
    elif char > strr[mid]:
        return isin(char, strr[mid+1:])
    else:
        return isin(char, strr[:mid])


print(isin(char, strr))
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
