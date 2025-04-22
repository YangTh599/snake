import pygame
from colors import *

# AMONG US MAKER
def draw_amongus(window:pygame.display, color:tuple, x: int, y : int, scale=1, flip= False):
    """haha draw amongus hahahahahahhhahaha"""
    if flip: # FLIPPED TRUE: AMONG US FACING LEFT
        amogus_body = Ellipse(window,color, x * scale, y * scale,300 *scale,400 * scale)
        amogus_legs1 = Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
        amogus_legs2 = Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
        amogus_backpack = Rectangle(window, color, (x + 275)* scale, (y + 50)* scale,75* scale,300* scale)
        glass = Ellipse(window, CC_BLUE, (x-50)* scale, (y+50)* scale ,300* scale,50* scale)
    else: # FLIPPED FALSE: AMONG US FACING RIGHT 
        amogus_body = Ellipse(window,color, x* scale , y* scale,300* scale,400* scale)
        amogus_legs1 = Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
        amogus_legs2 = Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
        amogus_backpack = Rectangle(window, color, (x - 50)* scale, (y + 50)* scale,75* scale,300* scale)
        glass = Ellipse(window, CC_BLUE, (x+50)* scale, (y+50)* scale ,300* scale,50* scale)

    amongus = [amogus_body,amogus_backpack,amogus_legs1,amogus_legs2,glass]

    return amongus

# SHAPE CLASSES

class Shape(): # SHAPES PARENT CLASS
    """Shapes class, barebones for any shape to be made"""
    def __init__(self, window:pygame.display, color:tuple, width=0):
        """window: The screen or window the shape is meant to be drawn on
        color: tuple of 3 RGB Values (0-255,0-255,0-255)
        width: This value determines whether the shape has a border | default =0 for no border, filled in"""
        self.window = window
        self.color = color
        self.width = width

    def change_color(self, new_color:tuple):
        """Changes the color of the shape
        new_color: a tuple of 3 ints, 0-255 (ex. (255,255,0))"""
        if not isinstance(new_color, tuple):
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        if len(new_color) != 3:
            raise ValueError("Tuple need 3 int values in it.")
        
        self.color = new_color

    def change_width(self, new_width:int):
        """Changes the width of the shape, 0= filled in shape, input bigger than 0 will give the shape a border of that int
        new_width: int determines border width of the shape. 0 for filled in shape """
        self.width = new_width
# ----------
class Line(Shape): # LINE CLASS
    """A class for a simple line"""

    def __init__(self,window:pygame.display, color:tuple, start_coord, end_coord, width=1):
        """window: The screen or window the shape is meant to be drawn on
        color: tuple of 3 RGB Values (0-255,0-255,0-255)
        start_coord: pair of int values the represent (x,y) coordinate points to start the line
        end_coord: pair of int values the represent (x,y) coordinate points to end the line
        width: This value determines the width of the line in pixels (px)
        """

        super().__init__(window, color, width)
        self.start = start_coord
        self.end = end_coord

    def new_start_points(self,new_x:int, new_y:int):
        """Gives the line a new starting point to be on.
        new_x: int value that represents the new x coordinate for the starting point
        new_y: int value that represents the new y coordinate for the starting point"""

        self.start = [new_x, new_y]

    def new_end_points(self,new_x:int, new_y:int):
        """Gives the line a new ending point to be on.
        new_x: int value that represents the new x coordinate for the starting point
        new_y: int value that represents the new y coordinate for the starting point"""

        self.end = [new_x, new_y]

    def move_right(self, displacement:int):
        """Moves the line to the right by a number of pixels
        displacement: int value of how many pixels to move the line to the right"""

        self.new_start_points(self.start[0] + displacement, self.start[1])
        self.new_end_points(self.end[0] + displacement, self.end[1])
    
    def move_left(self, displacement:int):
        """Moves the line to the left by a number of pixels
        displacement: int value of how many pixels to move the line to the left"""

        self.new_start_points(self.start[0] - displacement, self.start[1])
        self.new_end_points(self.end[0] - displacement, self.end[1])

    def move_up(self, displacement:int):
        """Moves the line up by a number of pixels
        displacement: int value of how many pixels to move the line up"""

        self.new_start_points(self.start[0], self.start[1] - displacement)
        self.new_end_points(self.end[0], self.end[1] - displacement)

    def move_down(self, displacement:int):
        """Moves the line down by a number of pixels
        displacement: int value of how many pixels to move the line down"""

        self.new_start_points(self.start[0], self.start[1] + displacement)
        self.new_end_points(self.end[0], self.end[1] + displacement)

    def draw(self):
        """Draws the line on the screen"""

        pygame.draw.line(self.window,self.color, self.start, self.end, self.width)
# ----------
class Rectangle(Shape): # RECTANGLE CLASS << SHAPES
    """A class to draw rectangular shape"""
    def __init__(self, window:pygame.display, color:tuple, x:int, y:int ,side_width=1, side_height=1, line_width=0):
        """window: The screen or window the shape is meant to be drawn on
        color: tuple of 3 RGB Values (0-255,0-255,0-255)
        x: int value that determines the x-axis placement of the top left vertex of the rectangle (closer to 0: goes left, further from 0 goes right)
        y: int value that determines the y-axis placement of the top left vertex of the rectangle (closer to 0: goes up, further from 0 goes down)
        side_height: int value that determines how tall the rectangle is (going down from (x,y) coordinate)
        side_width: int value that determine how long the rectangle goes (going right from (x,y) coordinate)
        width: This value determines whether the shape has a border | default =0 for no border, filled in"""

        super().__init__(window,color, line_width)
        self.rect = pygame.Rect(x,y,side_width,side_height)

        self.x = x 
        self.y = y
        self.side_width = side_width
        self.side_height = side_height

    def change_side_lengths(self, new_width:int, new_height:int):
        """Change the side lengths of the rectangle
        new_width: sets the width of the rectangle to the new given int value
        new_height: sets the height of the rectangle to the new given int value"""

        self.rect = pygame.Rect(self.x,self.y,new_width,new_height)

        self.side_width = new_width
        self.side_height = new_height

    def change_side_width(self, new_width:int):
        """Change the width of the rectangle
        new_width: sets the width of the rectangle to the new given int value"""

        self.change_side_lengths(new_width, self.side_height)

    def change_side_height(self, new_height:int):
        """Change the height of the rectangle
        new_height: sets the height of the rectangle to the new given int value"""

        self.change_side_lengths(self.side_width, new_height)

    def change_pos(self,new_x:int,new_y:int):
        """changes the (x,y) positioning of the rectangle"""
        self.x = new_x
        self.y = new_y

        self.rect = pygame.Rect(new_x,new_y,self.side_width,self.side_height)

    def change_x_pos(self, new_x:int):
        self.change_pos(new_x, self.y)
    
    def change_y_pos(self, new_y:int):
        self.change_pos(self.x, new_y)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect, self.width)
# ----------
class Square(Rectangle): # SQUARE CLASS << RECTANGLE << SHAPES

    def __init__(self, window, color, x, y, side_length = 1, line_width = 0):
        super().__init__(window, color, x, y, side_length, side_length, line_width)

    def change_side_lengths(self, new_length: int):
        return super().change_side_lengths(new_length, new_length)
    
    def change_side_width(self, new_width:int):
        self.change_side_lengths(new_width, new_width)

    def change_side_height(self, new_height:int):
        self.change_side_lengths(new_height, new_height)
# ----------
class Circ(Shape): # CIRCLE CLASS << SHAPES
    
    def __init__(self, window, color, center_coords, radius, width=0):
        super().__init__(window,color, width)
        self.center = center_coords
        self.x, self.y = center_coords
        self.r = radius

    def change_radius(self, new_r:int):
        self.r = new_r

    def change_pos(self,new_x:int,new_y:int):
        self.center = (new_x,new_y)

        self.x = new_x
        self.y = new_y

    def change_x_pos(self, new_x:int):
        self.change_pos(new_x, self.y)
    
    def change_y_pos(self, new_y:int):
        self.change_pos(self.x, new_y)

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.center, self.r, self.width)
# ----------
class Ellipse(Rectangle): # ELLIPSE CLASS << RECTANGLE << SHAPES

    def __init__(self, window, color, x, y, side_width=1, side_height=1, line_width = 0):
        super().__init__(window, color, x, y, side_width, side_height, line_width)

    def draw(self):
        pygame.draw.ellipse(self.window, self.color, self.rect, self.width)
# ----------
class Polygon(Shape): # POLYGON CLASS << SHAPES

    def __init__(self,window, color, points, width=0):
        super().__init__(window,color,width)
        self.points = points

    def move_right(self, displacement):
        for coords in self.points:
            coords[0] + displacement
    
    def move_left(self, displacement):
        for coords in self.points:
            coords[0] - displacement

    def move_up(self, displacement):
        for coords in self.points:
            coords[1] - displacement

    def move_down(self, displacement):
        for coords in self.points:
            coords[1] + displacement

    def draw(self):
        pygame.draw.polygon(self.window,self.color,self.points,self.width)