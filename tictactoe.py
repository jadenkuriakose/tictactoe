aboard = [' ' for x in range(10)]#initializes a board with 10 spaces 

def insertLetterArray(letter, pos):
    aboard[pos] = letter#gives a part of the board array a letter by assigning that letter to a position 

def spaceIsFreeArray(pos):
    return aboard[pos] == ' '#returns true if space in the array is free
    
dboard = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}#initializes a board with 9 spaces 

key_remover = []

def insertLetterDict(letter, pos):
    dboard[pos] = letter#gives a part of the board dictionary a letter by assigning that letter to a position 

def spaceIsFreeDict(pos):
    return dboard[pos] == ' '#returns true if space in the dictionary is free

def printBoard(board):
    #prints out our board using the dcitionary's assigned numbers
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def isWinner(b, l): #checks to see if someone has won yet
    return (b[7] == l and b[8] == l and b[9] == l) or (b[4] == l and b[5] == l and b[6] == l) or(b[1] == l and b[2] == l and b[3] == l) or(b[1] == l and b[4] == l and b[7] == l) or(b[2] == l and b[5] == l and b[8] == l) or(b[3] == l and b[6] == l and b[9] == l) or(b[1] == l and b[5] == l and b[9] == l) or(b[3] == l and b[5] == l and b[7] == l)

def playerMoveArray():#allows player to make a move and ensures move is within the parameters of the array (a valid integer between 1 and 9) before assigning a move to the array
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFreeArray(move):
                    run = False
                    insertLetterArray('X', move)
                else:
                    print('Sorry this space has been taken!')
            else:
                print('Invalid number! Please type a number between 1-9')
        except:
            print('Please type a number!')
            
def playerMoveDict():#allows player to make a move and ensures move is within the parameters of the array (a valid integer between 1 and 9) before assigning a move to the array
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFreeDict(move):
                    run = False
                    insertLetterDict('X', move)
                else:
                    print('Sorry this space has been taken!')
            else:
                print('Invalid number! Please type a number between 1-9')
        except:
            print('Please type a number!')
            
def player2Move():#allows player to make a move and ensures move is within the parameters of the array (a valid integer between 1 and 9) before assigning a move to the array
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFreeArray(move):
                    run = False
                    insertLetterArray('O', move)
                else:
                    print('Sorry this space has been taken!')
            else:
                print('Invalid number! Please type a number between 1-9')
        except:
            print('Please type a number!')           

def compMoveEasy():#allows computer to make moves starting with corners, then the middle, then edges as this is an optimal algorithm 
    possibleMoves = [x for x, letter in enumerate(aboard) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = aboard[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def checkDraw(board):
    return isDictBoardFull(board) 

def selectRandom(spaces):#selects a random position from the set of positions the algorithm prefers
    import random
    val = len(spaces)
    randSpot = random.randrange(0,val)
    return spaces[randSpot]
    

def isArrayBoardFull(board):#checks to see if board is full
    if board.count(' ') > 1: return False
    else: return True   
    
def compHardMove():
  bestScore = -1000
  bestMove = 0
  for key in list(dboard):
     if dboard[key] == ' ':
        dboard[key] = 'O'
        score = minimax(dboard,False)
        dboard[key] = ' '
        if(score> bestScore):
            bestScore = score
            bestMove = key
  insertLetterDict('O',bestMove)
 
def minimax(board,isMaximizing):
    score = 0
    bestScore = -800
    if isWinner(board,'O'):
        return 1
    elif isWinner(board,'X'):
        return -1
    elif checkDraw(board):
        return 0
    
    if isMaximizing:
     for key in list(board):
             if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board,False)
                board[key] = ' '
                if(score> bestScore):
                  bestScore = score
                 
     return bestScore
    else:
        bestScore = 800
        score = 0
        for key in list(board):
         if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board,True)
                board[key] = ' '
                if score <bestScore:
                    bestScore = score
        return bestScore
 
def isDictBoardFull(board):#checks to see if board is full
    for key in list(board):
     if board[key] == ' ': 
         return False
    return True   

def easyGame():
    print('Can you beat the bot')
    printBoard(aboard)

    while not(isArrayBoardFull(aboard)):
        if not(isWinner(aboard, 'O')):
            playerMoveArray()
            printBoard(aboard)
        else:
            print('You LOSE!')
            break

        if not(isWinner(aboard, 'X')):
            move = compMoveEasy()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetterArray('O', move)
                print('Computer made a move. Think carefully and respond!')
                printBoard(aboard)
        else:
            print('You won! Congratulations')
            break

    if isArrayBoardFull(aboard):
        print('Tie Game!')

def toughGame():
     print('Can you beat the bot')
     printBoard(dboard)
     while not(isDictBoardFull(dboard)):
         if not(isWinner(dboard, 'O')):
            playerMoveDict()
            printBoard(dboard)
         else:
            print('You LOSE!')
            break

         if not(isWinner(dboard, 'X')):
            move = compHardMove()
            if checkDraw(dboard):
                print('Tie Game!')
                break
            else:
                print('Computer made a move. Think carefully and respond!')
                printBoard(dboard)
         else:
            print('You won! Congratulations')
            break

         if checkDraw(dboard): 
           print('Tie Game ')
           
def playersGame():#alternates turns and determines winner
    print('Can you beat the bot')
    printBoard(aboard)

    while not(isArrayBoardFull(aboard)):
        if not(isWinner(aboard, 'O') or isArrayBoardFull(aboard)):
            playerMoveArray()
            print('player 1 made a move. Think carefully and respond!')
            printBoard(aboard)
        else:
            print('player 2 won!')
            break

        if not(isWinner(aboard, 'X') or isArrayBoardFull(aboard)):
                player2Move()
                print('player 2 made a move. Think carefully and respond!')
                printBoard(aboard)
        else:
            print('player 1 won')
            break

    if isArrayBoardFull(aboard):
        print('Tie Game!')


while True:

    answer = input('Do you want to play again? (Y/N) ')
    if answer.lower() == 'y' or answer.lower == 'yes':
        answer2 = input('type 1 for hard mode, type 2 for easy mode, type 3 for player v player ')
        try:
           answer2 = int(answer2)
           if answer2 < 4 and answer2 > 0:
                 if answer2 == 1:
                     dboard = {1: ' ', 2: ' ', 3: ' ',
                               4: ' ', 5: ' ', 6: ' ',
                               7: ' ', 8: ' ', 9: ' '}
                     toughGame()
                 if answer2 == 2:
                     aboard = [' ' for x in range(10)]
                     easyGame()
                 if answer2 == 3:
                     aboard = [' ' for x in range(10)]
                     playersGame()
           else:
                print('type a number between 1 and 3')
        except:
           print('type a valid number')
        
    else:
        break

