import random
board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']


def role_select():
    """
    Let the user choose between playing as X or O.
    """
    role = input('Would you like to play as x or o? ')
    if role == 'x' or role == 'o':
        print(f'You chose {role}\n')
        create_board()
        choose_place(role)
    else:
        print(f'{role} is not a valid input.\n')
        role_select()
    return role


def create_board():
    """
    Creates a 3 x 3 playing field which the game will take place on.
    """
    print(board[0:3])
    print()
    print(board[3:6])
    print()
    print(board[6:9])


def choose_place(role):
    """
    Lets user decide where to place their mark.
    """
    playing = True
    while playing:
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if role.capitalize() == board[a] == board[b] == board[c]:
                print(f'\n{role.capitalize()} wins!')
                playing = False
                return playing

        move = input('\nWhere will you place your mark? ')
        try:
            move = int(move) - 1
            if board[move] == '.':
                board[move] = role.capitalize()
                opponent_choose_place(role, playing)
            elif (move > 8) or (move < 0):
                print('Value must be between 1 and 9\n')
            elif board[move] != '.':
                print(f'\n{move + 1} is already occupied')
        except ValueError:
            print(f'{move} is an invalid input')
    if '.' not in board:
        print("It's a tie!")


def opponent_choose_place(role, playing):
    """
    Makes computer do a move against the player.
    """
    computer_move = random.randint(0, 8)
    if role == 'x':
        computer_role = 'o'
    elif role == 'o':
        computer_role = 'x'

    if board[computer_move] == '.':
        board[computer_move] = computer_role.capitalize()
        create_board()
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if computer_role.capitalize() == board[a] == board[b] == board[c]:
                print(f'\n{computer_role.capitalize()} wins!')
                playing = False
                return playing
    elif '.' not in board:
        create_board()
    else:
        opponent_choose_place(role, playing)


def main():
    """
    main
    """
    role_select()


print('Welcome to Tic Tac Toe!\n')
main()