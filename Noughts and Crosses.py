import random
# def creategrid(position):
#
#     """This function will create the grid for the game
#     :param position: Any number from 1-16.
#     :return: the grid of 4*4 on which the game is played
#     # >>> weapon_to_beat('rock')
#         |   |   |
#     ---------------
#         |   |   |
#     ---------------
#         |   |   |
#     ---------------
#         |   |   |
#     """
#     print(' ' + position[13] + ' | ' + position[14] + ' | ' + position[15] + ' | ' + position[16])
#     print('---------------')
#     print(' ' + position[9] + ' | ' + position[10] + ' | ' + position[11] + ' | ' + position[12])
#     print('---------------')
#     print(' ' + position[5] + ' | ' + position[6] + ' | ' + position[7] + ' | ' + position[8])
#     print('---------------')
#     print(' ' + position[1] + ' | ' + position[2] + ' | ' + position[3] + ' | ' + position[4])


def makepattern(coordinate, character):

    """This function determines the winning combination of the game.
    :param coordinate: It identifies the coordinates from 1-16.
    :param character: It identifies the symbol i.e 'X' , 'O', or 'T'.
    :return: This returns True if the game is won by any player.
    """

    return ((coordinate[14] == character and coordinate[15] == character and coordinate[16] == character) or  # Horizontally at the top
            (coordinate[13] == character and coordinate[14] == character and coordinate[15] == character) or  # Horizontally at the top
            (coordinate[10] == character and coordinate[11] == character and coordinate[12] == character) or  # Horizontally at the top 2nd pane
            (coordinate[9] == character and coordinate[10] == character and coordinate[11] == character) or  # Horizontally at the top 2nd pane
            (coordinate[6] == character and coordinate[7] == character and coordinate[8] == character) or  # Horizontally at the top 3rd pane
            (coordinate[5] == character and coordinate[6] == character and coordinate[7] == character) or  # Horizontally at the top 3rd pane
            (coordinate[2] == character and coordinate[3] == character and coordinate[4] == character) or  # Horizontally at the coordinatettom pane
            (coordinate[1] == character and coordinate[2] == character and coordinate[3] == character) or  # Horizontally at the coordinatettom pane
            (coordinate[13] == character and coordinate[9] == character and coordinate[5] == character) or  # Vertically at the leftmost pane
            (coordinate[9] == character and coordinate[5] == character and coordinate[1] == character) or  # Vertically at the leftmost pane
            (coordinate[14] == character and coordinate[10] == character and coordinate[6] == character) or  # Vertically at the 2nd left pane
            (coordinate[10] == character and coordinate[6] == character and coordinate[2] == character) or  # Vertically at the 2nd left pane
            (coordinate[15] == character and coordinate[11] == character and coordinate[7] == character) or  # Vertically at the 3rd left pane
            (coordinate[11] == character and coordinate[7] == character and coordinate[3] == character) or  # Vertically at the 3rd left pane
            (coordinate[16] == character and coordinate[12] == character and coordinate[8] == character) or  # Vertically at the rightmost pane
            (coordinate[12] == character and coordinate[8] == character and coordinate[4] == character) or  # Vertically at the rightmost pane
            (coordinate[15] == character and coordinate[10] == character and coordinate[5] == character) or  # Diagonally
            (coordinate[16] == character and coordinate[11] == character and coordinate[6] == character) or  # Diagonally
            (coordinate[12] == character and coordinate[7] == character and coordinate[2] == character) or  # Diagonally
            (coordinate[13] == character and coordinate[10] == character and coordinate[7] == character) or  # Diagonally
            (coordinate[9] == character and coordinate[6] == character and coordinate[3] == character) or  # Diagonally
            (coordinate[14] == character and coordinate[11] == character and coordinate[8] == character) or  # Diagonally
            (coordinate[11] == character and coordinate[6] == character and coordinate[1] == character) or  # Diagonally
            (coordinate[10] == character and coordinate[7] == character and coordinate[4] == character))  # Diagonally

def sequenceofplayers():

    """This function is used to select the order of the players randomly.
    :param : No parameter is passed to this function
    :return: The random order in which the player goes in each game.
    """

    c = random.randrange(0, 5)
    if c == 0:
        return ['computer', 'p1', 'p2']
    elif c == 1:
        return ['computer', 'p2', 'p1']
    elif c == 2:
        return ['p1', 'computer', 'p2']
    elif c == 3:
        return ['p1', 'p2', 'computer']
    elif c == 4:
        return ['p2', 'computer', 'p1']
    elif c == 5:
        return ['p2', 'p1', 'computer']


def select_sym_sequence():

    """This function selects the order of the symbols assigned to the players randomly.
    :param : No parameter is passed to this function
    :return: The random order in which the symbols are assigned to each player.
    """

    d = random.randrange(0, 5)
    if d == 0:
        return ['X', 'T', 'O']
    elif d == 1:
        return ['X', 'O', 'T']
    elif d == 2:
        return ['T', 'X', 'O']
    elif d == 3:
        return ['T', 'O', 'X']
    elif d == 4:
        return ['O', 'X', 'T']
    elif d == 5:
        return ['O', 'T', 'X']


def newposition(position):

    """This function makes a duplicate of the position list and return it the duplicate.
    :param position: It identifies the position from the list.
    :return: This returns duplicate list of the positions.
    """
    counter_pos = []
    for i in position:
        counter_pos.append(i)
    return counter_pos


def position_avail(position, move):

    """This function returns true if the new selected position is empty."""
    return position[move] == ' '


def chooseRandomMoveFromList(position, movesList):

    """This function checks if the move which AI is making is valid or not
    :param position: It identifies the position of the player.
    :param movesList:
    :return:
    """

    possibleMoves = []
    for i in movesList:
        if position_avail(position, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def choosecompturn(position, computersymbol, playersymbol1, playersymbol2):

    # Selecting position for next move for the smartest AI 1.
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            # makeMove(copy, computersymbol, i)
            copy[i] = computersymbol
            if makepattern(copy, computersymbol):
                return i

    # Check if the other AI's could win on their next move, and block them.
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


def is_position_available(position):

    """This function checks weather all the coordinates in the grid are filled.
    :param position: It identifies the position.
    :return:
    """
    for i in range(1, 17):
        if position_avail(position, i):
            return False
    return True


def smart_AI(position, computersymbol, playersymbol1, playersymbol2):
    # Selecting position for next move for its own
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = playersymbol1
            if makepattern(copy, playersymbol1):
                return i

    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            # makeMove(copy, computersymbol, i)
            copy[i] = computersymbol
            if makepattern(copy, computersymbol):
                return i
    m_centre = chooseRandomMoveFromList(position, [6, 7, 10, 11])
    if m_centre != None:
        return m_centre

    move = chooseRandomMoveFromList(position, [1, 4, 13, 16])
    if move != None:
        return move

    return chooseRandomMoveFromList(position, [2, 3, 5, 9, 8, 12, 14, 15])


def player1_play():
    move = smart_AI(theposition, computersymbol, playersymbol1, playersymbol2)
    theposition[move] = playersymbol1
    if makepattern(theposition, playersymbol1):
        # creategrid(theposition)
        print('We are sorry but our p1 has won the game!!')
        print('--------------------------------------------------------------')
        return 1
    else:
        if is_position_available(theposition):
            # creategrid(theposition)
            print('The game resulted in a tie.')
            print('--------------------------------------------------------------')
            return 2
        else:
            return 3


def dumb_AI(position, computersymbol, playersymbol1, playersymbol2):
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
            copy[i] = computersymbol
            if makepattern(copy, computersymbol):
                return i
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            # makeMove(copy, computersymbol, i)
            if makepattern(copy, playersymbol2):
                return i

    move = chooseRandomMoveFromList(position, [1, 4, 13, 16])
    if move != None:
        return move
    m_centre = chooseRandomMoveFromList(position, [6, 7, 10, 11])
    if m_centre != None:
        return m_centre
    return chooseRandomMoveFromList(position, [2, 3, 5, 9, 8, 12, 14, 15])


def player2_play():
    move = dumb_AI(theposition, computersymbol, playersymbol1, playersymbol2)
    theposition[move] = playersymbol2
    if makepattern(theposition, playersymbol2):
        # creategrid(theposition)
        print('We are sorry but our p2 has won the game!!')
        print('--------------------------------------------------------------')
        return 1
    else:
        if is_position_available(theposition):
            # creategrid(theposition)
            print('The game resulted in a tie.')
            print('--------------------------------------------------------------')
            return 2
        else:
            # turn1 = 'p1'
            return 3

def computer_play():
    move = choosecompturn(theposition, computersymbol, playersymbol1, playersymbol2)
    theposition[move] = computersymbol
    if makepattern(theposition, computersymbol):
        # creategrid(theposition)
        print('We are sorry but our AI has won the game!!')
        print('--------------------------------------------------------------')
        return 1
    else:
        if is_position_available(theposition):
            # creategrid(theposition)
            print('The game resulted in a tie.')
            print('--------------------------------------------------------------')
            return 2
        else:
            # turn1 = 'p1'
            return 3

print('Welcome to a 4*4, a 3 Player Noughts and Crosses game.\n We have three AI in the game with some different strategy.\n To win the game, they have to place 3 X-s, O-s or 3 T-s in a row.')
print('--------------------------------------------------------------')
c1 = c2 = c3 = tie = 0
ask_user = input("How many times do you want to simulate the game?")
ask_user = int(ask_user)
print('--------------------------------------------------------------')
for i in range(0, ask_user):
    # Reset the position
    theposition = [' '] * 17
    turn = sequenceofplayers()
    turn1 = turn[0]
    turn2 = turn[1]
    turn3 = turn[2]
    print('Turn 1 is of: ', turn1,'Turn 2 is of:', turn2 ,'Turn 3 is of: ',turn3)
    playersymbol = select_sym_sequence()
    playersymbol1 = playersymbol[0]
    playersymbol2 = playersymbol[1]
    computersymbol = playersymbol[2]
    print('The symbols for each player are: Player 1 is:', playersymbol1, ',Player 2 is:', playersymbol2, ',Computer is:',computersymbol)
    continue_playing = True
    while continue_playing:
        # -------------------------- if player 1 is first, player 2 second, computer third -----------------------------------------------
        if turn1 == 'p1' and turn2 == 'p2' and turn3 == 'computer':
            check = player1_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn2 == "p2"
            else:
                break
            check2 = player2_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn3 == "computer"
            else:
                break
            check3 = computer_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "computer"
            # elif check1 or check2 or check3 == 2:
            #     tie = tie +1
            else:
                break
        # --------------- if player 1 will play first, computer second and p2 third ----------------------------------
        if turn1 == 'p1' and turn2 == 'computer' and turn3 == 'p2':
            check = player1_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn2 == "computer"
            else:
                break
            check3 = computer_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "p2"
            else:
                break
            check2 = player2_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn1 == "p1"
            # elif check1 or check2 or check3 == 2:
            #     tie = tie +1
            else:
                break
        # --------------- if player 2 will play first, p1 second and computer third ----------------------------------
        if turn1 == 'p2' and turn2 == 'p1' and turn3 == 'computer':
            check2 = player2_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn2 == "p1"
            else:
                break
            check = player1_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn1 == "p2"
            else:
                break
            check3 = computer_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "p2"
            # elif check1 or check2 or check3 == 2:
            #     tie = tie + 1
            else:
                break
        # --------------- if player 2 will play first, computer second and p1 third ----------------------------------
        if turn1 == 'p2' and turn2 == 'computer' and turn3 == 'p1':
            check2 = player2_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn2 == "computer"
            else:
                break
            check3 = computer_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "p1"
            else:
                break
            check = player1_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn1 == "p2"
            # elif check1 or check2 or check3 == 2:
            #     tie = tie +1
            else:
                break
        # --------------- if computer will play first, p2 second and p1 third ----------------------------------
        if turn1 == 'computer' and turn2 == 'p2' and turn3 == 'p1':
            check3 = computer_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn2 == "p2"
            else:
                break
            check2 = player2_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn3 == "p1"
            else:
                break
            check1 = player1_play()
            if check1 == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check1 == 3:
                turn1 == "computer"
            # elif check1 or check2 or check3 == 2:
            #     tie = tie +1
            else:
                break
        # --------------- if computer will play first, p1 second and p2 third ----------------------------------
        if turn1 == 'computer' and turn2 == 'p1' and turn3 == 'p2':
            check3 = computer_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn2 = "p1"
            else:
                break
            check = player1_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn3 == "p2"
            else:
                break
            check2 = player2_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn1 == "computer"
            # elif check1 or check2 or check3 == 2:
            #     tie = tie +1
            else:
                break

print('Percentage of winning for Player 1', (c1 / ask_user) * 100)
print('Percentage of winning for Player 2', (c2 / ask_user) * 100)
print('Percentage of winning for Computer', (c3 / ask_user) * 100)
tie = (ask_user - (c1+c2+c3))
print('Percentage of tie is', (tie / ask_user) * 100)