def role_select():
    """
    Let the user choose between playing as X or O.
    """
    role = input('Would you like to play as x or o? ')
    if role == 'x' or role == 'o':
        selection = {role}
        print(f'You chose {role}\n')
    else:
        print(f'{role} is not a valid input.\n')
    return selection

def create_board ():
    """
    Creates a 3 x 3 playing field which the game will take place on.
    """
    board = ['.','.','.','.','.','.','.','.','.',]
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

create_board()


def main():
    role_select()


print('Welcome to Tic Tac Toe!\n')
#main()
