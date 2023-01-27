def checkered_board():
    r = int(input("enter row: "))
    c = int(input("enter column: "))

    board = c* "#"

    for i in range(r):
        print(board)

checkered_board()