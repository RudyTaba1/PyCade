import pygame as pg
import sys

# State of project 3/22
# window opens, paddles appear,
# left paddle can be moved with w/s or up/down
# stationary ball

pg.init()

# screen dimension constants
WIDTH, HEIGHT = 800, 700
CENTER_X, CENTER_Y = (WIDTH / 2), (HEIGHT / 2)

#color constants
WHITE = ((235, 235, 235))
RED = ((186, 13, 13))
BLUE = ((13, 42, 186))

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("pong")

FPS = 30
clock = pg.time.Clock()

bounce_count = 0
player_score = 0
computer_score = 0

"""
While I've used a decent amount of python, I'm pretty new
to using classes/object oriented aspects. Please feel free
to suggest fixes/best practices. 

Might move paddle to its own file, but for now easier to
just use one file.

attributes of paddle:
-color
-position: x & y
-speed
-dimensions: width, height
-possibly is_player
"""


class paddle:
    def __init__(self, x_pos, y_pos, color=WHITE, speed=12, height=110, width=20, is_player=False):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.height = height
        self.width = width
        self.is_player = is_player

        # rectangle/drawing objects
        self.rect = pg.Rect(x_pos, y_pos, width, height)
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)
    
    def set_speed(self, s):
        self.speed = s
    
    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos
    
    def move_toward(self, target_y):
        y = self.y_pos + 65 #vertical center of paddle
        y_mod = 0
        if (y < target_y):
            y_mod = 1
            print("moving down")

        #if the ball is close enough to the center of the paddle, don't move
        #helps prevent excessive stuttering
        #to be updated later to move exact distance to match ball    
        elif(y <= target_y + 10 and y >= target_y - 10): 
            y_mod = 0
            print("staying still")
        else: 
            y_mod = -1
            print("moving up")

        self.update(y_mod)

    
    def display(self):
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def update(self, y_mod):

        self.y_pos += self.speed*y_mod
            
        # prevent from leaving bounds
        if(self.y_pos < 0):
            self.y_pos = 0
        elif (self.y_pos + self.height >= HEIGHT):
            self.y_pos = HEIGHT - self.height

        # update self rectangle
        self.rect = (self.x_pos, self.y_pos, self.width, self.height)

    def __str__(self):
        # mostly for debugging, candidate for later deletion
        return ("paddle " + str(self.x_pos) + ", " + str(self.y_pos))

"""
Attributes of ball:
-size (is both length and width)
-speed
-x, y coords
-color
"""

class ball:
    def __init__(self, sz, sp, x, y, c = RED):
        self.size = sz
        self.speed = sp
        self.x_pos = x
        self.y_pos = y
        self.color = c

        #allow for change of direction
        self.x_vector = 1
        self.y_vector = 1

        # rectangle/draw objects
        self.rect = pg.Rect(x, y, sz, sz)
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def get_y(self):
        return self.y_pos

    def display(self):
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.x_pos += self.speed * self.x_vector
        self.y_pos += self.speed * self.y_vector

        #border hit conditions & reverse direction to bounce
        if(self.x_pos < 0 or self.x_pos > WIDTH - self.size):
            self.x_vector = -self.x_vector
        if (self.y_pos < 0 or self.y_pos > HEIGHT - self.size):
            self.y_vector = -self.y_vector

        self.speed += bounce_count

        self.rect = pg.Rect(self.x_pos, self.y_pos, self.size, self.size)

# create game components
player_paddle = paddle(10, CENTER_Y - 65, is_player=True)
computer_paddle = paddle(WIDTH - 30, CENTER_Y - 65)

game_ball = ball(20, 8, CENTER_X - 20, CENTER_Y - 20)

# contains game logic
def game_loop():

    running = True

    #outside of main loop to provide a few milliseconds
    #for user to process screen before game beings 
    screen.fill((0, 0, 0))
    player_paddle.display()
    computer_paddle.display()   
    game_ball.display()         
    pg.display.update()
    pg.time.wait(300)

    while(running):
        screen.fill((0, 0, 0))

        #handle quit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        y_mod = 0
        #handle keypress
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            y_mod = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            y_mod = 1

        #computer paddle follows ball
        computer_paddle.move_toward(game_ball.get_y() + 10)

        #update graphics 
        player_paddle.update(y_mod)
        game_ball.update()
        player_paddle.display()
        computer_paddle.display()   
        game_ball.display()         
        pg.display.update()
        clock.tick(FPS)
            
game_loop()