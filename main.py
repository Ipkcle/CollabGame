#import pygame as py

import pygame
from pygame.locals import *

'''Initilizes and sets up the display window and a couple other things.
 '''
def bootUp():
    screenSize=(800, 800)
    global screenSize
    py.init() #initilzes all the pygame modules
    py.display.set_mode(screenSize) #opens a window with dimensions of screenSize
    py.display.set_caption('Testing mouse functions')

def main():
    run = True
    while run:
        #returns tuple of boolean on MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
        mouseStatus = py.mouse.get_pressed() 
        #print(mouseStatus)

        #returns (x,y) of mouse position
        mousePos = py.mouse.get_pos()
        print(mousePos)

       
        moveMouseTo = [100,100]
        #py.mouse.set_pos(moveMouseTo) #sets cursor to 100,100 in the display window

        if mousePos == (0,10) or mouseStatus[0]==1:
            run = False

def test():
    pygame.init()
    pygame.display.set_mode((300,200))
    pygame.display.set_caption('Testing')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                #print event.button
                print pygame.mouse.get_pos()
    pygame.display.quit()

if __name__ == "__main__":
    print("Starting....")
    test()
    #bootUp()
    #main()
    #py.display.quit()
