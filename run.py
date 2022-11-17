"""
import for usage of random functions
"""
import random


BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
WINNERS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
PLAYING = True
WINNER = False
PLAYER1 = ''
PLAYER2 = ''


def role_select():
    """
    Let the user choose between playing as X or O. X will always go first.
    """
    global PLAYER1, PLAYER2, PLAYING
    PLAYER1 = input('Would you like to play as x or o? >').capitalize()
    if PLAYER1 == 'X' or 'O':
        print(f"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
       You chose {PLAYER1}\n
ooooooooooooooooooooooooooooooooooo
        """)
        if PLAYER1 == 'X':
            PLAYER2 = 'O'
            choose_place()
        elif PLAYER1 == 'O':
            PLAYER2 = 'X'
            opponent_choose_place()
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
    print(f'         {BOARD[0:3]}')
    print()
    print(f'         {BOARD[3:6]}')
    print()
    print(f'         {BOARD[6:9]}')


def choose_place():
    """
    Lets user decide where to place their mark.
    """
    global BOARD, PLAYER1, PLAYING
    while PLAYING:
        create_board()
        move = input('\nWhere will you place your mark? ')
        try:
            move = int(move) - 1
            if BOARD[move] == '.':
                BOARD[move] = PLAYER1
                if not WINNER:
                    check_winner(PLAYER1)
                opponent_choose_place()
            elif (move > 8) or (move < 0):
                print('Value must be between 1 and 9\n')
            elif BOARD[move] != '.':
                print(f'\n{move + 1} is already occupied')
        except ValueError:
            print(f'{move} is an invalid input')
    create_board()
    play_again()


def opponent_choose_place():
    """
    Makes computer do a move against the player.
    """
    global PLAYER2, BOARD
    computer_move = random.randint(0, 8)

    if '.' in BOARD:
        if BOARD[computer_move] == '.':
            BOARD[computer_move] = PLAYER2
            if not WINNER:
                check_winner(PLAYER2)
        else:
            opponent_choose_place()


def check_winner(player):
    """
    checks if there is a winner or tie
    """
    global PLAYING, WINNER
    for a, b, c in WINNERS:
        if (player) == BOARD[a] == BOARD[b] == BOARD[c]:
            print(f"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
             {player} wins!
ooooooooooooooooooooooooooooooooooo
            """)
            WINNER = True
            PLAYING = False

    if ('.' not in BOARD) and (not WINNER):
        print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           It's a tie!
ooooooooooooooooooooooooooooooooooo
        """)
        PLAYING = False


def play_again():
    """
    Allows the player to choose to play again or not
    """
    global BOARD, PLAYING, WINNER
    try_again = input('\nWould you like to play again? ')
    while not PLAYING:
        if try_again == 'yes':
            BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
            PLAYING = True
            WINNER = False
            choose_place()
        elif try_again == 'no':
            exit()
        else:
            print(f'{try_again} is not a valid input')
            play_again()


print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
      Welcome to Tic Tac Toe!
ooooooooooooooooooooooooooooooooooo
""")

role_select()
