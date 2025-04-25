import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp
from pygame.math import Vector2

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes
import snake as sn

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption
    # pygame.display.set_icon(ICON) #UNCOMMENT WHEN ICON IS DEFINED

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    window.fill(WHITE) # 15
    

    #FOREGROUND
    

    #UPDATE DISPLAY
    pygame.display.update()

# def handle_events():
#     """Handles any pygame event such as key input"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: # QUIT
#             return False
    
#     keys = pygame.key.get_pressed()

#     return True


class Main():
    def __init__(self, window):
        self.window = window
        self.snake = sn.Snake(window)
        self.fruit = sn.Apple(window)
        self.score_text = boxes.Text_box(self.window, 10, 10, 10, 10,"Score: ",BLACK)
        self.score = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.score += 1

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMS or not 0 <= self.snake.body[0].y < CELL_NUMS:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.score_text.text = "Score: 0"
        self.score = 0

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(CELL_NUMS):
            if row % 2 == 0:
                for col in range(CELL_NUMS):
                    if col % 2 == 0:

                        grass_rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.window, grass_color, grass_rect)

            else:
                for col in range(CELL_NUMS):
                    if col % 2 !=0:
                        grass_rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(self.window, grass_color, grass_rect)

    def draw_score(self):
        self.score_text.text = "Score: " + str(self.score)

        self.score_text.draw_text()

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    main_game = Main(window)
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # QUIT
                run = False
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)

                
        window.fill((175,215,70))
        main_game.draw_elements()
        pygame.display.update()

        
        # draw(window) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

