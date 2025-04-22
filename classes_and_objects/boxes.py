# These are Classes that help with on screen graphics

#font = pygame.font.Font("C:\\Windows/Users/YangTh599/Documents/GitHub/pygame-template/fonts/MoreSugar-Regular.ttf") # MORESUGAR Font

from colors import *
import pygame
from os.path import join
pygame.init()

class Text_box():

    def __init__(self, window, x, y, width, height, text, text_color = WHITE,rect_color = THAYER_GREEN,font="Comic Sans MS",text_size = 24, draw_rect = True, centered = True, rotation = 0):
        self.rect = pygame.Rect(x,y,width,height) # TEXTBOX BOX
        self.window = window

        # ----RECTANGLE PROPERTIES----
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.draw_rect = draw_rect # BOOLEAN VALUE
        self.rect_color = rect_color # TEXTBOX RECT COLOR
        self.centered = centered
        self.rotation = rotation

        # -----TEXT PROPERTIES-----
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.font = font
        self.text_font = pygame.font.SysFont(font, text_size)

    # ----- MUTATORS -----

    def change_font(self, new_font):
        if (new_font[-4:] == ".ttf" or new_font[-4:] == ".otf"):
            self.text_font = pygame.font.Font(new_font, self.text_size)
        else:
            self.text_font = pygame.font.SysFont(new_font, self.text_size)

        self.font = new_font

    def change_font_color(self, new_color):
        if not isinstance(new_color, tuple):
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        
        self.text_color = new_color

    def change_rect_color(self, new_color):
        if not isinstance(new_color, tuple):
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        if len(new_color) != 3:
            raise ValueError("Tuple need 3 int values in it.")
        
        self.rect_color = new_color

    def italicize(self, italicize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, italic=italicize)
        else:
            self.text_font.set_italic(True)
    
    def bolden(self, boldize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, bold=boldize)
        else:
            self.text_font.set_bold(True)

    def rotate(self, rotation):
        self.rotation = rotation

    def update_text(self, new_text):
        self.text = new_text

    # ----- DRAW FUNCTIONS -----

    def draw_textbox(self):
        text = self.text_font.render(self.text, True, self.text_color)
        if self.rotation != 0:
            text = pygame.transform.rotate(text, self.rotation)
        if self.draw_rect:
            pygame.draw.rect(self.window, self.rect_color, self.rect)
        if self.centered:
            text_rect = text.get_rect(center=self.rect.center)
            self.window.blit(text, text_rect)
        
        else:
            self.window.blit(text, [self.x,self.y])

    def draw_text(self):
        text = self.text_font.render(self.text, True, self.text_color)
        if self.rotation != 0:
            text = pygame.transform.rotate(text, self.rotation)
        self.window.blit(text, [self.x,self.y])

class Image_box():

    def __init__(self,window, x, y, width, height, image, rotation = 0):
        self.window = window
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(image).convert()
        self.rotation = rotation

    def rotate_image(self, angle):
        self.rotation = angle

    def scale(self, factor):
        self.image = pygame.transform.scale(self.image, (self.image.get_rect()[0] * factor, self.image.get_rect()[1] * factor))

    def draw_image(self):
        if self.rotation == 0:
            self.window.blit(self.image, (self.x, self.y))
        else:
            
            rot_image = pygame.transform.rotate(self.image, self.rotation)
            new_rect = rot_image.get_rect(center = self.image.get_rect(topleft = self.rect.topleft).center)
            
            self.window.blit(rot_image, new_rect)

class Button(Text_box):

    def __init__(self, window, x, y, width, height, text, text_color = WHITE,rect_color = THAYER_GREEN, hover_color = LIME,font="Comic Sans MS",text_size = 24, draw_rect = True, centered = True, rotation = 0):
        super.__init__(window, x, y, width, height, text, text_color,rect_color,font,text_size, draw_rect, centered, rotation)

        self.hover_color = hover_color
        self.not_hover_color = rect_color

    def change_hover_color(self, new_color):
        if not isinstance(new_color, tuple):
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        if len(new_color) != 3:
            raise ValueError("Tuple need 3 int values in it.")
        
        self.hover_color = new_color

    def change_not_hover_color(self, new_color):
        if not isinstance(new_color, tuple):
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        if len(new_color) != 3:
            raise ValueError("Tuple need 3 int values in it.")
        
        self.not_hover_color = new_color
        self.rect_color = new_color

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.change_rect_color(self.hover_color)
        else:
            self.change_rect_color(self.rect_color)

    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False



    

