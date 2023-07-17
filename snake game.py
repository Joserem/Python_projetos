'''
Making the snake game

Before starting the code you have to have pygame installed

To install pygame just write in the pip install pygame terminal

'''

import pygame
import time
import random


#------------------------------------------------------------------------------------  First Part ------------------------------------------------------------------------------------------------------


 
snake_speed = 15
 
# Window size -------------------------------------------------------------------------------------------------------
window_x = 720
window_y = 480
 
# defining colors ---------------------------------------------------------------------------------------------------
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame -----------------------------------------------------------------------------------------------
pygame.init()
 
# Initialise game window---------------------------------------------------------------------------------------------
pygame.display.set_caption('Snake Z Game')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller --------------------------------------------------------------------------------
fps = pygame.time.Clock()
 
# defining snake position -----------------------------------------------------------------------------------
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# apple position ----------------------------------------------------------------------------------------------------
apple_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
apple_spawn = True
 
# setting snake direction towards ---------------------------------------------------------------------------
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function ------------------------------------------------------------------------------------------
def show_score(choice, color, font, size):
   
    # font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function--------------------------------------------------------------------------------
def game_over():
   
    # font object my_font
    my_font = pygame.font.SysFont('Old School Adventures', 36)
     
    # text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # Position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 

#------------------------------------------------------------------------------------  Second Part ---------------------------------------------------------------------------------------------------
 
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    
    # directions simultaneously--------------------------------------------------------------

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 

    # Moving the snake-----------------------------------------------------------------------

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 

    # Snake body growing mechanism------------------------------------------------------------

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 10
        apple_spawn = False
    else:
        snake_body.pop()
         
    if not apple_spawn:
        apple_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    apple_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        apple_position[0], apple_position[1], 10, 10))
    
 
    # Game Over conditions ------------------------------------------------------------------
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

 
    # Touching the snake body ---------------------------------------------------------------
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score continuously ---------------------------------------------------------
    show_score(1, white, 'times new roman bold', 30)
 
    # Refresh game screen -------------------------------------------------------------------
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate ---------------------------------------------------------
    fps.tick(snake_speed)
