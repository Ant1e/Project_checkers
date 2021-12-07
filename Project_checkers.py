
import tkinter as tk
from tkinter import messagebox


def boardGame():
    board = []
    for i in range(0,10):
        board.append([])
        for j in range(0,10):
            board[i].append(0)
            if i%2 == 0 and j%2 == 0:
                board[i][j]=-1
            elif i%2 != 0 and j%2 != 0:
                board[i][j]=-1
    return board

def playerGenerator(board):
    player1 = []
    player2 = []
    for i in range(0,10):
        for j in range(0,10):
            if j in range(0,4):
                if i%2 == 0 and j%2 != 0:
                    player1.append((i,j))
                    board[i][j] = 1 
                elif i%2 != 0 and j%2 == 0:
                    player1.append((i,j))
                    board[i][j] = 1
            elif j in range(6,10):
                if i%2 == 0 and j%2 != 0:
                    player2.append((i,j))  
                    board[i][j] = 2
                elif i%2 != 0 and j%2 == 0:
                    player2.append((i,j))
                    board[i][j] = 2
    player2.append((0,0))
    return player1, player2


def findPossibleMove(board, x, y):
    nextCells = []
    
    if board[x][y] == 1 or board[x][y]==2:
        nextCells = [(x+1,y-1, 'topRight'), (x+1,y+1, 'botRight'), (x-1, y+1, 'botLeft'), (x-1, y-1, 'topLeft')]
        remove=[]
        for i in range(0,4):
            if nextCells[i][0] > 9 or nextCells[i][1] > 9 or nextCells[i][0] < 0 or nextCells[i][1] < 0:
                remove.append(nextCells[i])
        for j in remove:
            nextCells.remove(j)
        
        edibleList=[]
        remove = []
        for k in range(0,len(nextCells)):
            cell = nextCells[k]
            if board[cell[0]][cell[1]] == -1 :
                remove.append(cell)
            elif board[cell[0]][cell[1]] == 1 or board[cell[0]][cell[1]] == 2 :
                if edible(cell) == False or board[x][y] == board[cell[0]][cell[1]] :
                    remove.append(cell)   
                else:
                    nextCells.append(edible(cell))
                    edibleList.append(cell)
                    remove.append(cell)          
        for j in remove:
            nextCells.remove(j)
            
        remove =[]
        for i in range(0,len(nextCells)):
            cell = nextCells[i]
            if board[x][y] == 1 and cell[1]==y-1:
                remove.append(cell)
            elif board[x][y] == 2 and cell[1]==y+1:
                remove.append(cell)
        for j in remove:
            nextCells.remove(j)
        
        for i in nextCells:
            board[i[0]][i[1]] = [board[i[0]][i[1]], 3]
    
    return nextCells


def removePossibleCells(board, nextCells):
    for i in nextCells:
        board[i[0]][i[1]] = board[i[0]][i[1]][0]
    
    
def edible(cell):
    x, y, direction = cell[0], cell[1], cell[2]
    if x+1 <= 9 and y+1 <= 9 and x-1 >= 0 and y-1 >= 0:
        if direction == 'botRight' and board[x+1][y+1] == 0 :
            return x+1,y+1
        elif direction == 'topRight' and board[x+1][y-1] == 0:
            return x+1,y-1
        elif direction == 'topLeft' and board[x-1][y-1] == 0:
            return x-1,y-1
        elif direction == 'botLeft' and board[x-1][y+1] == 0:
            return x-1,y+1
        else:
            return False
    else:
        return False
              
    
def findCell(x, y):
    return x//60, y//60
        
def move(board, player, oldCell, newCell):
    player[player.index(oldCell)] = newCell
    board[oldCell[0]][oldCell[1]] = 0
    vecteur = [[newCell[0]-oldCell[0]],[newCell[1]-oldCell[1]]]
    if player== player1:
        if vecteur == [[-2],[2]]:
            player2.remove((newCell[0]+1,newCell[1]-1))
            board[newCell[0]+1][newCell[1]-1] = 0
            board[newCell[0]][newCell[1]] = 1
            player2.append((0,0))
            player1.remove((0,0))
        elif vecteur == [[2],[-2]]:
            player2.remove((newCell[0]-1,newCell[1]+1))
            board[newCell[0]-1][newCell[1]+1] = 0
            board[newCell[0]][newCell[1]] = 1
            player2.append((0,0))
            player1.remove((0,0))
        elif vecteur == [[2],[2]]:
            player2.remove((newCell[0]-1,newCell[1]-1))
            board[newCell[0]-1][newCell[1]-1] = 0
            board[newCell[0]][newCell[1]] = 1
            player2.append((0,0))
            player1.remove((0,0))
        elif vecteur == [[-2],[-2]]:
            player2.remove((newCell[0]+1,newCell[1]+1))
            board[newCell[0]+1][newCell[1]+1] = 0
            board[newCell[0]][newCell[1]] = 1
            player2.append((0,0))
            player1.remove((0,0))
        else:
            board[newCell[0]][newCell[1]] = 1
            player2.append((0,0))
            player1.remove((0,0))
    elif player== player2:
        if vecteur == [[-2],[2]]:
            player1.remove((newCell[0]+1,newCell[1]-1))
            board[newCell[0]+1][newCell[1]-1] = 0
            board[newCell[0]][newCell[1]] = 2
            player1.append((0,0))
            player2.remove((0,0))
        elif vecteur == [[2],[-2]]:
            player1.remove((newCell[0]-1,newCell[1]+1))
            board[newCell[0]-1][newCell[1]+1] = 0
            board[newCell[0]][newCell[1]] = 2
            player1.append((0,0))
            player2.remove((0,0))
        elif vecteur == [[2],[2]]:
            player1.remove((newCell[0]-1,newCell[1]-1))
            board[newCell[0]-1][newCell[1]-1] = 0
            board[newCell[0]][newCell[1]] = 2
            player1.append((0,0))
            player2.remove((0,0))
        elif vecteur == [[-2],[-2]]:
            player1.remove((newCell[0]+1,newCell[1]+1))
            board[newCell[0]+1][newCell[1]+1] = 0
            board[newCell[0]][newCell[1]] = 2
            player1.append((0,0))
            player2.remove((0,0))
        else:
            board[newCell[0]][newCell[1]] = 2
            player1.append((0,0))
            player2.remove((0,0))
        
    
    
def markCell(board, x, y):
    previousValue = board[x][y]
    board[x][y] = [previousValue, 4]


def drawPlayer(player1, player2):
    for k in player1:
        i,j = k[0], k[1]
        if (i,j) != (0,0):
            area.create_oval(i*60+5, j*60+5, i*60+55, j*60+55, fill='white')
    for f in player2:
        i ,j = f[0], f[1]
        if (i,j) != (0,0):
            area.create_oval(i*60+5, j*60+5, i*60+55, j*60+55, fill='blue')

def drawBoard(board):
    for i in range(0,10):
        for j in range(0,10):
            if i%2 == 0 and j%2 == 0:
                area.create_rectangle(i*60,j*60, i*60+60,j*60+60, fill = 'white')
            elif i%2 != 0 and j%2 != 0:
                area.create_rectangle(i*60,j*60, i*60+60,j*60+60, fill = 'white')
            elif i%2 == 0 and j%2 != 0:
                area.create_rectangle(i*60,j*60, i*60+60,j*60+60, fill = 'black')  
            elif i%2 != 0 and j%2 == 0:
                area.create_rectangle(i*60,j*60, i*60+60,j*60+60, fill = 'black')  
                

def drawPossibleMove(possibleMove, board, player1, player2):
    drawBoard(board)
    drawPlayer(player1, player2)
    for i in possibleMove:
        area.create_rectangle(i[0]*60,i[1]*60, i[0]*60+60,i[1]*60+60, fill = 'red')



    
def register_mouse_click(event, board, player1, player2):
    
    
    print("The click was made on the position:", event.x, event.y)
    print("cell coordinate", findCell(event.x, event.y))
    xCell, yCell = findCell(event.x, event.y)
    nextCells=[]
    
    
    
    for i in range(10):
        for j in range(10):
            try:
                if board[i][j][1] == 3:
                    nextCells.append((i,j))
            except:
                None
      
       
    
    if nextCells == []:
        
        if (0,0) in player1 and board[xCell][yCell] == 1:
            print('will draw', nextCells)
            drawPossibleMove(findPossibleMove(board, xCell, yCell), board, player1, player2)
            markCell(board, xCell, yCell)
        elif (0,0) in player2 and board[xCell][yCell] == 2:
            print('will draw', nextCells)
            drawPossibleMove(findPossibleMove(board, xCell, yCell), board, player1, player2)
            markCell(board, xCell, yCell)
        
    else:
        removePossibleCells(board, nextCells)
        print('next cells are', nextCells)
        currentCell = -2
        
        for i in range(10):
            for j in range(10):
                try:
                    if board[i][j][1] == 4:
                        currentCell = (i, j)
                        player = board[i][j][0]
                        board[i][j] = 0
                except:
                    None
                    
         
        
        if (xCell, yCell) in nextCells and currentCell != -2:
            print('player', board[currentCell[0]][currentCell[1]])
            if (xCell, yCell) is not player1 and player==1:
                move(board, player1, currentCell, (xCell, yCell))
                drawBoard(board)
                drawPlayer(player1, player2)
                
            if (xCell, yCell) is not player2 and player==2:
                move(board, player2, currentCell, (xCell, yCell))
                drawBoard(board)
                drawPlayer(player1, player2)
            
            
        
 

   
    
    
    

board = boardGame()
player1, player2 = playerGenerator(board)



window = tk.Tk()
window.title("Checkers")
area = tk.Canvas(window, width=600, height=600, background="black")
area.grid()

winner = False

drawBoard(board)
drawPlayer(player1, player2)
print(board)
print(player1)
area.pack(fill="both", expand=True)
area.bind('<1>',lambda event: register_mouse_click(event, board, player1, player2))


window.mainloop()
