#Claire Yegian
#12/14/17
#gameOfLife.py - creates Conway's Game of Life

from ggame import *

#Creates gameboard
def gameBoard():
    return [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

#Prints gameboard (with any updates)
def redrawAll():
    rowNum = 0
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            if data['gameBoard'][rowNum][columnNum] == 0:
                Sprite(data['deadCell'],(columnNum*50,rowNum*50))
            if data['gameBoard'][rowNum][columnNum] == 1:
                Sprite(data['liveCell'],(columnNum*50,rowNum*50))
            columnNum += 1
        rowNum += 1

#Finds out which box the user clicked, and changes the status of that cell (live vs dead)
def mouseClick(event):
    if (event.x>175 and event.x<325) and (event.y>510 and event.y<550):
        nextGeneration()
    else:
        row = event.x//50
        column = event.y//50
        if data['gameBoard'][column][row] == 0:
            data['gameBoard'][column][row] = 1
        else:
            data['gameBoard'][column][row] = 0
        redrawAll()

#Determines which boxes will live on to the next generation and which will die; resets gameboard with these updates
def nextGeneration():
    data['gameBoardUpdate'] = gameBoard()
    rowNum = 0 
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            numLive = numNeighbors(rowNum,columnNum)
            if (data['gameBoard'][columnNum][rowNum] == 1) and numLive<2:
                data['gameBoardUpdate'][columnNum][rowNum] = 0
            if (data['gameBoard'][columnNum][rowNum] == 1) and numLive>3:
                data['gameBoardUpdate'][columnNum][rowNum] = 0
            if (data['gameBoard'][columnNum][rowNum] == 0) and numLive == 3:
                data['gameBoardUpdate'][columnNum][rowNum] = 1
            if (data['gameBoard'][columnNum][rowNum] == 1) and (numLive == 3 or numLive == 2):
                data['gameBoardUpdate'][columnNum][rowNum] = 1
            columnNum += 1
        rowNum += 1
    data['gameBoard'] = data['gameBoardUpdate']
    redrawAll()

#finds and returns the number of living neighbors for each cell
def numNeighbors(rowNum,columnNum):
    numNeighbors = 0
    if columnNum<9 and data['gameBoard'][columnNum+1][rowNum] == 1:
        numNeighbors = numNeighbors + 1
    if columnNum<9 and rowNum<9 and data['gameBoard'][columnNum+1][rowNum+1] == 1:
        numNeighbors = numNeighbors + 1
    if columnNum<9 and rowNum>0 and data['gameBoard'][columnNum+1][rowNum-1] == 1:
        numNeighbors = numNeighbors + 1
    if columnNum>0 and data['gameBoard'][columnNum-1][rowNum] == 1:
        numNeighbors = numNeighbors + 1
    if columnNum>0 and rowNum<9 and data['gameBoard'][columnNum-1][rowNum+1] == 1:
        numNeighbors = numNeighbors + 1
    if columnNum>0 and rowNum>0 and data['gameBoard'][columnNum-1][rowNum-1] == 1:
        numNeighbors = numNeighbors + 1
    if rowNum<9 and data['gameBoard'][columnNum][rowNum+1] == 1:
        numNeighbors = numNeighbors + 1
    if rowNum>0 and data['gameBoard'][columnNum][rowNum-1] == 1:
        numNeighbors = numNeighbors + 1
    return(numNeighbors)

if __name__ == '__main__':
    dead = Color(0xffffff,1) #Colors used in program
    live = Color(0x000000,1)
    lightGrey = Color(0xD3D3D3,1)
    
    data = {} #Program dictionary
    data['deadCell'] = RectangleAsset(50,50,LineStyle(1,lightGrey),dead)
    data['liveCell'] = RectangleAsset(50,50,LineStyle(1,live),live)
    data['gameBoardUpdate'] = []
    
    data['gameBoard'] = gameBoard()
    redrawAll()
    
    nextGen = TextAsset('NextGeneration')
    Sprite(nextGen,(190,520))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
