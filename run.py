"""
import for usage of random functions
"""
import random
import copy


BOARD = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
WINNERS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
PLAYING = True
WINNER = False
PLAYER1 = ''
PLAYER2 = ''
CASE = 0


def role_select():
    """
    Let the user choose between playing as X or O. X will always go first.
    """
    global PLAYER1, PLAYER2, PLAYING
    PLAYER1 = input('Would you like to play as x or o? > ').capitalize()
    if PLAYER1 == ('X' or 'O'):
        print(f"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           You chose {PLAYER1}
ooooooooooooooooooooooooooooooooooo
        """)
        if PLAYER1 == 'X':
            PLAYER2 = 'O'
            choose_place()
        elif PLAYER1 == 'O':
            PLAYER2 = 'X'
            minimax(BOARD, PLAYER2, False)
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
    print()


def choose_place():
    """
    Lets user decide where to place their mark.
    """
    global BOARD, PLAYER1, PLAYING
    while PLAYING:
        create_board()
        move = input('Choose a place between 1 and 9 > ')
        if move == 'help':
            print("""
the playing field looks like this:
        [1   2   3]
        [4   5   6]
        [7   8   9]
so 1 is top left and 9 is bottom right and so on...

Once you choose where to place your mark, the computer will
set another one out and it will be your turn again.
                    """)
        else:
            try:
                if int(move) in range(1, 10):
                    move = int(move) - 1
                if BOARD[move] == '.':
                    BOARD[move] = PLAYER1
                    if not WINNER:
                        check_winner(BOARD, PLAYER1)
                    opponent_choose_place()
                elif BOARD[move] != '.':
                    print(f'\n{move + 1} is already occupied\n')
            except:
                print(f'{move} is not a valid input, type "help" for instructions')
    create_board()
    play_again()


def get_possible_moves(board):
    """
    gets the indexes of all unmarked places
    """
    possible_moves = []
    for place in range(len(board)):
        if board[place] == '.':
            possible_moves.append(place)
    return possible_moves


def make_move(move, player, board):
    """
    makes a move
    """
    board[move] = player


def minimax(board, player, maximizing):
    """
    Minimax algorithm
    """
    case = check_winner(board, player)

    if case == 1:
        return 1, None

    if case == -1:
        return -1, None

    if case == 0:
        return 0, None

    if maximizing:
        max_score = -10
        best_move = None
        possible_moves = get_possible_moves(board)

        for move in possible_moves:
            temp = copy.deepcopy(board)
            make_move(move, PLAYER2, temp)
            score = minimax(temp, PLAYER1, False)[0]
            if score > max_score:
                max_score = score
                best_move = move

        return max_score, best_move

    elif not maximizing:
        min_score = 10
        best_move = None
        possible_moves = get_possible_moves(board)

        for move in possible_moves:
            temp = copy.deepcopy(board)
            make_move(move, PLAYER1, temp)
            score = minimax(temp, PLAYER2, True)[0]
            if score < min_score:
                min_score = score
                best_move = move

        return min_score, best_move


def opponent_choose_place():
    """
    Makes computer do a move against the player.
    """
    global PLAYER2, BOARD
    bruh, move = minimax(BOARD, PLAYER2, True)
    make_move(move, PLAYER2, BOARD)
    print(f'ai has chosed to place their mark on {move} with an eval of {bruh}')


def check_winner(board, player):
    """
    checks if there is a winner or tie
    """
    global PLAYING, WINNER

    for a, b, c in WINNERS:
        if '.' not in board:
            return 0
        else:
            if (player) == board[a] == board[b] == board[c]:

                if player == PLAYER1:
                    return 1
                elif player == PLAYER2:
                    return -1
                else:
                    return 0


def play_again():
    """
    Allows the player to choose to play again or not
    """
    global BOARD, PLAYING, WINNER
    try_again = input('Would you like to play again? > ')
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
