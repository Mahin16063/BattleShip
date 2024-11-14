""" 
Project Details:
    Name: Mahin Hossain Akond
    Student #: 101256049
    Date Created: 30/10/24


External Libraries Used:
1. Random
********************************************************
"""
""" Pseudocode 
        Prompt user input for total rounds of the game
        Initialize the total game score
        for each round:
            Validate the user input for board size and number of ships
            Handle invalid entries 
            Set the board and ships.
            for each shot in the round:
                Request the user to input the assumed ship coordinates
                Display the Hit message (Hit or Miss)
                Display the full board with updated attempts results 
            Show the final state of the board
            Display the user final score of this round
        Display the user final score of the game
"""

""" Importing the libraries

"""
import random

""" Defining global variables

"""
totalScore = 0


def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
        Parameter(s): 
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None   
    """
    #creating the outer list
    rows = []
    for i in board:
        #creating the inner list
        columns = []
        for j in board:
             columns.append('~')
             #after appending the inner list with ~, the outer list is appended with the inner list
        rows.append(columns)
    replacement = 0
    #the ship will be randomly added in empty slots until the specified no. of ships are added
    while replacement < numShips:
        row = random.randint(0,len(board)-1)
        column = random.randint(0,len(board)-1)
        #This makes sure the ships are only placed in empty slots
        if board[row][column] == '~':
            board[row][column] = 'S'
            replacement += 1
    return

def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s): 
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    #since it is basically a rectangle grid, the possible number of slots will be the square of the length or width
    possibleSlots = size*size
    #making sure at least 1 ship is added to the board 
    if numShips > 0:
        #number of ships must be less than the total slots possible, not even equal
        if numShips > possibleSlots:
            return True
        else:  
            return False
    else:
        return True

def checkFireError(board, row, col):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return [Boolean]: Return True if an error is found or False if there is no error.   
    """
    #adjusting coordinates for 0-based indexing
    row -= 1
    col -= 1
    #checking if shot is out of bounds of the board
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return True
    #check if user shoots at the same coordinate again. X or O means that has been shot, hence returning error
    if board[row][col] == 'X' or board[row][col] == 'O':
        return True

    return False

def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists  
    """
    #creating outer list that will hold the list of ~
    row = []
    #iterates through the outer list
    for i in range(size):
        #create the empty inner list
        column = []
        #iterates through the inner list
        for j in range(size):
            #append the inner list with ~
            column.append('~')
        #then, append the outer list with the inner list, so a list containing lists of ~
        row.append(column)
    return row

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.
        
        Return: None  
    """
    #looping through the board
    for row in board:
        #looping through the cells or coordinates in the row
        for cell in row:
            if not round:
                # Display the cell as-is if revealing the board at the end of the round
                print(cell, end=' ')
            else:
                # Hide ships by replacing 'S' with '~' during active gameplay
                print('~' if cell == 'S' else cell, end=' ')
        #proceed to the next row or line of the board
        print()  
   
    

def fireShot(board, row, col):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.     
    """  
    #if the fired coordinate contains S, this will mark as a hit and it will be replaced with X to
    #indicate the ship is hit
    if board[row-1][col-1] == 'S':
        board[row-1][col-1] = 'X'  # Mark hit
        return True
    #if the fired coordinate contains ~, this will mark as a miss and it will be replaced with O to
    #indicate there are no ships in the coordinate and to mark that slot is hit
    elif board[row-1][col-1] == '~':  
        board[row-1][col-1] = 'O'  # Mark miss
        return False
    
    

def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round 
            
            Pseudocode:
            Keep track of number of shots for the round
            Keep track of the score (number of hits) for the round
            Loop until user fires all their shots
                Ask user to enter coordinates for their shot.  Input two numbers separated by a space.
                Validate the shot coordinates using checkFireError function
                Fire a shot using the fireShot function
                Output if the shot is a hit or a miss
                display the board after the shot has been taken displayBoard(board)
            Output "End of round X"
            display the board at the end of the round displayBoard(board, False)
    
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.   
    """
    #setting the initial value of the variables
    shots_fired = 0
    hits = 0
    #player has same number of shots as ships
    max_shots = numShips 
    shotNumber = 0
    #print the rules
    print(f"\nRULES:\n1. You will get a total of {max_shots} shots for each round!\n2. You cannot hit the same coordinate more than once!\n")
    #user will be able to fire shots until the specified number of shots allowed is met
    while shots_fired < max_shots:
        #Input shot coordinates
        user_input = input("Enter row and column to take a shot (e.g., 2 3): ")
        
        #Split input and validate coordinates
        try:
            row, col = map(int, user_input.split())
            if checkFireError(board, row, col) == True:
                print("Invalid coordinates. Please try again.")
                continue
        except ValueError:
            print("Please enter two numbers separated by a space.")
            continue

        #Fire the shot
        result = fireShot(board, row, col)
        #this keeps count of the shot number in each attempt in a round
        shotNumber += 1
        if result == True:
            print(f"Shot {shotNumber} is a hit!")
            hits += 1
        else:
            print(f"Shot {shotNumber} is a miss!")

        shots_fired += 1
        
        #Display the board after each shot
        displayBoard(board)
    
    #End of round message and display the full board
    print(f"\nEnd of round with {shots_fired} shots taken and {hits} hits.\n")
    #For visuals, the final message before board displayed is in bold format
    print("\033[1m**Final board**\033[0m")
    displayBoard(board,round=False)
    
    
    return hits
    
#the main function is left untouched

def main():    
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None  
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return

if __name__ == '__main__':
    main()
