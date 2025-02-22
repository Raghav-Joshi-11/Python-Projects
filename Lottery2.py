import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lottery Simulation")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (192, 192, 192)
darkgray = (80, 80, 80)
green = (0, 255, 0)
nicegreen=(0,204,0)
darkgreen = (0, 153, 0)
red=(255,51,51)

# Button colors
buttoncolor = gray
buttoncolor1 = gray
buttoncolor3 = green
buttoncolor4 = green
buttoncolor5 = green
buttoncolor6 = green
buttoncolor7=darkgray
buttoncolor8=darkgray
buttoncolor9=darkgray
# Global variables
totaltickets = 0
game_state = "menu"  # Tracks the current game state ("menu" or "ticketimg")
megasame=False

# Lottery Numbers & Profit
ballsame=0
mynumbs=[]
jackpotnumbs=[]
megasame=False
tickets=0
profit=0
prize1=0
prize2=0
prize3=0
prize4=0
prize5=0
prize6=0
prize7=0
prize8=0
prize9=0
years=0
label_font_size=45
z=0
alpha=""
def show_text(msg, a, b, color):
    global fontobj,label_font_size
    fontobj = pygame.font.SysFont("freesans", label_font_size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (a, b))
def display_graph(years):
    global game_state, totaltickets,alpha,beta,label_font_size
    if beta=="CD's":
        screen.fill(black)
        show_text(f"CD Growth - {years} Years", 180, 10, white)
        pygame.draw.line(screen, white, (100, 100), (100, 500))
        pygame.draw.line(screen, white, (100, 500), (500, 500)) 
        show_text("Years", 520, 480, white)
        show_text("$", 100, 70, white)
        xscale=400/years
        x=380
        y=120
        for i in range(0,years):
            pygame.draw.line(screen,red,(100+xscale*i,x),(100+xscale*(i+1),x-(y*1.0425-y)),3)
            x=x-(y*1.0425-y)
            y=1.0425*y
        label_font_size=20
        show_text(str(totaltickets*4/1000)+"K",40,280,white)
        show_text(str(totaltickets*8/1000)+"K",40,105,white)
        show_text(str(years/2),290,520,white)
        show_text(str(years),500,520,white)
        if alpha=="a":
            show_text("+123%",520,340,nicegreen)
        if alpha=="b":
            show_text("+152%",520,305,nicegreen)
        if alpha=="c":
            show_text("+230%",520,205,nicegreen)
        pygame.display.update()
    if beta=="Index":
        screen.fill(black)
        show_text(f"S&P 500 Growth - {years} Years", 140, 10, white)
        pygame.draw.line(screen, white, (100, 100), (100, 500))
        pygame.draw.line(screen, white, (100, 500), (500, 500)) 
        show_text("Years", 520, 480, white)
        show_text("$", 100, 70, white)
        x=400
        y=100
        xscale=400/years
        for i in range(0,years):
            chance=random.randint(1,24)
            if chance>6:
                pygame.draw.line(screen,red,(100+xscale*i,x),(100+xscale*(i+1),x-(y*1.1-y)))
                x=x-(y*1.1-y)
                y=1.1*y
            else:
                pygame.draw.line(screen,red,(100+xscale*i,x),(100+xscale*(i+1),x+(y-y*0.87)))
                x=x+(y-y*0.87)
                y=0.87*y
        label_font_size=20
        if x<400:
            show_text("+"+str(round((500-x)/1,1))+"%",510,x-5,nicegreen)
        else:
            show_text("-"+str(round(500-x/1,1))+"%",510,x-5,nicegreen)
        show_text(str(totaltickets*4/1000)+"K",40,280,white)
        show_text(str(totaltickets*8/1000)+"K",40,105,white)
        show_text(str(years/2),290,520,white)
        show_text(str(years),500,520,white)
        pygame.display.update()
    label_font_size=45
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  
                    game_state = "menu"
                    return
def CD(): 
    global game_state,label_font_size,years,totaltickets,alpha,beta
    screen.fill(black)
    butotn=pygame.image.load("butotn-removebg-preview 1.png")
    screen.blit(butotn,(200,75))
    screen.blit(butotn,(200,250))
    screen.blit(butotn,(200,425))
    label_font_size=35
    show_text("How many years? ", 10, 10, white)
    label_font_size=25
    show_text("5 Years",265,110,white)
    show_text("10 Years",248,290,white)
    show_text("20 Years",255,462,white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 200 < event.pos[0] < 400 and 75 < event.pos[1] < 175:
                    years = 5
                    alpha="a"
                    game_state = "graph_display"
                if 200 < event.pos[0] < 400 and 250 < event.pos[1] < 350:
                    years=10
                    alpha="b"
                    game_state="graph_display"
                if 200 < event.pos[0] < 400 and 425 < event.pos[1] < 525:
                    years=20
                    alpha="c"
                    game_state="graph_display"

def investimg(): 
    global buttoncolor7,buttoncolor8,buttoncolor9,game_state,label_font_size,alpha,beta

    screen.fill(black)
    pygame.draw.rect(screen, buttoncolor, (66, 250, 200, 100))
    pygame.draw.rect(screen, buttoncolor1, (332, 250, 200, 100))
    cd=pygame.image.load("Group 14.png")
    sp=pygame.image.load("Group 10.png")
    screen.blit(cd,(66,250))
    screen.blit(sp,(332,250))
    label_font_size=35
    show_text("Which investing option? ", 10, 10, white)
    label_font_size=20
    show_text("S&P 500", 390, 330, white)
    label_font_size=25
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 75 < event.pos[0] < 225 and 225 < event.pos[1] < 325:
                    game_state="CD's"
                    beta="CD's"
                if 375 < event.pos[0] < 525 and 225 < event.pos[1] < 325:
                    game_state="CD's"
                    beta="Index"
    
    # Ticket Selection Screen
def ticketimg():
    global buttoncolor3, buttoncolor4, buttoncolor5, buttoncolor6, totaltickets, game_state

    screen.fill(black)
    ticketer=pygame.image.load("ticket-removebg-preview 1.png")
    screen.blit(ticketer,(100,100))
    screen.blit(ticketer,(100,350))
    screen.blit(ticketer,(350,100))
    screen.blit(ticketer,(350,350))
    show_text("How many tickets? ", 10, 10, white)
    show_text("500", 150, 150, white)
    show_text("1000", 385, 150, white)
    show_text("2000", 138, 400, white)
    show_text("5000", 388, 400, white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 100 < event.pos[0] < 275 and 100 < event.pos[1] < 250:
                    totaltickets = 500
                    game_state="runlottery"
                if 350 < event.pos[0] < 525 and 100 < event.pos[1] < 250:
                    totaltickets = 1000
                    game_state="runlottery"
                if 100 < event.pos[0] < 275 and 350 < event.pos[1] < 500:
                    totaltickets = 2000
                    game_state="runlottery"
                if 350 < event.pos[0] < 525 and 350 < event.pos[1] < 500:
                    totaltickets = 5000
                    game_state="runlottery"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Return to menu
                game_state = "menu"

def runlottery(totaltickets):
    # Initialize variables
    global game_state, screen, fontobj,label_font_size,z  # Use the existing screen
    jackpotnumbs = [random.randint(1, 69) for _ in range(5)]
    jmega = random.randint(1, 26)
    tickets = 0
    profit = 0
    prizes = [0] * 9  # List to store prize counts

    while tickets < totaltickets:
        mynumbs = [random.randint(1, 69) for _ in range(5)]
        mymega = random.randint(1, 26)
        ballsame = sum(1 for num in mynumbs if num in jackpotnumbs)
        megasame = (mymega == jmega)

        # Determine prize
        if ballsame == 0 and megasame:
            profit += 2
            prizes[0] += 1
        elif ballsame == 1 and megasame:
            profit += 4
            prizes[1] += 1
        elif ballsame == 2 and megasame:
            profit += 10
            prizes[2] += 1
        elif ballsame == 3 and not megasame:
            profit += 10
            prizes[3] += 1
        elif ballsame == 3 and megasame:
            profit += 200
            prizes[4] += 1
        elif ballsame == 4 and not megasame:
            profit += 500
            prizes[5] += 1
        elif ballsame == 4 and megasame:
            profit += 10000
            prizes[6] += 1
        elif ballsame == 5 and not megasame:
            profit += 1000000
            prizes[7] += 1
        elif ballsame == 5 and megasame:
            profit += 141000000
            prizes[8] += 1
        else:
            profit -= 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        tickets += 1
    screen.fill(black)
    show_text(f"Simulating Tickets: {tickets}/{totaltickets}", 50, 50, white)
    pygame.display.update()

    # Display results
    
    screen.fill(black)
    label_font_size=30
    show_text(f"You Spent ${totaltickets*2} dollars", 50, 50, white)
    show_text(f"Total Profit: ${profit}", 50, 100, white)
    pygame.draw.line(screen, white, (100, 190), (100, 550))
    pygame.draw.line(screen, white, (100, 550), (460, 550))
    label_font_size=10
    for i in range(0,9):
        pygame.draw.rect(screen,white,(119+i*38,550-2*prizes[i],19,2*prizes[i]))
    show_text("Mega",112,560,white)
    show_text("1+Mega",145,560,white)
    show_text("2+Mega",189,560,white)
    show_text("3 Balls",232,560,white)
    show_text("3+Mega",270,560,white)
    show_text("4 Balls",314,560,white)
    show_text("4+Mega",352,560,white)
    show_text("5 Balls",398,560,white)
    show_text("Win",440,560,white)
    show_text(str(90),75,360,white)
    show_text(str(180),75,185,white)
    label_font_size=25
    show_text("Number of Times Each Prize was Won",115,160,white)
    pygame.display.update()
    time.sleep(5)
    game_state="investimg"
    return
def main_menu():
    #Main menu w/play & quit
    global buttoncolor, buttoncolor1, game_state
    
    screen.fill(black)
    play=pygame.image.load("Plau.png")
    quit=pygame.image.load("Quit.png")
    screen.blit(play,(25,225))
    screen.blit(quit,(325,225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 25 < event.pos[0] < 275 and 225 < event.pos[1] < 375:
                    game_state = "ticketimg"  # Change state to ticket selection
            if 325 < event.pos[0] < 575 and 225 < event.pos[1] < 375:
                    pygame.quit()

    pygame.display.update()



# Main loop
while True:
    if game_state == "menu":
        main_menu()
    elif game_state == "ticketimg":
        ticketimg()
    elif game_state == "runlottery":
        runlottery(totaltickets) 
    elif game_state == "investimg":
        investimg()
    elif game_state=="CD's":
        CD()
    elif game_state == "graph_display":
        display_graph(years)

    pygame.display.update()