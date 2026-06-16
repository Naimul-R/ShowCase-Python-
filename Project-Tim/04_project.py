def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) -1:
                row_str += " | "

        print(row_str)
        if i != len(board) - 1:
            print("----------")

def get_move(turn, board):
    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))

        if row < 1 or row > len(board):
            print("Invalid row, try again!!")
        elif col < 1 or col > len(board[row - 1]):
            print("Invalid col, try again!!")
        elif board[row - 1][col - 1] != " ":
            print("Already taken, try again!!")
        else:
            break
    board[row - 1][col - 1] = turn


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
    print(f"It is the {turn} player's turn, please select your move.")
    get_move(turn, board)
    print_board(board)

    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1