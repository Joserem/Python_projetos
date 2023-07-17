'''
Make game war 
autor: José Henrique



'''


# Libraries ----------------------------------------------------------------------------------------------

import pygame
import random


# Starting the game --------------------------------------------------------------------------------------

pygame.init()

# Window -------------------------------------------------------------------------------------------------

#screen aspect ratio

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Game Z War")

# Game background and characters -------------------------------------------------------------------------

#background
bg = pygame.image.load('image/cenario.png').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

#nazi airplane
naair = pygame.image.load('image/aviaonz.png').convert_alpha()
naair = pygame.transform.scale(naair, (65,65))
naair = pygame.transform.rotate(naair, -90)

#player airplane
playerAir = pygame.image.load('image/aviao.png').convert_alpha()
playerAir = pygame.transform.scale(playerAir, (75,75))
playerAir = pygame.transform.rotate(playerAir, -90)

#missil
missil = pygame.image.load('image/pngegg.png').convert_alpha()
missil = pygame.transform.scale(missil, (37.5,37.5))
missil = pygame.transform.rotate(missil, -0)


# Defining the initial positions of the characters --------------------------------------------------------

pos_naair_x= 500
pos_naair_y = 360

pos_playerAir_x = 200
pos_playerAir_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

#stitches--------------------------------------------------------------------------------------------------

stitches = 3


triggered = False


# Screen open ----------------------------------------------------------------------------------------------

running = True

# Show the points ------------------------------------------------------------------------------------------

font = pygame.font.SysFont('Old School Adventures', 25)
# Enabling image colisions ---------------------------------------------------------------------------------

playerAir_react = playerAir.get_rect()
naair_react = naair.get_rect()
missil_react = missil.get_rect()


# Respawn of nazi plane and missil -------------------------------------------------------------------------

#nazi plane
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

#missil
def respawn_missil():
    triggered = False
    respawn_missil_x = pos_playerAir_x
    respawn_missil_y = pos_playerAir_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]

# colisions -----------------------------------------------------------------------------------------------

def colisions():
    global stitches
    if playerAir_react.colliderect(naair_react) or naair_react.x == 60:
        stitches -=1
        return True
    elif missil_react.colliderect(naair_react):
        stitches +=1
        return True
    else:
        return False
    
#screen close ---------------------------------------------------------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(bg, (0,0))

    #background moving from a carousel --------------------------------------------------------------------

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0)) #creates a background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))


    # Character commands  ---------------------------------------------------------------------------------

    #Player command 1 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and pos_playerAir_y > 1:
        pos_playerAir_y -=1


        #missil command 1
        if not triggered:
            pos_missil_y -= 1


    #Player command 2
    if keys[pygame.K_DOWN] and pos_playerAir_y < 660:
        pos_playerAir_y += 1


        #missil command 2
        if not triggered:
            pos_missil_y += 1

    
    #Triggering the missil
    if keys[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 2

    if stitches == -1:
        running = False


    # Definitions of the respawn of the Nazi plane and missil -----------------------------------------------
     
    #nazi plane
    if pos_naair_x == 50:
        pos_naair_x = respawn()[0]
        pos_naair_y = respawn()[1]

    #missil
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()

    #nazi plane
    if pos_naair_x == 50 or colisions():
        pos_naair_x = respawn()[0]
        pos_naair_y = respawn()[1]


    # React Position ---------------------------------------------------------------------------------------

    playerAir_react.y = pos_playerAir_y
    playerAir_react.x = pos_playerAir_x

    missil_react.x = pos_missil_x
    missil_react.y = pos_missil_y

    naair_react.x = pos_naair_x
    naair_react.y = pos_naair_y

    # Speed of background movement and movement of the Nazi plane ------------------------------------------

    #speed of background
    x-=2  

    #movement nazi plane
    pos_naair_x -=1

    #missil
    pos_missil_x += vel_missil_x


    #Show Score --------------------------------------------------------------------------------------------

    score = font.render(f'Score: {int(stitches)} ', True, (0,0,0))
    screen.blit(score, (10,10))


    #position of characters in background -------------------------------------------------------------------

    screen.blit(naair, (pos_naair_x, pos_naair_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerAir, (pos_playerAir_x, pos_playerAir_y))



    print(stitches)

    pygame.display.update()
