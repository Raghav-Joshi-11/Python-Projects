import pygame
import time
import random
pygame.init()
screen=pygame.display.set_mode((700,500))
pygame.display.set_caption("Flappy Bird")
def show_text(msg,a,b,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(a,b))
def flappy():
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    blue=(0,0,255)
    green=(0,255,0)
    yellow=(255,255,0)
    x=50
    y=250
    ychange=2
    x1=600
    score=0
    y1=random.randint(1,400)
    clock=pygame.time.Clock()
    birdie=pygame.image.load("flap-removebg-preview 1.png")
    birdie=pygame.transform.scale(birdie,(50,50))
    while True:
        clock.tick(60)
        screen.fill(black)
        bird=screen.blit(birdie,(x,y))
        pipe1=pygame.draw.rect(screen,white,(x1,0,50,y1))
        pipe2=pygame.draw.rect(screen,white,(x1,y1+100,50,400-y1))
        show_text(str(score),600,10,white)
        pygame.display.update()
        y+=ychange
        x1-=2
        if bird.colliderect(pipe1) or bird.colliderect(pipe2):
            show_text("You lost!",300,10,blue)
            pygame.display.update()
            time.sleep(2)
            return()
        if score==10:
            show_text("You Won!",300,10,blue)
            pygame.display.update()
            time.sleep(2)
            return(0)
        if x1+50<0:
            x1=700
            y1=random.randint(1,450)
            score+=1
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    y=y-30
            if event.type==pygame.QUIT:
                exit()
flappy()