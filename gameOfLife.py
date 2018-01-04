#Claire Yegian
#12/14/17
#gameOfLife.py - creates Conway's Game of Life

from ggame import *

def gameBoard():
    data['gameBoard'] = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

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

def nextGeneration():
    rowNum = 0 
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            numNeighbors(rowNum,columnNum)
            if (data['gameBoard'][columnNum][rowNum] == 1) and numNeighbors<2:
                data['gameBoard'][columnNum][rowNum] = 0
            if (data['gameBoard'][columnNum][rowNum] == 1) and numNeighbors>3:
                data['gameBoard'][columnNum][rowNum] = 0
            if (data['gameBoard'][columnNum][rowNum] == 0) and numNeighbors == 3:
                data['gameBoard'][columnNum][rowNum] == 1
            columnNum += 1
        rowNum += 1

def numNeighbors(rowNum,columNum):
    numNeighbors = 0
    if data['gameBoard'][columnNum+1][rowNum] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum+1][rowNum+1] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum+1][rowNum-1] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum-1][rowNum] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum-1][rowNum+1] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum-1][rowNum-1] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum][rowNum+1] == 1:
        numNeighbors = numNeighbors + 1
    if data['gameBoard'][columnNum][rowNum-1] == 1:
        numNeighbors = numNeighbors + 1
    print(numNeighbors)
    return(numNeighbors)
    
#DONT FORGET COMMENTS

if __name__ == '__main__':
    dead = Color(0xffffff,1)
    live = Color(0x000000,1)
    lightGrey = Color(0xD3D3D3,1)
    
    data = {}
    data['deadCell'] = RectangleAsset(50,50,LineStyle(1,lightGrey),dead)
    data['liveCell'] = RectangleAsset(50,50,LineStyle(1,live),live)
    
    gameBoard()
    redrawAll()
    
    nextGen = TextAsset('NextGeneration')
    Sprite(nextGen,(190,520))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()