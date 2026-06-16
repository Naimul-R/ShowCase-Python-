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
            continue
        if col < 1 or col > len(board[row]):
            print("Invalid col, try again!!")
            continue


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print_board(board)