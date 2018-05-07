import random
# def creategrid(position):
#
#     """This function will create the grid for the game
#     :param position: Any number from 1-16.
#     :return: the grid of 4*4 on which the game is played
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

def makepattern(coordinate,character):
    # Given coordinate and the symbol used, this function returns True if the game is won by a particular player.
    # Coordinate means the particular position on the grid and and character means O,X or T.
    """Determine the game winner."""
    WIN = [[ 14,15,16 ],[13,14,15 ],[ 10,11,12 ],[ 9,10,11 ],[ 6,7,8 ],[ 5,6,7 ],[ 2,3,4] ,[1,2,3 ],[13,9,5] ,[ 9,5,1 ],[14,10,6 ],[10,6,2],[15,11,7],[11,7,3],
    [16,12,8 ],[12,8,4],[15,10,5],[16,11,6],[12,7,2 ],[13,10,7 ],[ 9,6,3],[14,11,8],[11,6,1],[10,7,4]]
    k=0
    for i in WIN:
        if coordinate[i[0]] == character and coordinate[i[1]] == character and coordinate[i[2]] == character:
            k = k+1
    if k>0:
        return True
    else:
        return False


def sequenceofplayers():

    """This function is used to select the order of the players randomly.
    :param : No parameter is passed to this function
    :return: The random order in which the player goes in each game.
    """

    c = random.randrange(0, 5)
    if c == 0:
        return ['smartestAI', 'smartAI', 'dumbAI']
    elif c == 1:
        return ['smartestAI', 'dumbAI', 'smartAI']
    elif c == 2:
        return ['smartAI', 'smartestAI', 'dumbAI']
    elif c == 3:
        return ['smartAI', 'dumbAI', 'smartestAI']
    elif c == 4:
        return ['dumbAI', 'smartestAI', 'smartAI']
    elif c == 5:
        return ['dumbAI', 'smartAI', 'smartestAI']


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


def choose_smartestAI_turn(position, smartestAI_symbol, smartAI_symbol, dumbAI_symbol):

    # Selecting position for next move for the smartest AI 1.
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            # makeMove(copy, smartestAI_symbol, i)
            copy[i] = smartestAI_symbol
            if makepattern(copy, smartestAI_symbol):
                return i

    # Check if the other AI's could win on their next move, and block them.
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = smartAI_symbol
            if makepattern(copy, smartAI_symbol):
                return i
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = dumbAI_symbol
            if makepattern(copy, dumbAI_symbol):
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


def smart_AI(position, smartestAI_symbol, smartAI_symbol, dumbAI_symbol):
    # Selecting position for next move for its own
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = smartAI_symbol
            if makepattern(copy, smartAI_symbol):
                return i

    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            # makeMove(copy, smartestAI_symbol, i)
            copy[i] = smartestAI_symbol
            if makepattern(copy, smartestAI_symbol):
                return i
    m_centre = chooseRandomMoveFromList(position, [6, 7, 10, 11])
    if m_centre != None:
        return m_centre

    move = chooseRandomMoveFromList(position, [1, 4, 13, 16])
    if move != None:
        return move

    return chooseRandomMoveFromList(position, [2, 3, 5, 9, 8, 12, 14, 15])


def smartAI_play():
    move = smart_AI(theposition, smartestAI_symbol, smartAI_symbol, dumbAI_symbol)
    theposition[move] = smartAI_symbol
    if makepattern(theposition, smartAI_symbol):
        #creategrid(theposition)
        print('We are sorry but our smartAI has won the game!!')
        print('--------------------------------------------------------------')
        return 1
    else:
        if is_position_available(theposition):
            #creategrid(theposition)
            print('The game resulted in a tie.')
            print('--------------------------------------------------------------')
            return 2
        else:
            return 3


def dumb_AI(position, smartestAI_symbol, smartAI_symbol, dumbAI_symbol):
    # Check if other player could win on their next move, and block them.
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = smartAI_symbol
            if makepattern(copy, smartAI_symbol):
                return i
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = smartestAI_symbol
            if makepattern(copy, smartestAI_symbol):
                return i
    for i in range(1, 17):
        copy = newposition(position)
        if position_avail(copy, i):
            # makeMove(copy, smartestAI_symbol, i)
            if makepattern(copy, dumbAI_symbol):
                return i

    move = chooseRandomMoveFromList(position, [1, 4, 13, 16])
    if move != None:
        return move
    m_centre = chooseRandomMoveFromList(position, [6, 7, 10, 11])
    if m_centre != None:
        return m_centre
    return chooseRandomMoveFromList(position, [2, 3, 5, 9, 8, 12, 14, 15])


def dumbAI_play():
    move = dumb_AI(theposition, smartestAI_symbol, smartAI_symbol, dumbAI_symbol)
    theposition[move] = dumbAI_symbol
    if makepattern(theposition, dumbAI_symbol):
        #creategrid(theposition)
        print('We are sorry but our dumbAI has won the game!!')
        print('--------------------------------------------------------------')
        return 1
    else:
        if is_position_available(theposition):
            #creategrid(theposition)
            print('The game resulted in a tie.')
            print('--------------------------------------------------------------')
            return 2
        else:
            # turn1 = 'smartAI'
            return 3

def smartestAI_play():
    move = choose_smartestAI_turn(theposition, smartestAI_symbol, smartAI_symbol, dumbAI_symbol)
    theposition[move] = smartestAI_symbol
    if makepattern(theposition, smartestAI_symbol):
        #creategrid(theposition)
        print('We are sorry but our AI has won the game!!')
        print('--------------------------------------------------------------')
        return 1
    else:
        if is_position_available(theposition):
            #creategrid(theposition)
            print('The game resulted in a tie.')
            print('--------------------------------------------------------------')
            return 2
        else:
            # turn1 = 'smartAI'
            return 3

print('Welcome to a 4*4, a 3 Player Noughts and Crosses game.\n We have three AI in the game with some different strategy.\n To win the game, they have to place 3 X-s, O-s or 3 T-s in a row.')
print('--------------------------------------------------------------')
c1 = c2 = c3 = tie = 0
first_smartAI = first_dumbAI = first_smartestAI = 0
second_smartAI = second_dumbAI = second_smartestAI = 0
third_smartAI = third_dumbAI = third_smartestAI = 0
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
    if(turn1 == 'smartAI'):
        first_smartAI = first_smartAI+1
    elif(turn1== 'dumbAI'):
        first_dumbAI = first_dumbAI+1
    else:
        first_smartestAI= first_smartestAI+1

    if(turn2 == 'smartAI'):
        second_smartAI = second_smartAI+1
    elif(turn2== 'dumbAI'):
        second_dumbAI = second_dumbAI+1
    else:
        second_smartestAI= second_smartestAI+1

    if(turn3 == 'smartAI'):
        third_smartAI = third_smartAI+1
    elif(turn3== 'dumbAI'):
        third_dumbAI = third_dumbAI+1
    else:
        third_smartestAI= third_smartestAI+1

    print('Turn 1 is of: ', turn1,'Turn 2 is of:', turn2 ,'Turn 3 is of: ',turn3)
    playersymbol = select_sym_sequence()
    smartAI_symbol = playersymbol[0]
    dumbAI_symbol = playersymbol[1]
    smartestAI_symbol = playersymbol[2]
    print('The symbols for each player are: smartAI is:', smartAI_symbol, ',dumbAI is:', dumbAI_symbol, ',smartestAI is:',smartestAI_symbol)
    continue_playing = True
    while continue_playing:
        # if smartAI is first, dumbAI is second,  and smartestAI is third
        if turn1 == 'smartAI' and turn2 == 'dumbAI' and turn3 == 'smartestAI':
            check = smartAI_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn2 == "dumbAI"
            else:
                break
            check2 = dumbAI_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn3 == "smartestAI"
            else:
                break
            check3 = smartestAI_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "smartestAI"
            else:
                break
        #if smartAI will play first, smartestAI is second and dumbAI is third
        if turn1 == 'smartAI' and turn2 == 'smartestAI' and turn3 == 'dumbAI':
            check = smartAI_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn2 == "smartestAI"
            else:
                break
            check3 = smartestAI_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "dumbAI"
            else:
                break
            check2 = dumbAI_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn1 == "smartAI"
            else:
                break
        #if dumbAI will play first smartAI is second and smartestAI is third
        if turn1 == 'dumbAI' and turn2 == 'smartAI' and turn3 == 'smartestAI':
            check2 = dumbAI_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn2 == "smartAI"
            else:
                break
            check = smartAI_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn1 == "dumbAI"
            else:
                break
            check3 = smartestAI_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "dumbAI"
            else:
                break
        #if dumbAI will play first, smartestAI is second and smartAI is last
        if turn1 == 'dumbAI' and turn2 == 'smartestAI' and turn3 == 'smartAI':
            check2 = dumbAI_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn2 == "smartestAI"
            else:
                break
            check3 = smartestAI_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn3 == "smartAI"
            else:
                break
            check = smartAI_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn1 == "dumbAI"
            else:
                break
        #if smartestAI will play first, dumbAI is second and smartAI goes third
        if turn1 == 'smartestAI' and turn2 == 'dumbAI' and turn3 == 'smartAI':
            check3 = smartestAI_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn2 == "dumbAI"
            else:
                break
            check2 = dumbAI_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn3 == "smartAI"
            else:
                break
            check1 = smartAI_play()
            if check1 == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check1 == 3:
                turn1 == "smartestAI"
            else:
                break
        #if smartestAI will play first, smartAI is second and dumbAI third
        if turn1 == 'smartestAI' and turn2 == 'smartAI' and turn3 == 'dumbAI':
            check3 = smartestAI_play()
            if check3 == 1:
                c3 = c3 + 1
                continue_playing = False
                break
            elif check3 == 3:
                turn2 = "smartAI"
            else:
                break
            check = smartAI_play()
            if check == 1:
                c1 = c1 + 1
                continue_playing = False
                break
            elif check == 3:
                turn3 == "dumbAI"
            else:
                break
            check2 = dumbAI_play()
            if check2 == 1:
                c2 = c2 + 1
                continue_playing = False
                break
            elif check2 == 3:
                turn1 == "smartestAI"
            else:
                break
print('*************************************************')
print('Number of times smartAI goes first',first_smartAI)
print('Number of times dumbAI goes first',first_dumbAI)
print('Number of times smartestAI goes first',first_smartestAI)
print('*************************************************')
print('Number of times smartAI goes second',second_smartAI)
print('Number of times dumbAI goes second',second_dumbAI)
print('Number of times smartestAI goes second',second_smartestAI)
print('*************************************************')
print('Number of times smartAI goes third',third_smartAI)
print('Number of times dumbAI goes third',third_dumbAI)
print('Number of times smartestAI goes third',third_smartestAI)
print('*************************************************')

print('Percentage of winning for smartAI', (c1 / ask_user) * 100)
print('Percentage of winning for dumbAI', (c2 / ask_user) * 100)
print('Percentage of winning for smartestAI', (c3 / ask_user) * 100)
tie = (ask_user - (c1+c2+c3))
print('Percentage of tie is', (tie / ask_user) * 100)