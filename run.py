import random
board = ['.', '.', '.', '.', '.', '.', '.', '.', '.', ]
playing = True


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
    while playing:
        move = input('Where will you place your mark? ')
        try:
            move = int(move)
            if board[int(move)] == '.':
                board[int(move)] = role.capitalize()
                create_board()
                opponent_choose_place(role)
            elif (move > len(board)) or (move < len(board)):
                print('Value must be between 0 and 8')
            else:
                print(f'{move} is already occupied')

        except ValueError:
            print(f'{move} is an invalid input')


def opponent_choose_place(role):
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
        choose_place(role)
    else:
        opponent_choose_place(role)


def main():
    """
    main
    """
    role_select()


print('Welcome to Tic Tac Toe!\n')
main()
