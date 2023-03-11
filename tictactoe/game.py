import random #for ai

print("Welcome to Tic Tac Toe!")
print("-----------------------")

# make user select character x or o

def characterSelection():
    userLetter = ''
    cpuLetter = ''
    
    while True:
        userLetter = input('Please choose your letter! x or o: ')
        if userLetter.lower() == 'x':
            cpuLetter = 'o'
            print(f'You are {userLetter.lower()} and Computer is {cpuLetter}')
            break
        elif userLetter.lower() == 'o':
            cpuLetter = 'x'
            print(f'You are {userLetter.lower()} and Computer is {cpuLetter}')
            break
        else:
            print("Invalid Input! Please Try Again!")
    return (userLetter, cpuLetter)
# characterSelection()
                         
possibleNumbers = [1,2,3,4,5,6,7,8,9]
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def drawboard():
    for x in range (3):
        print("\n+---+---+---+")
        print("|", end = "")
        for y in range (3):
            print ("", board[x][y], end = " |")
    print("\n+---+---+---+")


#array modify
# board[(num - 1) // 3][(num - 1) % 3] = turn

#Check Win
def winCon(board, player):
    # X axis
    return ((board[0][0] == board[0][1] == board[0][2] == player) or
            (board[1][0] == board[1][1] == board[1][2] == player) or
            (board[2][0] == board[2][1] == board[2][2] == player) or
            (board[0][0] == board[1][0] == board[2][0] == player) or
            (board[0][1] == board[1][1] == board[2][1] == player) or
            (board[0][2] == board[1][2] == board[2][2] == player) or
            (board[0][0] == board[1][1] == board[2][2] == player) or
            (board[0][2] == board[1][1] == board[2][0] == player))

turnCounter = 0
userLetter, cpuLetter = characterSelection()
#main game
while True:
    #check if ended in tie
    if winCon(board, userLetter):
        print("You have won!")
        break
    elif winCon(board, cpuLetter):
        print("Computer has won")
        break
    elif len(possibleNumbers) == 0:
        print("Tie!")
        break
    # chech if someone has won
    else:
        #keep playing
        drawboard()
        #user's turn
        if (turnCounter % 2 == 0):
            numPicked = int(input("\nChoose from [1-9]: "))
            if numPicked in possibleNumbers:
                board[(numPicked - 1) // 3][(numPicked - 1) % 3] = userLetter
                possibleNumbers.remove(numPicked)
                turnCounter += 1
            else:
                print ("Invalid Input! Please Try Again!")
        # cpu turn
        elif (turnCounter % 2 == 1):
            while True:
                cpuChoice = random.choice(possibleNumbers)
                print(f'Cpu has chosen {cpuChoice}!')
                if (cpuChoice in possibleNumbers): 
                    board[(cpuChoice - 1) // 3][(cpuChoice - 1) % 3] = cpuLetter
                    possibleNumbers.remove(cpuChoice)
                    turnCounter += 1
                    break