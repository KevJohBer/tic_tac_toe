import random


board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
WINNERS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
PLAYING = True
WINNER = False
PLAYER1 = ''
PLAYER2 = ''


def role_select():
    """
    Let the user choose between playing as X or O.
    """
    global PLAYER1
    PLAYER1 = input('Would you like to play as x or o? ').capitalize()
    if PLAYER1 == 'X' or PLAYER1 == 'O':
        print(f'You chose {PLAYER1}\n')
        create_board()
        choose_place()
    else:
        print(f'{PLAYER1} is not a valid input.\n')
        role_select()


def create_board():
    """
    Creates a 3 x 3 playing field which the game will take place on. Also
    checks for wins or ties.
    """
    print(board[0:3])
    print()
    print(board[3:6])
    print()
    print(board[6:9])

    global PLAYING, PLAYER1, PLAYER2, WINNERS
    for a, b, c in WINNERS:
        if (PLAYER1) == board[a] == board[b] == board[c]:
            print(f'\n{PLAYER1} wins!')
            PLAYING = False
        elif (PLAYER2) == board[a] == board[b] == board[c]:
            print(f'\n{PLAYER2} wins!')
            PLAYING = False


def choose_place():
    """
    Lets user decide where to place their mark.
    """
    global PLAYING, WINNER, PLAYER1
    while PLAYING:
        move = input('\nWhere will you place your mark? ')
        try:
            move = int(move) - 1
            if board[move] == '.':
                board[move] = PLAYER1.capitalize()
                opponent_choose_place()
            elif (move > 8) or (move < 0):
                print('Value must be between 1 and 9\n')
            elif board[move] != '.':
                print(f'\n{move + 1} is already occupied')
        except ValueError:
            print(f'{move} is an invalid input')


def opponent_choose_place():
    """
    Makes computer do a move against the player.
    """
    global WINNER, PLAYER1, PLAYER2, PLAYING
    computer_move = random.randint(0, 8)
    if PLAYER1 == 'X':
        PLAYER2 = 'O'
    elif PLAYER1 == 'O':
        PLAYER2 = 'X'

    if '.' in board:
        if board[computer_move] == '.':
            board[computer_move] = PLAYER2
            create_board()
        else:
            opponent_choose_place()
    else:
        create_board()
        print("\nit's a tie!")
        PLAYING = False


def main():
    """
    main
    """
    role_select()


print('Welcome to Tic Tac Toe!\n')
main()