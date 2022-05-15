s = input('Enter a string: ')


def ispalindrome(s):
    return s == s[::-1]

ans = ispalindrome(s)
if ans:
    print(s, 'is palindrome')
else:
    print(s, 'is not palindrome')