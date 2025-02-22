
import pygame
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Pong")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
y=210
y1=210
x=400
y2=250
speedy2=.4
speedx=.5
score=0
score1=0
p1up=False
p1down=False
p2up=False
p2down=False
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",32)
  msobj=fontobj.render(msg,False,color)
  screen.blit(msobj,(x,y))
while True:
  screen.fill(black)
  pygame.draw.rect(screen,white,(700,y,20,80),)
  pygame.draw.rect(screen,white,(50,y1,20,80),)
  pygame.draw.circle(screen,green,(x,y2),20)
  pygame.display.update()
  if p1up==True:
    y1-=1
  if p1down==True:
    y1+=1
  if p2up==True:
    y-=1
  if p2down==True:
    y+=1
  if 699<x<701 and y<=y2<=y+80:
    speedx=speedx*-1
  if 69<x<71 and y1<=y2<=y1+80:
    speedx=speedx*-1
  if y2<20 or y2>480:
    speedy2=-speedy2
  if x<0:
    x=400
    y2=250
    score+=1
  if x>800:
    x=400
    y2=250
    score1+=1
  x+=speedx
  y2+=speedy2
  for event in pygame.event.get():
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_w:
        p1up=True
      if event.key==pygame.K_s:
        p1down=True
      if event.key==pygame.K_UP:
        p2up=True
      if event.key==pygame.K_DOWN:
        p2down=True

    if event.type==pygame.KEYUP:
      if event.key==pygame.K_w:
        p1up=False
      if event.key==pygame.K_s:
        p1down=False
      if event.key==pygame.K_UP:
        p2up=False
      if event.key==pygame.K_DOWN:
        p2down=False

    if event.type==pygame.QUIT:
      pygame.quit()
      exit()
