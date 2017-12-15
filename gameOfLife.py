#Claire Yegian
#12/14/17
#gameOfLife.py - creates Conway's Game of Life

from ggame import *

def buildBoard():
    rowNum = 1
    for row in data['gameBoard']:
        columnNum = 1
        for column in row:
            Sprite(data['deadCell'],((columnNum*50)-25,(rowNum*50)-25))
            columnNum += 1
        rowNum += 1

def mouseClick(event):
    row = 50
    for item in data['gameBoard']:
        column = 50
        for value in item:
            data['squareLocation'][value] = [column-25,row-25]
            column += 50
        row += 50
    if (event.x>20 and event.x<70) and (event.y>185 and event.y<235):
        processNumber(1)
    
#mouseClick - Should take one argument, event. The function should figure out what row and column the user clicked 
#(event.x and event.y have the coordinates of the click). It should change that cell to the opposite color of its 
#current state. This function should also detect when the user clicks the next generation area of the screen.

if __name__ == '__main__':
    dead = Color(0xffffff,1)
    live = Color(0x000000,1)
    lightGrey = Color(0xD3D3D3,1)
    
    data = {}
    data['squareLocation'] = data['gameBoard']
    data['gameBoard'] = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    data['deadCell'] = RectangleAsset(50,50,LineStyle(1,lightGrey),dead)
    data['liveCell'] = RectangleAsset(50,50,LineStyle(1,live),live)
    
    buildBoard()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
