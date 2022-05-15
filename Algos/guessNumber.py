print('Please think of a number between 0 and 100!')
lo = 0
h = 100
ans = (lo+h)//2
print('Is your secret number ' + str(ans) + '?')
char = str(input('Enter \'h\' to indicate the guess is too high. '
             'Enter \'l\' to indicate the guess is too low. '
             'Enter \'c\' to indicate I guessed correctly. '))

if char == 'h':
    h = ans
elif char == 'l':
    lo = ans
ans = (lo+h)//2

while char != 'c':
    print('Is your secret number ' + str(ans) + '?')
    char = str(input('Enter \'h\' to indicate the guess is too high. '
             'Enter \'l\' to indicate the guess is too low. '
             'Enter \'c\' to indicate I guessed correctly. '))
    if char == 'h':
        h = ans
    elif char == 'l':
        lo = ans
    elif char == 'c':
        print('Game over. Your secret number was:', ans)
    else:
        print('Sorry, I did not understand your input.')
    ans = (lo+h)//2




