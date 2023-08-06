#using modules to generate random sudoku boards

from dokusan import generators
import numpy as np
import copy

#Board class with an init method used for initializing the sudoku grid

class Board():
    def __init__(self,board):
        self.board=board

    #Gridboard method that prints out the sudoku grid on the screen

    def gridboard(self,board):
        for i in range(len(board)):
            if i%3==0 and i!=0:
                print("-----------------------")
            for j in range(len(board)):
                if j%3==0 and j!=0:
                    print(" | ",end="")
                print(board[i][j],end=" ")
            print()

    #validity function to check whether a number entered in a board is valid or not

    def valid(board,val,pos):

        #loop to check for any repeating numbers in a particular row

        for i in range(len(board)):
            if board[pos[0]][i]==val and pos[1]!=i:
                return False
            
        #loop to check for any repeating numbers in a particular column

        for j in range(len(board)):
            if board[j][pos[1]]==val and pos[0]!=j:
                return False
            
        #A way to check for any repeating numbers in a particular "square"

        x_grid=pos[1]//3
        y_grid=pos[0]//3
        for i in range(y_grid*3,y_grid*3+3):
            for j in range(x_grid*3,x_grid*3+3):
                if board[i][j]==val and (i,j)!=pos:
                    return False

        return True

    #position function to return the position of a place where 0, or any space is available

    def position(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==0:
                    pos=(i,j)
                    return pos
        return False
    
    #Method to place a number of user's choice in a particular box or space
    
    def placeNumber(self,board,number,posX,posY):
        global isFull
        isFull=True
        
        if(self.isBoardFull(board)==False):
            board[posX][posY]=number
            self.gridboard(board)
            isFull=False

        elif isFull==False:
            self.checkBoard(board)


    #A method that returns true if there are no more empty spaces in the board and vice versa

    def isBoardFull(self,board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]==0:
                    return False
                
        return True
    
    #This method returns true if the board has been solved correctly by comparing it to the solution board that was solved earlier by the CPU.
    
    def checkBoard(self,board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!=solutionBoard[i][j]:

                    print("SORRY, THIS SUDOKU BOARD HAS NOT BEEN SOLVED CORRECTLY!\n")

                    return False
                    
                    
        return True
                    
#Solve class that contains important methods to solve the puzzle. Uses inheritance to access some methods from the board class.                     

class Solve(Board):

    #solve function to solve the board recursively

    def __init__(self,board):
        self.board=board
        global solutionBoard
        solutionBoard=copy.deepcopy(board)
        
        self.solve(solutionBoard)
        
        if(playerChoice=='1'):
            print("HERE'S THE BOARD YOU NEED TO SOLVE\n")
            self.gridboard(board)
            self.humanSolve(board)

        elif(playerChoice=='2'):
            self.gridboard(solutionBoard)

    #A method that allows the user to place a number in a particular box or space

    def humanSolve(self,board):
        
        userNumber=input("WHAT NUMBER DO YOU WANT TO PLACE?\n")
        if(userNumber not in ('0','1','2','3','4','5','6','7','8','9')):
            print("PLEASE ENTER A VALID NUMBER\n")
            self.humanSolve(board)

        else:
            userNumber=int(userNumber)

        positionX=input("WHICH POSITION (FOR X) DO YOU WANT TO ENTER A NUMBER (0-8)\n")
        positionY=input("WHICH POSITION (FOR Y) DO YOU WANT TO ENTER A NUMBER (0-8)\n")
        if((positionX not in ('0','1','2','3','4','5','6','7','8')) or (positionY not in ('0','1','2','3','4','5','6','7','8'))):
            print("PLEASE ENTER VALID POSITIONS FOR BOTH ARGUMENTS\n")
            self.humanSolve(board)

        else:
            positionX=int(positionX)
            positionY=int(positionY)
            self.placeNumber(board,userNumber,positionX,positionY)

            if(isFull==True):
                solutionChoice=str(input("DO YOU WANT TO VIEW THE SOLUTION? (Y FOR YES, ANY KEY FOR NO)\n"))

                if(solutionChoice.lower()=="y"):
                    self.gridboard(solutionBoard)

                elif(solutionChoice.lower()!="y"):
                    print("GOODBYE!")
                    return
            else:
                self.humanSolve(board)
        

    #Main solve method that the CPU uses to solve the board recursively

    def solve(self,board):
        empty=Board.position(board)
        if not empty:
            return True
        
        else:
            placex=empty[0]
            placey=empty[1]
        
        for i in range(1,10):
            if Board.valid(board,i,(placex,placey)):
                board[placex][placey]=i
                if self.solve(board):
                    return True
                board[placex][placey]=0

        return False
                

#some random commands to print the board out before and after the solve state

def startGame():
    print("WELCOME TO SUDOKU!\n")
    global playerChoice
    playerChoice=input("DO YOU WANT TO PLAY FOR YOURSELF (1), OR SEE THE COMPUTER SOLVE ONE? (2)\n")

    if(playerChoice=='1'):
        arr=np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9,9)
        final=arr.astype(np.intc)
        boardInstance=Board(final)
        solveInstance=Solve(final)

    elif(playerChoice=='2'):
        arr=np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9,9)
        final=arr.astype(np.intc)
        print("UNSOLVED BOARD\n")       
        boardInstance=Board(final)
        boardInstance.gridboard(final)
        print()
        print("SOLVED BOARD\n")
        solveInstance=Solve(final)

    else:
        print("PLEASE ENTER A VALID CHOICE\n")
        startGame()

#start the game

startGame()


