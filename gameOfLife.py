#Claire Yegian
#12/14/17
#gameOfLife.py - creates Conway's Game of Life

from ggame import *

def redrawAll():
    rowNum = 1
    for row in data['gameBoard']:
        columnNum = 1
        for column in row:
            Sprite(data['deadCell'],((columnNum*50)-25,(rowNum*50)-25))
            columnNum += 1
        rowNum += 1

def gameBoard():
    data['gameBoard'] = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

"""def mouseClick(event):

    if (event.x>data['squareLocation'][0][0][0] and event.x<data['squareLocation'][0][0][1]):
        print('yay')"""
    
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
