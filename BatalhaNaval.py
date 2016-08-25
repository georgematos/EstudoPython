from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

trys = 4

for turn in range(4):
    
    print("Tentativas: %d " % (trys))

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    print("Posição do navio: %d %d " % (ship_row, ship_col))
    print("Coordenadas do tiro: %d %d " % (guess_row, guess_col))

    if guess_row not in range(5) or guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
    elif guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    elif board[guess_row][guess_col] == "X":
        print("Voce ja tentou esse.")
    else:
        board[guess_col][guess_row] = "X"
        print("You missed my battleship!")

    trys -= 1
    print_board(board)