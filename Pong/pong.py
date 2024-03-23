import pygame as pg
import sys

# State of project 3/22
# window opens, paddles appear,
# left paddle can be moved with w/s or up/down

pg.init()

WIDTH, HEIGHT = 800, 700
CENTER_X, CENTER_Y = (WIDTH / 2), (HEIGHT / 2)
screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("pong")

FPS = 30
clock = pg.time.Clock()



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
    def __init__(self, x, y, c=((255, 255, 255)), s=20, h=110, w=20):
        self.color = c
        self.x_pos = x
        self.y_pos = y
        self.speed = s
        self.height = h
        self.width = w

        self.rect = pg.Rect(x, y, w, h)
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)
    
    def set_speed(self, s):
        self.speed = s

    def display(self):
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def update(self, y_mod):
        self.y_pos += self.speed*y_mod

        # prevent from leaving bounds
        if (self.y_pos < 0):
            self.y_pos = 0
        elif (self.y_pos + self.height >= HEIGHT):
            self.y_pos = HEIGHT-self.height


        self.rect = (self.x_pos, self.y_pos, self.width, self.height)

    def __str__(self):
        return ("paddle " + str(self.x_pos) + ", " + str(self.y_pos))

"""
Attributes of ball:
-size (is both length and width)
-speed
-x, y coords
-color
"""

class ball:
    def __init__(self, sz, sp, x, y, c):
        self.size = sz
        self.speed = sp
        self.x_pos = x
        self.y_pos = y
        self.color = c

        self.rect = pg.Rect(x, y, sz, sz)
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def display(self):
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

player_paddle = paddle(10, 300)
computer_paddle = paddle(770, 300)
game_ball = ball(20, 20, (CENTER_X - 20), (CENTER_Y - 20), ((255, 255, 255)))

def game_loop():
    running = True
    while(running):
        screen.fill((0, 0, 0))

        #handle keypress
        y_mod = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            y_mod = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            y_mod = 1


        #update graphics 
        player_paddle.update(y_mod)
        player_paddle.display()
        computer_paddle.display()   
        game_ball.display()         
        pg.display.update()
        clock.tick(FPS)
            
game_loop()