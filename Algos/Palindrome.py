<<<<<<< HEAD
s = input('Enter a string: ')


def ispalindrome(s):
    return s == s[::-1]

ans = ispalindrome(s)
if ans:
    print(s, 'is palindrome')
else:
=======
s = input('Enter a string: ')


def ispalindrome(s):
    return s == s[::-1]

ans = ispalindrome(s)
if ans:
    print(s, 'is palindrome')
else:
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
    print(s, 'is not palindrome')