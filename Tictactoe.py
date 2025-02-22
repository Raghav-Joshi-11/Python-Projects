import pygame
import time
pygame.init()
screen=pygame.display.set_mode((300,300))
pygame.display.set_caption("Tic Tac Toe")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
dict={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
z=0
def show_text(msg,a,b,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(a,b))
def checkwin():
    if dict[1]==dict[4]==dict[7] and dict[1]!="":
        show_text(str(dict[1])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[2]==dict[5]==dict[8] and dict[2]!="":
        show_text(str(dict[2])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[3]==dict[6]==dict[9] and dict[3]!="":
        show_text(str(dict[3])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[1]==dict[2]==dict[3] and dict[1]!="":
        show_text(str(dict[1])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[4]==dict[5]==dict[6] and dict[4]!="":
        show_text(str(dict[4])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[7]==dict[8]==dict[9] and dict[7]!="":
        show_text(str(dict[7])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[1]==dict[5]==dict[9] and dict[1]!="":
        show_text(str(dict[1])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)
    if dict[3]==dict[5]==dict[7] and dict[3]!="":
        show_text(str(dict[3])+" has won the game",5,134,red)
        pygame.display.update()
        time.sleep(3)

def calcpos(x1,y1):
    global z
    if 0<x1<100 and 0<y1<100 and dict[1]=="":
        model_x(50,50)
        if z%2==0:
            dict[1]="O"
        elif z%2==1:
            dict[1]="X"
    if 100<x1<200 and 0<y1<100 and dict[2]=="":
        model_x(150,50)
        if z%2==0:
            dict[2]="O"
        if z%2==1:
            dict[2]="X"
    if 200<x1<300 and 0<y1<100 and dict[3]=="":
        model_x(250,50)
        if z%2==0:
            dict[3]="O"
        if z%2==1:
            dict[3]="X"
        
    if 0<x1<100 and 100<y1<200 and dict[4]=="":
        model_x(50,150)
        if z%2==0:
            dict[4]="O"
        if z%2==1:
            dict[4]="X"
    if 100<x1<200 and 100<y1<200 and dict[5]=="":
        model_x(150,150)
        if z%2==0:
            dict[5]="O"
        if z%2==1:
            dict[5]="X"
    if 200<x1<300 and 100<y1<200 and dict[6]=="":
        model_x(250,150)
        if z%2==0:
            dict[6]="O"
        if z%2==1:
            dict[6]="X"
    if 0<x1<100 and 200<y1<300 and dict[7]=="":
        model_x(50,250)
        if z%2==0:
            dict[7]="O"
        if z%2==1:
            dict[7]="X"
    if 100<x1<200 and 200<y1<300 and dict[8]=="":
        model_x(150,250)
        if z%2==0:
            dict[8]="O"
        if z%2==1:
            dict[8]="X"
    if 200<x1<300 and 200<y1<300 and dict[9]=="":
        model_x(250,250)
        if z%2==0:
            dict[9]="O"
        if z%2==1:
            dict[9]="X"
def model_x(x,y):
    global z
    z+=1
    if z%2==1:
        pygame.draw.line(screen,white,(x+40,y-40),(x-40,y+40),3)
        pygame.draw.line(screen,white,(x-40,y-40),(x+40,y+40),3)
    else:
        pygame.draw.circle(screen,white,(x,y),40,3)
while True:
  pygame.display.update()
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
       calcpos(event.pos[0],event.pos[1])
       checkwin()
    if event.type==pygame.QUIT:
      pygame.quit()
      exit()