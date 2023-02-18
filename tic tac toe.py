import random

board = [' ' for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def computer_move(icon):
    if icon == 'X':
        number = 2
    elif icon == 'O':
        number = 1
    print("Your turn player {}".format(number))
    while True:
        choice = random.randint(0, 8)
        if board[choice] == ' ':
            board[choice] = icon
            break

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

player_choice = input("Do you want to play against a player (P) or against the computer (C)? ")

while player_choice != 'P' and player_choice != 'C':
    player_choice = input("Invalid input. Do you want to play against a player (P) or against the computer (C)? ")

while True:
    print_board()
    if player_choice == 'P':
        player_move('X')
        if is_victory('X'):
            print_board()
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
        player_move('O')
        if is_victory('O'):
            print_board()
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
    elif player_choice == 'C':
        player_move('X')
        if is_victory('X'):
            print_board()
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
        computer_move('O')
        if is_victory('O'):
            print_board()
            print("O wins! Congratulations computer!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
    else:
        print("Invalid input, please try again")
