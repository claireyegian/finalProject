#Claire Yegian
#12/14/17
#gameOfLife.py - creates Conway's Game of Life

from ggame import *

def gameBoard():
    data['gameBoard'] = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

def redrawAll():
    gameBoard()
    rowNum = 1
    for row in data['gameBoard']:
        columnNum = 1
        for column in row:
            Sprite(data['deadCell'],((columnNum*50)-25,(rowNum*50)-25))
            data['cellStatus'].append('live')
            columnNum += 1
        rowNum += 1

def mouseClick(event):
    row = (event.x-25)//50
    column = (event.y-25)//50
    if row > 9:
        print('next generation')
    if data['cellStatus'][row+(10*column)] == 'dead':
        Sprite(data['liveCell'],(((row+1)*50)-25,((column+1)*50)-25))
        data['cellStatus'][row+(10*column)] = 'live'
    if data['cellStatus'][row+(10*column)] == 'live':
        Sprite(data['deadCell'],(((row+1)*50)-25,((column+1)*50)-25))
        data['cellStatus'][row+(10*column)] = 'dead'
    
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
    data['cellStatus'] = []
    
    redrawAll()
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
