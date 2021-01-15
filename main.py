import pygame
import os
import random

pygame.init()
width=500
Position=[(7,7), (6,7), (5,7)]

def DrawGrid(win):
    size=width//20
    x=0
    y=0
    for i in range (0,20):
        x=x+size
        y=y+size
        pygame.draw.line(win, (255,255,255), (x,0), (x,width))
        pygame.draw.line(win, (255,255,255), (0,y), (width,y))


def Fruit ():
    global xFruit
    global yFruit
    xFruit=0
    yFruit=0
    stop=True
    while stop==True:
        stop=False
        xFruit=random.randint(0,19)
        yFruit=random.randint(0,19)
        for i in range (0,len(Position)):
            if Position[i][0]==xFruit and Position[i][1]==yFruit:
                stop=True

def main ():
    Fru=False
    win=pygame.display.set_mode((width , width))
    icon=pygame.image.load(os.path.join("image","snake.jpg"))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("SNAKE")
    clock=pygame.time.Clock()
    run=True
    a=x=0
    b=y=0
    while run==True:

        win.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                     y=-1
                     x=0
                if event.key==pygame.K_s:
                    y=1
                    x=0
                if event.key==pygame.K_d:
                    y=0
                    x=1
                if event.key==pygame.K_a:
                    y=0
                    x=-1
        for i in range (len(Position), 1, -1):
            if x!=0 or y!=0:
                Position[i-1]=Position[i-2]
            pygame.draw.rect(win, (255,0,0), ((Position[i-1][0]*25, Position[i-1][1]*25), (25, 25)))
        if x!=0 or y!=0:
            if Position[0][0]+x>19:
                Position[0]=[0,Position[0][1]]
            elif Position[0][0]+x<0:
                 Position[0]=[20,Position[0][1]]
            elif Position[0][1]+y>19:
                 Position[0]=[Position[0][0], 0]
            elif Position[0][1]+y<0:
                Position[0]=[Position[0][0], 20]
            else:
                Position[0]=[Position[0][0]+x,Position[0][1]+y]
        for i in range (1,len(Position)):
            if Position[0]==Position[i]:
                run=False
        pygame.draw.rect(win, (255,0,0), ((Position[0][0]*25, Position[0][1]*25), (25,25)))
        if Position[0]==[a,b]:
            Position.append([1,1])
            Fru=False

        if Fru==False:
            Fruit()
            a=xFruit
            b=yFruit
            Fru=True
        pygame.draw.rect(win, (0,255,0), ((xFruit*25, yFruit*25), (25,25)))
        DrawGrid(win)
        pygame.display.update()
        pygame.time.delay(150)

main()