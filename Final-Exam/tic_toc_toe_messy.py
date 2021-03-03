# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """
    Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    """ Randomly choose the player who goes first. """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    """This function returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    """
    Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much.
    """
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle    # TODO: Fix the indentation of this lines and the following ones.
            (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def getBoardCopy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    return [item for item in board]

def is_space_free(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def getPlayerMove(board):
    """Let the player type in their move."""
    global move
    move = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moves_list):
    """
    Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move.
    """
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    # TODO: How would you write this pythanically? (You can google for it!)
    if possible_moves:
        return random.choice(possible_moves)
    return None

def getComputerMove(board, computerLetter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """Given a board and the computer's letter, determine where to move and return that move."""
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if is_space_free(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if is_space_free(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

def game_setup():
    """Creates the board, sets player letters, and chooses who goes first"""
    BOARD_SPACES = 10
    the_board = [' '] * BOARD_SPACES # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    playerLetter, computer_letter = input_player_letter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    return the_board, playerLetter, computer_letter, turn

def player_turn(board, player_letter):
    """
    Will run through players turn, will return if the game ends
    and which turn is next
    """
    drawBoard(board)
    move = getPlayerMove(board)
    makeMove(board, player_letter, move)

    if isWinner(board, player_letter):
        drawBoard(board)
        print('Hooray! You have won the game!')
        return 'computer', True
    elif isBoardFull(board):
        drawBoard(board)
        print('The game is a tie!')
        return 'computer', True
    return 'computer', False

def computer_turn(board, computer_letter):
    """
    Runs through the computers turn, will return if game ends
    and which turn is next
    """
    move = getComputerMove(board, computer_letter)
    makeMove(board, computer_letter, move)

    if isWinner(board, computer_letter):
        drawBoard(board)
        print('The computer has beaten you! You lose.')
        return 'player', True
    elif isBoardFull(board):
        drawBoard(board)
        print('The game is a tie!')
        return 'player', True
    return 'player', False

def game_play():
    """Starting the game and going through each step of game play"""
    print('Welcome to Tic Tac Toe!')
    # TODO: The following mega code block is a huge hairy monster. Break it down 
    # into smaller methods. Use TODO s and the comment above each section as a guide 
    # for refactoring.
    while True:
        the_board, player_letter, computer_letter, turn = game_setup()
        while True: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                            #       Use a meaningful name for the function you choose.
            if turn == 'player':
                # Player's turn
                turn, is_end = player_turn(the_board,player_letter)
                if is_end:
                    break

            else:
                # Computer’s turn.
                turn, is_end = computer_turn(the_board,computer_letter)
                if is_end:
                    break

        if not playAgain():
            break

if __name__ == "__main__":
    game_play()
