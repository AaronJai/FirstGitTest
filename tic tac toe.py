import random
# test
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

def player_move(icon, number):
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def computer_move(icon, number):
    print("Your turn player {}".format(number))
    while True:
        choice = random.randint(0, 8)
        if board[choice] == ' ':
            board[choice] = icon
            break

def is_victory(icon):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if all(board[i] == icon for i in win):
            return True
    return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

player_choice = ''
while player_choice != 'P' and player_choice != 'C':
    player_choice = input("Do you want to play against a player (P) or against the computer (C)? ")

while True:
    print_board()
    if player_choice == 'P':
        player_move('X', 1)
        print_board()
        if is_victory('X'):
            print_board()
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
        player_move('O', 2)
        if is_victory('O'):
            print_board()
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
    elif player_choice == 'C':
        player_move('X', 1)
        if is_victory('X'):
            print_board()
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
        computer_move('O', 2)
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
