#using modules to generate random sudoku boards

from dokusan import generators
import numpy as np
arr=np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9,9)
final=arr.astype(np.int)

#making the sudoku grid

board=final
def gridboard(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -")
        for j in range(len(board)):
            if j%3==0 and j!=0:
                print(" | ",end="")
            print(board[i][j],end=" ")
        print()

#solve function to solve the board recursively

def solve(board):
    empty=position(board)
    if not empty:
        return True
    else:
        placex=empty[0]
        placey=empty[1]
    
    
    for i in range(1,10):
        if valid(board,i,(placex,placey)):
            board[placex][placey]=i
            if solve(board):
                return True
            board[placex][placey]=0

    return False
                



#validity function to check whether a number entered in a board is valid or not

def valid(board,val,pos):
    #check row

    for i in range(len(board)):
        if board[pos[0]][i]==val and pos[1]!=i:
            return False
    #check column

    for j in range(len(board)):
        if board[j][pos[1]]==val and pos[0]!=j:
            return False
    #check subgrid

    x_grid=pos[1]//3
    y_grid=pos[0]//3
    for i in range(y_grid*3,y_grid*3+3):
        for j in range(x_grid*3,x_grid*3+3):
            if board[i][j]==val and (i,j)!=pos:
                return False
    
    return True


#position function to return the position of a place where 0 is available

def position(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                pos=(i,j)
                return pos
    return False

#some random commands to print the board out before and after the solve state

print("UNSOLVED BOARD\n")        
gridboard(board)
print()
print("SOLVED BOARD\n")
solve(board)
gridboard(board)
