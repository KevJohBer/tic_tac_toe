import random


BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
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
    global WINNER, PLAYING
    print(BOARD[0:3])
    print()
    print(BOARD[3:6])
    print()
    print(BOARD[6:9])

    for a, b, c in WINNERS:
        if (PLAYER1) == BOARD[a] == BOARD[b] == BOARD[c]:
            print(f'\n{PLAYER1} wins!')
            WINNER = True
            PLAYING = False
        elif (PLAYER2) == BOARD[a] == BOARD[b] == BOARD[c]:
            print(f'\n{PLAYER2} wins!')
            WINNER = True
            PLAYING = False
    if ('.' not in BOARD) and (not WINNER):
        print("\nIt's a tie!")
        PLAYING = False


def choose_place():
    """
    Lets user decide where to place their mark.
    """
    global BOARD, PLAYER1, PLAYING
    while PLAYING:
        move = input('\nWhere will you place your mark? ')
        try:
            move = int(move) - 1
            if BOARD[move] == '.':
                BOARD[move] = PLAYER1
                opponent_choose_place()
            elif (move > 8) or (move < 0):
                print('Value must be between 1 and 9\n')
            elif BOARD[move] != '.':
                print(f'\n{move + 1} is already occupied')
        except ValueError:
            print(f'{move} is an invalid input')
    play_again()


def opponent_choose_place():
    """
    Makes computer do a move against the player.
    """
    global PLAYER1, PLAYER2, PLAYING
    computer_move = random.randint(0, 8)
    if PLAYER1 == 'X':
        PLAYER2 = 'O'
    elif PLAYER1 == 'O':
        PLAYER2 = 'X'

    if '.' in BOARD:
        if BOARD[computer_move] == '.':
            BOARD[computer_move] = PLAYER2
            create_board()
        else:
            opponent_choose_place()
    else:
        create_board()


def play_again():
    """
    Allows the player to choose to play again or not
    """
    global BOARD, PLAYING
    try_again = input('Would you like to play again? ')
    try:
        if try_again == 'yes':
            BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
            PLAYING = True
            create_board()
            choose_place()
        elif try_again == 'no':
            exit()
    except ValueError():
        if (try_again != 'yes') and (try_again != 'no'):
            print(f'{try_again} is not a valid input')


print('Welcome to Tic Tac Toe!\n')

role_select()
