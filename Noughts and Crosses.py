# Trying intial commit
import random

def creategrid(position):
    #We are creating the basic grid of the game by using this function.
    print(' ' + position[13] + ' | ' + position[14] + ' | ' + position[15] + ' | ' + position[16])
    print('---------------')
    print(' ' + position[9] + ' | ' + position[10] + ' | ' + position[11] + ' | ' + position[12])
    print('---------------')
    print(' ' + position[5] + ' | ' + position[6] + ' | ' + position[7] + ' | ' + position[8])
    print('---------------')
    print(' ' + position[1] + ' | ' + position[2] + ' | ' + position[3] + ' | ' + position[4])


def Player1():
    #This function returns the symbol choosed by Player 1
    symbol = ''
    while (symbol != 'X' and symbol != 'O' and symbol != 'T'):
        name1 = input('Player 1 please enter Your Name: ')
        print('Hello ', name1, 'please choose the symbol type you want to be \n Choices are: X, O, T')
        symbol = input().upper()
    if symbol == 'X':
        return ('X')
    elif symbol == 'O':
        return ('O')
    elif symbol == 'T':
        return ('T')


def Player2(p):
    # This function returns the symbol choosed by Player 2
    symbol1 = ''
    while (symbol1 != 'X' and symbol1 != 'O' and symbol1 != 'T'):
        name2 = input('Player 2 please enter Your Name: ')
        print('Hello ', name2, 'please choose the symbol type you want to be. \nPlease do not enter Player 1s choice')
        symbol1 = input().upper()
    if symbol1 == p:
        print('We are sorry but that symbol is taken')
    else:
        if p == 'X':
            if symbol1 == 'O':
                return ['O', 'T']
            else:
                return ['T', 'O']
        elif p == 'O':
            if symbol1 == 'X':
                return ['X', 'T']
            else:
                return ['T', 'X']
        else:
            if symbol1 == 'O':
                return ['O', 'X']
            else:
                return ['X', 'O']


def sequenceofplayers():
    # This function is used to select the order of the players randomly.
    if random.randrange(0, 5) == 0:
        return ['computer', 'p1', 'p2']
    elif random.randrange(0, 5) == 1:
        return ['computer', 'p2', 'p1']
    elif random.randrange(0, 5) == 2:
        return ['p1', 'computer', 'p2']
    elif random.randrange(0, 5) == 3:
        return ['p1', 'p2', 'computer']
    elif random.randrange(0, 5) == 4:
        return ['p2', 'computer', 'p1']
    elif random.randrange(0, 5) == 5:
        return ['p2', 'p1', 'computer']


def makepattern(coordinate, character):
    # Given coordinate and the symbol used, this function returns True if the game is won by a particular player.
    # Coordinate means the particular position on the grid and and character means O,X or T.
    return ((coordinate[14] == character and coordinate[15] == character and coordinate[
        16] == character) or  # Horizontally at the top
            (coordinate[13] == character and coordinate[14] == character and coordinate[
                15] == character) or  # Horizontally at the top
            (coordinate[10] == character and coordinate[11] == character and coordinate[
                12] == character) or  # Horizontally at the top 2nd pane
            (coordinate[9] == character and coordinate[10] == character and coordinate[
                11] == character) or  # Horizontally at the top 2nd pane
            (coordinate[6] == character and coordinate[7] == character and coordinate[
                8] == character) or  # Horizontally at the top 3rd pane
            (coordinate[5] == character and coordinate[6] == character and coordinate[
                7] == character) or  # Horizontally at the top 3rd pane
            (coordinate[2] == character and coordinate[3] == character and coordinate[
                4] == character) or  # Horizontally at the coordinatettom pane
            (coordinate[1] == character and coordinate[2] == character and coordinate[
                3] == character) or  # Horizontally at the coordinatettom pane
            (coordinate[13] == character and coordinate[9] == character and coordinate[
                5] == character) or  # Vertically at the leftmost pane
            (coordinate[9] == character and coordinate[5] == character and coordinate[
                1] == character) or  # Vertically at the leftmost pane
            (coordinate[14] == character and coordinate[10] == character and coordinate[
                6] == character) or  # Vertically at the 2nd left pane
            (coordinate[10] == character and coordinate[6] == character and coordinate[
                2] == character) or  # Vertically at the 2nd left pane
            (coordinate[15] == character and coordinate[11] == character and coordinate[
                7] == character) or  # Vertically at the 3rd left pane
            (coordinate[11] == character and coordinate[7] == character and coordinate[
                3] == character) or  # Vertically at the 3rd left pane
            (coordinate[16] == character and coordinate[12] == character and coordinate[
                8] == character) or  # Vertically at the rightmost pane
            (coordinate[12] == character and coordinate[8] == character and coordinate[
                4] == character) or  # Vertically at the rightmost pane
            (coordinate[15] == character and coordinate[10] == character and coordinate[
                5] == character) or  # Diagonally
            (coordinate[16] == character and coordinate[11] == character and coordinate[
                6] == character) or  # Diagonally
            (coordinate[12] == character and coordinate[7] == character and coordinate[2] == character) or  # Diagonally
            (coordinate[13] == character and coordinate[10] == character and coordinate[
                7] == character) or  # Diagonally
            (coordinate[9] == character and coordinate[6] == character and coordinate[3] == character) or  # Diagonally
            (coordinate[14] == character and coordinate[11] == character and coordinate[
                8] == character) or  # Diagonally
            (coordinate[11] == character and coordinate[6] == character and coordinate[1] == character) or  # Diagonally
            (coordinate[10] == character and coordinate[7] == character and coordinate[4] == character))  # Diagonally


def newposition(position):
    # Make a duplicate of the position list and return it the duplicate.
    counter_pos = []
    for i in position:
        counter_pos.append(i)
    return counter_pos


def position_avail(position, move):
    # This function returns true if the new selected position is empty.
    return position[move] == ' '


def chooseplayerturn(position):
    # This function asks the player to enter their turn to play the game.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not position_avail(position, int(move)):
        print('What is your next move? (1-16)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(position, movesList):
    # Checks if the move is valid or not
    possibleMoves = []
    for i in movesList:
        if position_avail(position, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def choosecompturn(position, computersymbol, playersymbol1, playersymbol2):
    #Selecting position for next move for computer
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            #makeMove(copy, computersymbol, i)
            copy[i] = computersymbol
            if makepattern(copy, computersymbol):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = playersymbol1
            if makepattern(copy, playersymbol1):
                return i
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = playersymbol2
            if makepattern(copy, playersymbol2):
                return i

    m_centre = chooseRandomMoveFromList(position, [6, 7, 10, 11])
    if m_centre != None:
        return m_centre
    move = chooseRandomMoveFromList(position, [1, 4, 13, 16])
    if move != None:
        return move

    return chooseRandomMoveFromList(position, [2, 3, 5, 9, 8, 12, 14, 15])

def playAgain():
    # True means the player wants to play the game again and false means the player wants to quit playing
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def is_position_available(position):
    # Checks weather all the coordinates in the grid are filled.
    for i in range(1, 17):
        if position_avail(position, i):
            return False
    return True


print(
    'Welcome to 4*4, a 3 Player Noughts and Crosses game.\nTo win the game, you have to place 3 X-s, O-s or 3 T-s in a row.')
print('--------------------------------------------------------------')

c1=0
c2=0
c3=0

while True:
    for i in range(0, 1):
    # Reset the position
        theposition = [' '] * 17
        playersymbol1 = Player1()
        print('Player 1 choose the symbol', playersymbol1)
        playersymbol2, computersymbol = Player2(playersymbol1)
        print('Player 2 choose the symbol', playersymbol2)
        print('So, the final choices are Player 1 is:', playersymbol1, '\nPlayer 2 is:', playersymbol2, '\nComputer is',
              computersymbol)
        turn1, turn2, turn3 = sequenceofplayers()
        print('The ' + turn1 + ' will go first.')
        print('The ' + turn2 + ' will go second.')
        print('The ' + turn3 + ' will go third.')
        continue_playing = True
        while continue_playing:
            # -------------------------- if player 1 is first, player 2 second, computer third -----------------------------------------------
            if turn1 == 'p1' and turn2 == 'p2' and turn3 == 'computer':
                # if turn1 == 'p1':
                creategrid(theposition)
                move = chooseplayerturn(theposition)
                theposition[move] = playersymbol1
                if makepattern(theposition, playersymbol1):
                    creategrid(theposition)
                    print('Congratulations Player 1, you won the game!')
                    c1=c1+1
                    continue_playing = False
                else:
                    if is_position_available(theposition):
                        creategrid(theposition)
                        print('The game resulted in a tie.')
                        break
                    else:
                        turn2 = 'p2'
                creategrid(theposition)
                move = chooseplayerturn(theposition)
                theposition[move] = playersymbol2
                if makepattern(theposition, playersymbol2):
                    creategrid(theposition)
                    print('Congratulations Player 2, you won the game!')
                    c2=c2+1
                    continue_playing = False
                else:
                    if is_position_available(theposition):
                        creategrid(theposition)
                        print('The game resulted in a tie.')
                        break
                    else:
                        turn3 = 'computer'

                move = choosecompturn(theposition, computersymbol, playersymbol1, playersymbol2)
                theposition[move] = computersymbol
                print('The computer moved at position:', move)
                if makepattern(theposition, computersymbol):
                    creategrid(theposition)
                    print('We are sorry but our AI has won the game!!')
                    c3=c3+1
                    continue_playing = False
                else:
                    if is_position_available(theposition):
                        creategrid(theposition)
                        print('The game resulted in a tie.')
                        break
                    else:
                        turn1 = 'p1'