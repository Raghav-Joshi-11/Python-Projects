import pygame
import time
import random
pygame.init()
pygame.font.get_init()
 # Explicitly initialize the font module

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
yellow=(255,255,0)

def show_text(msg,a,b,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(a,b))

up=False
left=False
right=False
down=False

foodx=(random.randint(0,600)//10)*10
foody=(random.randint(0,600)//10)*10
snakex=(random.randint(0,600)//10)*10
snakey=(random.randint(0,600)//10)*10
snakebody=[[snakex,snakey]]

score=0
clock=pygame.time.Clock()
while True:
    clock.tick(15)
    screen.fill(black)
    apple=pygame.draw.rect(screen,red,(foodx,foody,40,40))
    snake=pygame.draw.rect(screen,green,(snakex,snakey,40,40))
    for i in snakebody:
        pygame.draw.rect(screen,green,(i[0],i[1],40,40))
    if down==True:
        snakey+=10
    if up==True:
        snakey-=10
    if left==True:
        snakex-=10
    if right==True:
        snakex+=10
    if snakex<0:
        snakex=600
    if snakex>600:
        snakex=0
    if snakey<0:
        snakey=600
    if snakey>600:
        snakey=0
    snakebody.insert(0,[snakex,snakey])
    if snake.colliderect(apple):
        foodx=(random.randint(0,600)//10)*10
        foody=(random.randint(0,600)//10)*10
        score+=1
    else:
        snakebody.pop()
        time.sleep(2)
        pygame.quit()
    for body in snakebody[1:]:
        if [snakex, snakey]==body:
            show_text('Game Over',300,300,white)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            exit()
    show_text(str(score), 300, 10, white)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if up==False:
                    down=True
                    up=False
                    left=False
                    right=False
            if event.key == pygame.K_UP:
                if down==False:
                    down=False
                    up=True
                    left=False
                    right=False
            if event.key == pygame.K_RIGHT:
                if left==False:
                    down=False
                    up=False
                    left=False
                    right=True
            if event.key == pygame.K_LEFT:
                if right==False:
                    down=False
                    up=False
                    left=True
                    right=False
        
        if event.type==pygame.QUIT:
                pygame.quit()
                exit()