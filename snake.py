import pygame
from random import randint as r
from pygame.math import Vector2
from colors import *

import pygame_config as cfig

class Snake:

    def __init__(self,window):
        self.window = window
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load("snake_assets/snake_img/head_up.png").convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cfig.CELL_SIZE, cfig.CELL_SIZE))

        self.crunch = pygame.mixer.Sound("snake_assets/crunch/crunch1.mp3")

    def draw_snake(self):
        self.update_head_graphics()

        for index, block, in enumerate(self.body):
            x_pos = int(block.x * cfig.CELL_SIZE)
            y_pos = int(block.y * cfig.CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, cfig.CELL_SIZE, cfig.CELL_SIZE)

            if index == 0:
                self.window.blit(self.head,block_rect)
            else:
                pygame.draw.rect(self.window, THAYER_GREEN, block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)

    def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]
            if head_relation == Vector2(1,0): self.head = pygame.transform.rotate(self.head_up,90)
            elif head_relation == Vector2(-1,0): self.head = pygame.transform.rotate(self.head_up,270)
            elif head_relation == Vector2(0,1): self.head = self.head_up
            elif head_relation == Vector2(0,-1): self.head = pygame.transform.rotate(self.head_up,180)


class Apple:
    
    def __init__(self,window):
        self.window = window
        self.randomize()
        self.apple_img = pygame.image.load("apple_folder/lucas.png").convert_alpha()
        self.apple_img = pygame.transform.scale(self.apple_img, (cfig.CELL_SIZE, cfig.CELL_SIZE))

    def randomize(self):
        self.x = r(0, cfig.CELL_NUMS - 1)
        self.y = r(0, cfig.CELL_NUMS - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cfig.CELL_SIZE), int(self.pos.y * cfig.CELL_SIZE), cfig.CELL_SIZE, cfig.CELL_SIZE)
        self.window.blit(self.apple_img, fruit_rect)
        # pygame.draw.rect(self.window, COMMUNIST_RED, fruit_rect)