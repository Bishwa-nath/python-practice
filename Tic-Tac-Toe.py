# Initial board of the game.
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def show_board(board):
    # show after every move.
    print("+-+-+-+")
    print("|" + board['7'] + "|" + board['8'] + "" + "|" + board['9'] + "|")
    print("+-+-+-+")
    print("|" + board['4'] + "|" + board['5'] + "" + "|" + board['6'] + "|")
    print("+-+-+-+")
    print("|" + board['1'] + "|" + board['2'] + "" + "|" + board['3'] + "|")
    print("+-+-+-+")


def main():
    show_board(theBoard)
    count = 0
    x = 'X'
    for i in range(20):
        print("Player " + x + " try, move which place? ")
        n = input()
        if theBoard[n] == ' ':
            theBoard[n] = x
            count += 1
            show_board(theBoard)
        else:
            print("This cell is already filled... try again")
            continue
        # Check whether player X or O won after 5 moves...
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                print("Congratulations! winner is", x)
                print("Game over")
                break

        # Change the player after every move
        if x == 'X':
            x = 'O'
        else:
            x = 'X'

        # Stop the game.
        if count == 9:
            print("It's tie.\nGame over")
            break

    # Restart the game
    print("Do you want to try again (y/n)?")
    y = input()
    if y == 'y' or y == 'Y' or y == 'yes':
        for k in theBoard.keys():
            theBoard[k] = ' '
        main()


if __name__ == "__main__":
    main()
