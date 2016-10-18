import pygame
import numpy as np
##import time

## global (to module only) variable defs 
black = (0,0,0)
white = (255,255,255)
red = (255, 0,0)
blue = (0,0,255)
l_gray = (196,195,190)

display_width = 600
display_height = 400
size = [display_width, display_height]


    
cho_rect_w = 190
cho_rect_h = 80
cho_rect_pad = int((display_width - 3*cho_rect_w)/4)
HvHrect = pygame.Rect(cho_rect_pad, display_height/3,cho_rect_w,cho_rect_h)
HvRrect = pygame.Rect(2*cho_rect_pad+cho_rect_w, display_height/3,cho_rect_w,cho_rect_h)
RvRrect = pygame.Rect(3*cho_rect_pad+2*cho_rect_w, display_height/3,cho_rect_w,cho_rect_h)

square_size = 0

##P1turn = True

cell = []
pygame.init()
TTTdisplay = pygame.display.set_mode(size)
def Init_Board():
    global TTTdisplay

    pygame.display.set_caption('TTT')
    TTTdisplay.fill(white)
    pygame.draw.rect(TTTdisplay,black,HvHrect,0)
    pygame.draw.rect(TTTdisplay,black,HvRrect,0)
    pygame.draw.rect(TTTdisplay,black,RvRrect,0)

    # Display mode choice text
    font = pygame.font.Font(None, 36)
    text1 = font.render("H v H?", 1, red)
    text2 = font.render("H v R?", 1, red)
    text3 = font.render("R v R?", 1, red)
    text1pos = HvHrect.center 
    text2pos = HvRrect.center
    text3pos = RvRrect.center
    # unfortunately no direct text onto image in pygame so instead render it onto a
    # new surface and then blit the surface onto the main TTTdisplay
    TTTdisplay.blit(text1, text1pos)
    TTTdisplay.blit(text2, text2pos)
    TTTdisplay.blit(text3, text3pos)

    pygame.display.update()
    return

def ChooseMode():
    global TTTdisplay, pygame
    mode = 0
    while mode == 0:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if HvHrect.collidepoint(event.pos):
                    mode = 1 # HvH
                if HvRrect.collidepoint(event.pos):
                    mode = 2 # HvR
                if RvRrect.collidepoint(event.pos):
                    mode = 3 # RvR
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
##                pygame.quit()
                quit()
    Draw_Board() # draws empty board
    return mode

def Draw_Board():
    global cell, square_size
    cell = [0,1,2] # rows
    TTTdisplay.fill(white) # clear old UX controls
    grid_pad = 50 # pixels on top and left
    square_size = 100
    for i in range(0,3): # rows 
        cell[i]=[] # initialize lists for the columns
        for j in range(0,3): # columns
            left = grid_pad+square_size*(i)
            top = grid_pad+square_size*(j)
            width = height = square_size
            pygame.draw.rect(TTTdisplay,black,(left,top,width,height),2)
            cell[i].append(pygame.Rect(left,top,width,height))
    pygame.display.update()
    return


def HumanMove(P1Turn, board):
    global TTTdisplay, pygame
    Stop = False
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                for i in range(0,3):
                    for j in range(0,3):
                        if cell[j][i].collidepoint(event.pos) and P1Turn:
                            if board[i,j] == 0:
                                board[i,j] = 1
                                move = j+i*3
                                done = True
                        elif cell[j][i].collidepoint(event.pos) and not P1Turn:
                            if board[i,j] == 0:
                                board[i,j] = 2
                                move = j+i*3
                                done = True
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                    exit()
    return move, board, Stop



def Update_Board(board):
    Xs = np.where(board == 2)
    Ohs = np.where(board == 1)
    print("x's:",Xs," o's:",Ohs)
    for x in range(0,len(Xs[0])):
        center = cell[Xs[1][x]][Xs[0][x]].center
        pygame.draw.circle(TTTdisplay,red,center,30,3)
    for o in range(0,len(Ohs[0])):
        xl = cell[Ohs[1][o]][Ohs[0][o]].centerx - square_size/3
        xr = cell[Ohs[1][o]][Ohs[0][o]].centerx + square_size/3
        yu = cell[Ohs[1][o]][Ohs[0][o]].centery - square_size/3
        yd = cell[Ohs[1][o]][Ohs[0][o]].centery + square_size/3
        pygame.draw.line(TTTdisplay,red,(xl,yu),(xr,yd),3)
        pygame.draw.line(TTTdisplay,red,(xr,yu),(xl,yd),3)
    pygame.display.update()
    return


def Get_Board():
    return board

