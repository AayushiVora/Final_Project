import random


def creategrid(position):
    # We are creating the basic grid of the game by using this function.
    print(' ' + position[21] + ' | ' + position[22] + ' | ' + position[23] + ' | ' + position[24]+ ' | ' + position[25])
    print('--------------------')
    print(' ' + position[16] + ' | ' + position[17] + ' | ' + position[18] + ' | ' + position[19]+ ' | ' + position[20])
    print('--------------------')
    print(' ' + position[11] + ' | ' + position[12] + ' | ' + position[13] + ' | ' + position[14]+ ' | ' + position[15])
    print('--------------------')
    print(' ' + position[6] + ' | ' + position[7] + ' | ' + position[8] + ' | ' + position[9]+ ' | ' + position[10])
    print('--------------------')
    print(' ' + position[1] + ' | ' + position[2] + ' | ' + position[3] + ' | ' + position[4]+ ' | ' + position[5])


def makepattern(coordinate,character):

    """This function will check the winning possibilties
    :param coordinate: Grid for the game.
    :param character: The symbol for which it checks the winning condition i.e., O,X or T.
    :return: True if there's a winning combination for the symbol.
    >>> test_list = [' '] * 26
    >>> test_list[1] = test_list[2] = test_list[3] = 'X'
    >>> makepattern(test_list,'T')
    False
    >>> makepattern(test_list,'X')
    True
    >>> makepattern(test_list,'O')
    False
    """

    WIN = [[1, 2, 3],[2, 3, 4],[3, 4, 5],[6, 7, 8],[7, 8, 9],[8, 9, 10],[11, 12, 13],[12, 13, 14],[13, 14, 15],[16, 17, 18],[17, 18, 19],[18, 19, 20],
        [21, 22, 23],[22, 23, 24],[23, 24, 25],[1, 6, 11],[6, 11, 16],[11, 16, 21],[2, 7, 12],[7, 12, 17],[12, 17, 22],[3, 8, 13],[8, 13, 18],[13, 18, 23],
        [4, 9, 14],[9, 14, 19],[14, 19, 24],[5, 10, 15],[10, 15, 20],[15, 20, 25],[1, 7, 13],[7, 13, 19],[13, 19, 25],[2, 8, 14],[8, 14, 20],[3, 9, 15],
        [6, 12, 18],[12, 18, 24],[11, 17, 23],[3, 7, 11],[4, 8, 12],[8, 12, 16],[5, 9, 13],[9, 13, 17],[13, 17, 21],[10, 14, 18],[14, 18, 22],[15, 19, 23]]
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
    :param position: It is the game grid.
    :return: This returns duplicate list of the positions.
    """
    counter_pos = []
    for i in position:
        counter_pos.append(i)
    return counter_pos


def position_avail(position, move):

    """This function checks if the position is empty or no"""
    return position[move] == ' '


def chooseRandomMoveFromList(position, movesList):

    """This function randomly selects the move from the list
    :param position: It is the game grid
    :param movesList: It contains the list of positions in which a player can make a move.
    :return: It will return a random position from the move list.
    """

    possibleMoves = []
    for i in movesList:
        if position_avail(position, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def check_against_players(position,symbol):

    """This function checks if the opposite player is winning.
    :param position: It is the game grid
    :param symbol: It is the competitor player's symbol.
    :return: It will return the position for winning possibility of competitor.
    """

    for i in range(1, 26):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = symbol
            if makepattern(copy, symbol):
                return i

def check_own_winning(position,symbol):

    """This function checks checks the player's own winning possibility
    :param position: It is the game grid
    :param symbol: It is the player's symbol.
    :return: It will return if there's a winning possibility of itself.
    """

    for i in range(1, 26):
        copy = newposition(position)
        if position_avail(copy, i):
            copy[i] = symbol
            if makepattern(copy, symbol):
                return i

def choose_smartestAI_turn(position, smartestAI_symbol, smartAI_symbol, dumbAI_symbol):

    """This function is the smartest AI's strategy.
    :param position: It is the game grid
    :param smartestAI_symbol: It is the smartest AI's symbol.
    :param smartAI_symbol: It is the smart AI's symbol.
    :param dumbAI_symbol: It is the dumb AI's symbol.
    :return: It will return the next move for the smartest AI.
    """

    check_own_winning(position,smartestAI_symbol)
    check_against_players(position,smartAI_symbol)
    check_against_players(position,dumbAI_symbol)
    m_centre = chooseRandomMoveFromList(position, [7,8,9,12,13,14,17,18,19])
    if m_centre != None:
        return m_centre
    move = chooseRandomMoveFromList(position, [1,5,21,25])
    if move != None:
        return move
    return chooseRandomMoveFromList(position, [2, 3, 4,6,10,11,15,10,20,22,23,24])


def is_position_available(position):

    """This function checks weather all the coordinates in the grid are filled.
    :param position: It is the game grid.
    :return: It returns True if the grid is filled
    >>> test_list = [' '] * 26
    >>> test_list[1] = test_list[2] = test_list[3] = 'X'
    >>> is_position_available(test_list)
    False
    """
    for i in range(1, 26):
        if position_avail(position, i):
            return False
    return True


def smart_AI(position, smartestAI_symbol, smartAI_symbol):

    """This function is the smart AI's strategy.
    :param position: It is the game grid
    :param smartestAI_symbol: It is the smartest AI's symbol.
    :param smartAI_symbol: It is the smart AI's symbol.
    :return: It will return the next move for the smart AI.
    """

    check_own_winning(position,smartAI_symbol)
    check_against_players(position,smartestAI_symbol)
    m_centre = chooseRandomMoveFromList(position, [7,8,9,12,13,14,17,18,19])
    if m_centre != None:
        return m_centre

    move = chooseRandomMoveFromList(position, [1,5,21,25])
    if move != None:
        return move

    return chooseRandomMoveFromList(position, [2, 3, 4,6,10,11,15,10,20,22,23,24])


def smartAI_play():

    """This function determines the outcomes of the smart AI's moves.
    :return: 1 if smart AI is winning, 2 if There's a tie and 3 if there's none of these cases.
    """

    move = smart_AI(theposition, smartestAI_symbol, smartAI_symbol)
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

    """This function is the dumb AI's strategy.
   :param position: It is the game grid
   :param smartestAI_symbol: It is the smartest AI's symbol.
   :param smartAI_symbol: It is the smart AI's symbol.
   :param dumbAI_symbol: It is the dumb AI's symbol.
   :return: It will return the next move for the dumb AI.
   """

    check_against_players(position,smartestAI_symbol)
    check_against_players(position,smartAI_symbol)
    check_own_winning(position,dumbAI_symbol)
    move = chooseRandomMoveFromList(position, [1,5,21,25])
    if move != None:
        return move
    m_centre = chooseRandomMoveFromList(position, [7,8,9,12,13,14,17,18,19])
    if m_centre != None:
        return m_centre
    return chooseRandomMoveFromList(position, [2, 3, 4,6,10,11,15,10,20,22,23,24])


def dumbAI_play():

    """This function determines the outcomes of the dumb AI's moves.
    :return: 1 if dumb AI is winning, 2 if There's a tie and 3 if there's none of these cases.
    """

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

    """This function determines the outcomes of the smartest AI's moves.
    :return: 1 if smartest AI is winning, 2 if There's a tie and 3 if there's none of these cases.
    """

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

if __name__ == '__main__':

    print('Welcome to a 5*5, a 3 Player Noughts and Crosses game.\n We have three AI in the game with some different strategy.\n To win the game, they have to place 3 X-s, O-s or 3 T-s in a row.')
    print('--------------------------------------------------------------')
    c1 = c2 = c3 = tie = 0
    count_smartAI = count_dumbAI = count_smartestAI = 0
    first_smartAI = first_dumbAI = first_smartestAI = 0
    second_smartAI = second_dumbAI = second_smartestAI = 0
    third_smartAI = third_dumbAI = third_smartestAI = 0
    fourth_smartAI = fourth_dumbAI = fourth_smartestAI = 0
    fifth_smartAI = fifth_dumbAI = fifth_smartestAI = 0
    sixth_smartAI = sixth_dumbAI = sixth_smartestAI = 0
    ask_user = input("How many times do you want to simulate the game?")
    ask_user = int(ask_user)
    print('--------------------------------------------------------------')
    for i in range(0, ask_user):

        # Reset the position
        theposition = [' '] * 26
        turn = sequenceofplayers()
        turn1 = turn[0]
        turn2 = turn[1]
        turn3 = turn[2]
        if(turn1 == 'smartAI'):
            count_smartAI = count_smartAI+1
        elif(turn1== 'dumbAI'):
            count_dumbAI = count_dumbAI+1
        else:
            count_smartestAI= count_smartestAI+1
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
                    first_smartAI = first_smartAI+1
                    break
                elif check == 3:
                    turn2 == "dumbAI"
                else:
                    break
                check2 = dumbAI_play()
                if check2 == 1:
                    c2 = c2 + 1
                    continue_playing = False
                    first_dumbAI=first_dumbAI+1
                    break
                elif check2 == 3:
                    turn3 == "smartestAI"
                else:
                    break
                check3 = smartestAI_play()
                if check3 == 1:
                    c3 = c3 + 1
                    continue_playing = False
                    first_smartestAI=first_smartestAI+1
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
                    second_smartAI=second_smartAI+1
                    break
                elif check == 3:
                    turn2 == "smartestAI"
                else:
                    break
                check3 = smartestAI_play()
                if check3 == 1:
                    c3 = c3 + 1
                    continue_playing = False
                    second_smartestAI = second_smartestAI+1
                    break
                elif check3 == 3:
                    turn3 == "dumbAI"
                else:
                    break
                check2 = dumbAI_play()
                if check2 == 1:
                    c2 = c2 + 1
                    continue_playing = False
                    second_dumbAI=second_dumbAI+1
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
                    third_dumbAI=third_dumbAI+1
                    break
                elif check2 == 3:
                    turn2 == "smartAI"
                else:
                    break
                check = smartAI_play()
                if check == 1:
                    c1 = c1 + 1
                    continue_playing = False
                    third_smartAI=third_smartAI+1
                    break
                elif check == 3:
                    turn1 == "dumbAI"
                else:
                    break
                check3 = smartestAI_play()
                if check3 == 1:
                    c3 = c3 + 1
                    continue_playing = False
                    third_smartestAI=third_smartestAI+1
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
                    fourth_dumbAI=fourth_dumbAI+1
                    break
                elif check2 == 3:
                    turn2 == "smartestAI"
                else:
                    break
                check3 = smartestAI_play()
                if check3 == 1:
                    c3 = c3 + 1
                    continue_playing = False
                    fourth_smartestAI=fourth_smartestAI+1
                    break
                elif check3 == 3:
                    turn3 == "smartAI"
                else:
                    break
                check = smartAI_play()
                if check == 1:
                    c1 = c1 + 1
                    continue_playing = False
                    fourth_smartAI=fourth_smartAI+1
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
                    fifth_smartestAI=fifth_smartestAI+1
                    break
                elif check3 == 3:
                    turn2 == "dumbAI"
                else:
                    break
                check2 = dumbAI_play()
                if check2 == 1:
                    c2 = c2 + 1
                    continue_playing = False
                    fifth_dumbAI=fifth_dumbAI+1
                    break
                elif check2 == 3:
                    turn3 == "smartAI"
                else:
                    break
                check1 = smartAI_play()
                if check1 == 1:
                    c1 = c1 + 1
                    continue_playing = False
                    fifth_smartAI=fifth_smartAI+1
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
                    sixth_smartestAI=sixth_smartestAI+1
                    break
                elif check3 == 3:
                    turn2 = "smartAI"
                else:
                    break
                check = smartAI_play()
                if check == 1:
                    c1 = c1 + 1
                    continue_playing = False
                    sixth_smartAI=sixth_smartAI+1
                    break
                elif check == 3:
                    turn3 == "dumbAI"
                else:
                    break
                check2 = dumbAI_play()
                if check2 == 1:
                    c2 = c2 + 1
                    continue_playing = False
                    sixth_dumbAI=sixth_dumbAI+1
                    break
                elif check2 == 3:
                    turn1 == "smartestAI"
                else:
                    break
    print('*************************************************')
    print('Number of times smartAI goes first',count_smartAI)
    print('Number of times dumbAI goes first',count_dumbAI)
    print('Number of times smartestAI goes first',count_smartestAI)
    print('*************************************************')
    print('if smartAI is first, dumbAI is second,  and smartestAI is third')
    print('Number of times smartAI wins',first_smartAI)
    print('Number of times dumbAI wins',first_dumbAI)
    print('Number of times smartestAI wins',first_smartestAI)
    print('*************************************************')
    print('if smartAI will play first, smartestAI is second and dumbAI is third')
    print('Number of times smartAI wins',second_smartAI)
    print('Number of times dumbAI wins',second_dumbAI)
    print('Number of times smartestAI wins',second_smartestAI)
    print('*************************************************')
    print('if dumbAI will play first smartAI is second and smartestAI is third')
    print('Number of times smartAI wins',third_smartAI)
    print('Number of times dumbAI wins',third_dumbAI)
    print('Number of times smartestAI wins',third_smartestAI)
    print('*************************************************')
    print('if dumbAI will play first, smartestAI is second and smartAI is last')
    print('Number of times smartAI wins',fourth_smartAI)
    print('Number of times dumbAI wins',fourth_dumbAI)
    print('Number of times smartestAI wins',fourth_smartestAI)
    print('*************************************************')
    print('if smartestAI will play first, dumbAI is second and smartAI goes third')
    print('Number of times smartAI wins',fifth_smartAI)
    print('Number of times dumbAI wins',fifth_dumbAI)
    print('Number of times smartestAI wins',fifth_smartestAI)
    print('*************************************************')
    print('if smartestAI will play first, smartAI is second and dumbAI third')
    print('Number of times smartAI wins',sixth_smartAI)
    print('Number of times dumbAI wins',sixth_dumbAI)
    print('Number of times smartestAI wins',sixth_smartestAI)
    print('*************************************************')

    print('Percentage of winning for smartAI', (c1 / ask_user) * 100)
    print('Percentage of winning for dumbAI', (c2 / ask_user) * 100)
    print('Percentage of winning for smartestAI', (c3 / ask_user) * 100)
    tie = (ask_user - (c1+c2+c3))
    print('Percentage of tie is', (tie / ask_user) * 100)