# I want to know the last cell clicked Line 131

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
             
        remove = []
        for k in range(0,len(nextCells)):
            cell = nextCells[k]
            if board[cell[0]][cell[1]] == -1 :
                remove.append(cell)
            if board[cell[0]][cell[1]] == 1 or board[cell[0]][cell[1]] == 2 :
                if edible(cell) == False:
                    remove.append(cell)         
        for j in remove:
            nextCells.remove(j)
        for i in nextCells:
            board[i[0]][i[1]] = 3
    return nextCells
    
def edible(cell):
    x, y, direction = cell[0], cell[1], cell[2]
    if direction == 'botRight' and board[x+1][y-1] == 0:
        return True
    elif direction == 'topRight' and board[x+1][y+1] == 0:
        return True
    elif direction == 'topLeft' and board[x-1][y+1] == 0:
        return True
    elif direction == 'botLeft' and board[x-1][y-1] == 0:
        return True
    else:
        return False
              
    
def findCell(x, y):
    return x//60, y//60
        
def move(player, oldCell, newCell):
    player[player.index(oldCell)] = newCell
    print(player)   
    

def drawPlayer(player1, player2):
    for k in player1:
        i,j = k[0], k[1]
        area.create_oval(i*60+5, j*60+5, i*60+55, j*60+55, fill='white')
    for f in player2:
        i ,j = f[0], f[1]
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



def register_mouse_click(event, board):
    print("The click was made on the position:", event.x, event.y)
    print("cell coordinate", findCell(event.x, event.y))
    xCell, yCell = findCell(event.x, event.y)
    #print("next cells", findPossibleMove(board, xCell, yCell))
    nextCells=[]
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                nextCells.append((i,j))
                
    if nextCells == []:
        drawPossibleMove(findPossibleMove(board, xCell, yCell), board, player1, player2)
    else:
        print('next cells are', nextCells)
        ######## Here I want to access the last cell clicked ##########
        '''
        if (xCell, yCell) in nextCells:
            #moveMouseClick(event, player1, oldCell)
            drawBoard(board)
            drawPlayer(player1, player2)
            
        '''

    
    
def moveMouseClick(event, player, oldCell):
    xCell, yCell = findCell(event.x, event.y)
    move(player, oldCell, (xCell, yCell))
    
    

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
area.bind('<1>',lambda event: register_mouse_click(event, board))


window.mainloop()
