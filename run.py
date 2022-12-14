"""
import for copy and random function
"""
import random
import copy
import sys


BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
WINNER = False
PLAYER1 = ''
PLAYER2 = ''
GAMEMODE = ''


def gamemode():
    """
    Allows user to select the gamemode
    """
    global GAMEMODE, PLAYER1, PLAYER2

    select = input("""
Choose gamemode:
a) normal
b) impossible
c) pvp
>""").capitalize()

    if select in ['A', 'B', 'C']:
        GAMEMODE = select
        if GAMEMODE == 'C':
            PLAYER1 = 'X'
            PLAYER2 = 'O'
            choose_place()
        else:
            role_select()
    else:
        print(f'{select} is not a valid input')
        gamemode()


def role_select():
    """
    Let the user choose between playing as X or O. X will always go first.
    """
    global PLAYER1, PLAYER2

    PLAYER1 = input('\nWould you like to play as x or o? > ').capitalize()

    if PLAYER1 in ['X', 'O']:
        print(f"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           You chose {PLAYER1}
ooooooooooooooooooooooooooooooooooo""")
        PLAYER1 = 'X' if PLAYER1 == 'X' else 'O'
        PLAYER2 = 'O' if PLAYER1 == 'X' else 'X'
        choose_place() if PLAYER1 == 'X' else opponent_choose_place()
    else:
        print(f'{PLAYER1} is not a valid input.\n')
        role_select()


def create_board():
    """
    Creates a 3 x 3 playing field which the game will take place on. Also
    checks for wins or ties.
    """
    print()
    print(f'         {BOARD[0:3]}')
    print()
    print(f'         {BOARD[3:6]}')
    print()
    print(f'         {BOARD[6:9]}')


def instructions():
    """
    prints instructions on the console when called
    """
    print("""
The board looks like this:
         [1     2     3]

         [4     5     6]

         [7     8     9]
Each location on the board has a corresponding number.
Top left being 1 and bottom right being 9 and so on.
Once you make your move it will be the opponents turn.
            """)
    choose_place()


def choose_place():
    """
    Lets user decide where to place their mark.
    """
    global BOARD, PLAYER1

    create_board()
    move = input('\nChoose a location between 1 and 9 > ')
    if move == 'help':
        instructions()
    else:
        try:
            move = int(move) - 1
        except ValueError:
            print(f'''
{move} is an invalid input,
type "help" for instructions''')
            choose_place()

        if move <= 8 and move >= 0:
            if BOARD[move] == '.':
                BOARD[move] = PLAYER1
                create_board()
                check_winner(BOARD)
                opponent_choose_place()
            else:
                print('\nlocation occupied')
                choose_place()
        else:
            print('\nmove needs to be between 1 and 9')
            choose_place()


def get_possible_moves(board):
    """
    gets the indexes of all unmarked places
    """
    possible_moves = []
    for place in range(0, 9):
        if board[place] == '.':
            possible_moves.append(place)
    return possible_moves


def minimax(board, maximizing):
    """
    plays out possible end game scenarios and
    returns the winning moves
    """

    case = check_winner(board)

    if case == 1:
        return 1, None

    if case == 2:
        return -1, None

    elif '.' not in board:
        return 0, None

    if maximizing:
        max_score = -2
        best_move = None

        for move in get_possible_moves(board):
            temp = copy.deepcopy(board)
            temp[move] = PLAYER1
            score = minimax(temp, False)[0]
            if score > max_score:
                max_score = score
                best_move = move

        return max_score, best_move

    elif not maximizing:
        min_score = 2
        best_move = None

        for move in get_possible_moves(board):
            temp = copy.deepcopy(board)
            temp[move] = PLAYER2
            score = minimax(temp, True)[0]
            if score < min_score:
                min_score = score
                best_move = move

        return min_score, best_move


def opponent_choose_place():
    """
    allows player2 to make a move
    """
    global PLAYER2, BOARD

    # normal difficulty
    if GAMEMODE == 'A':
        move = random.choice(get_possible_moves(BOARD))
        BOARD[move] = PLAYER2
        print(f'\nopponent chose to mark {move + 1}')
        check_winner(BOARD)
        choose_place()
    # impossible difficulty
    elif GAMEMODE == 'B':
        print('\nopponent making move...')
        move = minimax(BOARD, False)[1]
        BOARD[move] = PLAYER2
        print(f'\nopponent chose to mark {move + 1}')
        check_winner(BOARD)
        choose_place()
    # pvp gamemode
    elif GAMEMODE == 'C':
        move = input('\nchoose a location between 1 and 9 >')
        if move == 'help':
            instructions()
        else:
            try:
                move = int(move) - 1
            except ValueError:
                print(f'\n{move} is not a valid input')
                opponent_choose_place()

            if move >= 0 and move <= 8:
                if BOARD[move] == '.':
                    BOARD[move] = PLAYER2
                    check_winner(BOARD)
                    choose_place()
                else:
                    print('\nlocation occupied')
                    opponent_choose_place()
            else:
                print('\nMove needs to be between 1 and 9')
                opponent_choose_place()


def check_winner(board):
    """
    checks if there is a winner or tie
    """
    global WINNER

    # winning end states
    winners = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
        ]

    for a, b, c in winners:
        if (PLAYER1) == board[a] == board[b] == board[c]:
            WINNER = True
            if board == BOARD:
                print(F"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
              {PLAYER1} wins!
ooooooooooooooooooooooooooooooooooo""")
                create_board()
                play_again()
                return 1
            else:
                return 1
        elif (PLAYER2) == board[a] == board[b] == board[c]:
            WINNER = True
            if board == BOARD:
                print(F"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
              {PLAYER2} wins!
ooooooooooooooooooooooooooooooooooo""")
                create_board()
                play_again()
                return 2
            else:
                return 2

    if '.' not in BOARD:
        print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           It's a tie!
ooooooooooooooooooooooooooooooooooo""")
        create_board()
        play_again()

    return 0


def play_again():
    """
    Allows the player to choose to play again or not
    """
    global BOARD, WINNER

    try_again = input('\nWould you like to play again? yes or no > ').upper()
    if try_again == 'YES':
        BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        WINNER = False
        if PLAYER1 == 'O':
            opponent_choose_place()
        else:
            choose_place()
    elif try_again == 'NO':
        print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
       Thank you for playing!
ooooooooooooooooooooooooooooooooooo
""")
        sys.exit()
    else:
        print(f'{try_again} is an invalid input')
        play_again()


print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
      Welcome to Tic Tac Toe!
ooooooooooooooooooooooooooooooooooo""")

gamemode()
