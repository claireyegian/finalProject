#Claire Yegian
#12/14/17
#gameOfLife.py - creates Conway's Game of Life

from ggame import *

def gameBoard():
    data['gameBoard'] = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

def redrawAll():
    gameBoard()
    rowNum = 0
    for row in data['gameBoard']:
        columnNum = 0
        for column in row:
            if data['gameBoard'][rowNum][columnNum] == 0:
                Sprite(data['deadCell'],(columnNum*50,rowNum*50)
            if data['gameBoard'][rowNum][columnNum] == 1:
                Sprite(data['liveCell'],(columnNum*50,rowNum*50)
            columnNum += 1
        rowNum += 1

def mouseClick(event):
    row = event.x//50
    column = event.y//50
    if row > 9:
        print('next generation')
    """Sprite(data['liveCell'],(((row+1)*50)-25,((column+1)*50)-25))
    data['gameBoard'][row][column] = 1"""
    if data['gameBoard'][row][column] == 0:
        data['gameBoard'][row][column] = 1
    if data['gameBoard'][row][column] == 1:
        data['gameBoard'][row][column] = 0
    redrawAll()

"""def numNeighbors(rowNum, columnNum):"""
    
#mouseClick - Should take one argument, event. The function should figure out what row and column the user clicked 
#(event.x and event.y have the coordinates of the click). It should change that cell to the opposite color of its 
#current state. This function should also detect when the user clicks the next generation area of the screen.

if __name__ == '__main__':
    dead = Color(0xffffff,1)
    live = Color(0x000000,1)
    lightGrey = Color(0xD3D3D3,1)
    
    data = {}
    data['deadCell'] = RectangleAsset(50,50,LineStyle(1,lightGrey),dead)
    data['liveCell'] = RectangleAsset(50,50,LineStyle(1,live),live)
    
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
