def printBoard():
    VerticalLine = '   |   |'
    HorizontalLine = '-----------'

    for x in range(3):
        print(VerticalLine)
        if (x != 2):
            print(HorizontalLine)

print('A Game of Tic-Tac-Toe!')
userSign = input("Enter the sign you want to be (X or O): ")
print(userSign)
printBoard()
