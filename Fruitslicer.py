import pygame
import time
import random
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Tic Tac Toe")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
def show_text(msg,a,b,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(a,b))
idleflag=True
runflag=False
leftflag=False
runimgs=[]
idleimgs=[]
direction="right"
for i in range(1,11):
    runimage=pygame.image.load(f"Run ({i}).png")
    runimage=pygame.transform.scale(runimage,(200,200))
    runimgs.append(runimage)
for i in range(1,11):
    idleimage=pygame.image.load(f"Idle ({i}).png")
    idleimage=pygame.transform.scale(idleimage,(200,200))
    idleimgs.append(idleimage)
count=0
x=100
clock=pygame.time.Clock()
x1=random.randint(40,960)
y1=60
banana=pygame.image.load("Group 1 (1).png")
miss=["","X","X X","X X X"]
misses=0
score=0
while True:
    clock.tick(20)
    screen.fill(black)
    screen.blit(banana,(x1,y1))
    if count>9:
        count=0
    if idleflag==True:
        if direction=="right":
            idle=idleimgs[count]
            screen.blit(idle,(x,800))
        if direction=="left":
            idle=pygame.transform.flip(idleimgs[count],True,False)
            screen.blit(idle,(x,800))
    if runflag==True:
        direction="right"
        run=runimgs[count]
        screen.blit(run,(x+10,800))
        x+=10
    elif leftflag==True:
        direction="left"
        left=pygame.transform.flip(runimgs[count],True,False)
        screen.blit(left,(x-10,800))
        x-=10
    count+=1
    player_rect = pygame.Rect(x, 800, 200, 200)
    bananarect=pygame.Rect(x1,y1,100,100)
    show_text(f"Score : {score}",5,5,green)
    if bananarect.colliderect(player_rect):
        score+=1
        time.sleep(.05)
        x1=random.randint(40,960)
        y1=60
    show_text(f"Misses : {miss[misses]}",750,5,red)
    if y1>1000:
        x1=random.randint(40,960)
        y1=60
        misses+=1
    if misses==3:
        show_text(f"Misses : {miss[misses]}",750,5,red)
        show_text("Game Over!",400,480,red)
        pygame.display.update()
        time.sleep(2)
        exit()
    y1=y1+10+score
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                idleflag=False
                leftflag=False
                runflag=True
                direction="right"
            if event.key==pygame.K_LEFT:
                idleflag=False
                runflag=False
                leftflag=True
                direction="left"
        if event.type==pygame.KEYUP:
                idleflag=True
                runflag=False
                leftflag=False

        