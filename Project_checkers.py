import tkinter as tk
from tkinter import messagebox
from time import sleep


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
        try:
            board[i[0]][i[1]] = board[i[0]][i[1]][0]
        except:
            None
    
    
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


def checkWinner(player1, player2):
    
    if len(player1) == 0 or player1 == [(0,0)]:
        return 2
    elif len(player1) == 0 or player1 == [(0,0)]:
        return 1
    else:
        return False
    
def markCell(board, x, y):
    previousValue = board[x][y]
    board[x][y] = [previousValue, 4]
    

    
def mouse_click(event, board, player1, player2):
    global turn
    
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
        if (0,0) in player1 and board[xCell][yCell] == 1 :
            drawPossibleMove(findPossibleMove(board, xCell, yCell), board, player1, player2)
            markCell(board, xCell, yCell)
        elif (0,0) in player2 and board[xCell][yCell] == 2:
            drawPossibleMove(findPossibleMove(board, xCell, yCell), board, player1, player2)
            markCell(board, xCell, yCell)
        
    else:
        removePossibleCells(board, nextCells)
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
            if (xCell, yCell) is not player1 and player==1:
                move(board, player1, currentCell, (xCell, yCell))
                drawBoard(board)
                drawPlayer(player1, player2)
                turn += 1
                
            if (xCell, yCell) is not player2 and player==2:
                move(board, player2, currentCell, (xCell, yCell))
                drawBoard(board)
                drawPlayer(player1, player2)
                turn += 1
            
                
        elif board[xCell][yCell]==-1 or (xCell, yCell) not in nextCells:
            board[currentCell[0]][currentCell[1]] = player
            currentCell = -2
            nextCells=[]
            drawBoard(board)
            drawPlayer(player1, player2)
                
    if checkWinner(player1, player2) == 1:
        playerName =  scoreList[len(scoreList)-2]
        scoreList[len(scoreList)-2] = str(playerName)+' win in '+str(turn)+' turn.'
        scoreList.remove(scoreList[len(scoreList)-1])
        with open('score.txt', 'w') as f:
            for line in scoreList:
                f.write(line+'\n')
        winner = str(playerName)+' win in '+str(turn)+'turn.'
        messagebox.showinfo(message=winner)
        sleep(3.5)
        window.destroy()
        
    elif checkWinner(player1, player2) == 2:
        playerName =  scoreList[len(scoreList)-1]
        scoreList[len(scoreList)-1] = str(playerName)+' win in '+str(turn)+' turn.'
        scoreList.remove(scoreList[len(scoreList)-2])
        with open('score.txt', 'w') as f:
            for line in scoreList:
                f.write(line+'\n')
                
        winner = str(playerName)+' win in '+str(turn)+' turn.'
        messagebox.showinfo(message=winner)
        sleep(3.5)
        window.destroy()
            
        
            
def drawPlayer(player1, player2):
    for k in player1:
        i,j = k[0], k[1]
        if (i,j) != (0,0):
            area.create_oval(i*80+5, j*80+5, i*80+75, j*80+75, fill='white')
    for f in player2:
        i ,j = f[0], f[1]
        if (i,j) != (0,0):
            area.create_oval(i*80+5, j*80+5, i*80+75, j*80+75, fill='blue')


def drawBoard(board):
    for i in range(0,10):
        for j in range(0,10):
            if i%2 == 0 and j%2 == 0:
                area.create_rectangle(i*80,j*80, i*80+80,j*80+80, fill = 'white')
            elif i%2 != 0 and j%2 != 0:
                area.create_rectangle(i*80,j*80, i*80+80,j*80+80, fill = 'white')
            elif i%2 == 0 and j%2 != 0:
                area.create_rectangle(i*80,j*80, i*80+80,j*80+80, fill = 'black')  
            elif i%2 != 0 and j%2 == 0:
                area.create_rectangle(i*80,j*80, i*80+80,j*80+80, fill = 'black')  
                

def drawPossibleMove(possibleMove, board, player1, player2):
    drawBoard(board)
    drawPlayer(player1, player2)
    for i in possibleMove:
        area.create_rectangle(i[0]*80,i[1]*80, i[0]*80+80,i[1]*80+80, fill = 'red')              

def findCell(x, y):
    return x//80, y//80


def showScore(scoreList):
    
    if len(scoreList)<10:
        for i in scoreList:
            record = tk.Label(score, text = i, fg = "black")
            record.pack()
    else:
        for j in range(1,10):
            record = tk.Label(score, text = scoreList[-j], fg = "black")
            record.pack()
    
    
        
def close_win(top, scoreList):
   global closed
   top.destroy()
   showScore(scoreList)
   closed = True
   
   
def insert_val(e1, e2, scoreList):
    global closed
    
    file = 'score.txt'
    text1 = entry.get()
    text2 = entry2.get()
    print(text1, text2)
    with open(file, 'a', encoding='utf-8') as f:
        f.write( '\n'+text1+' :')
        f.write( '\n'+text2+' :')
    scoreList.append(text1)
    scoreList.append(text2)
    closed = True

def stopGame(player1, player2):
    numberPawns1 = len(player1)
    numberPawns2 = len(player2)
    
    if (0,0) in player1:
        numberPawns1 -= 1
    if (0,0) in player2:
        numberPawns2 -= 1 
    
    if numberPawns1< numberPawns2:
        playerName =  scoreList[len(scoreList)-1]
        scoreList.pop()
        scoreList.pop()
        winner = str(playerName)+' win'
        with open('score.txt', 'w+') as f:
                for line in scoreList:
                    f.write(line)
        
        messagebox.showinfo(message=winner)
        sleep(3.5)
        window.destroy()
        
        
    elif numberPawns2<len(player1):
        playerName =  scoreList[len(scoreList)-2]
        scoreList.pop()
        scoreList.pop()
        winner = str(playerName)+' win'
        with open('score.txt', 'w+') as f:
                for line in scoreList:
                    f.write(line)
                    
        messagebox.showinfo(message=winner)
        sleep(3.5)
        window.destroy()
    else:
        scoreList.pop()
        scoreList.pop()
        with open('score.txt', 'w+') as f:
                for line in scoreList:
                    f.write(line)
        messagebox.showinfo(message='draw')
        sleep(10)
        window.destroy()
    


board = boardGame()
player1, player2 = playerGenerator(board)
    
window = tk.Tk()
window.title("Checkers")

score = tk.Frame(window)
score.pack(side=tk.RIGHT, expand='False')

instruction = tk.Label(score, text = "Player 1 is white,\nPlayer 2 is blue.\nPlayer 2 starts.\n", fg = "black")
instruction.pack()

title = tk.Label(score, text = "score", fg = "black")
title.pack()

scoreList =[]
with open('score.txt') as f:
    for line in f:
        scoreList.append(line)

area = tk.Canvas(window, width=800, height=800, background="black")
area.pack(side=tk.LEFT, expand='False')

drawBoard(board)
drawPlayer(player1, player2)

turn = 0
area.bind('<1>',lambda event: mouse_click(event, board, player1, player2))

button3 = tk.Button(window,text= "Stop", command= lambda:stopGame(player1, player2))
button3.pack(pady=5, side= tk.BOTTOM)

closed = False 
while closed == False:
    top = tk.Toplevel(window)
    label1 = tk.Label(top,  text = "Enter player1 name", fg = "black")
    label1.pack()
    t = tk.StringVar()
    
    entry= tk.Entry(top, width= 25, textvariable = t)
    entry.pack()
        
    label2= tk.Label(top,  text = "Enter player2 name", fg = "black")
    label2.pack()
    t2 = tk.StringVar()
    entry2= tk.Entry(top, width= 25, textvariable = t2)
    entry2.pack()
    
    button1 = tk.Button(top,text= "Insert", command= lambda:insert_val(t, t2, scoreList))
    button1.pack(pady=5, side= tk.TOP)
    
    button2= tk.Button(top, text="Ok", command=lambda:close_win(top, scoreList))
    button2.pack(pady=5, side= tk.TOP)
       
    top.mainloop()

window.mainloop()