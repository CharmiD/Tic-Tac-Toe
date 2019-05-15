def printBoard():
    VerticalLine = '   |   |'
    HorizontalLine = '-----------'

    for x in range(3):
        print(VerticalLine)
        if (x != 2):
            print(HorizontalLine)

def determineSign(userSign):
    if (userSign == 'O'):
        computerSign = 'X'
    else:
        computerSign = 'O'
    return computerSign


print("A Game of Tic-Tac-Toe!")
userSign = raw_input("Enter the sign you want to be (X or O): ")
computerSign = determineSign(userSign)

printBoard()