import pygame as pg
import random
import math

#State of project 4/1:
    #functional pong game
    #score tracked in terminal
    #random ball "throw" direction to start

#most immediate to-dos:
    #add in game score
    #less predictable ball movements

#cleaning up later, after we get things rolling:
    #-possibly seperate paddle/ball/main for readability
    #-refine computer movements
    #-add constants where appropriate (paddle dimensions?)
    #-python best practices: is get_y or similar necessary? 
    #   I don't know I just carried over the idea of getters
    #   and setters from java
    #-remove uneccessary variables if applicable
    #-smoother graphics, sometimes the computer paddle stutters

pg.init()

# screen dimension constants
WIDTH, HEIGHT = 800, 700
CENTER_X, CENTER_Y = (WIDTH / 2), (HEIGHT / 2)

#color constants
WHITE = ((235, 235, 235))
RED = ((186, 13, 13))
BLUE = ((13, 42, 186))

#other constants
INIT_SPEED = 4

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("pong")

FPS = 60
clock = pg.time.Clock()

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
    
    def get_rect(self):
        return self.rect_draw

    def move_toward(self, target_y):
        y = self.y_pos + 55 #vertical center of paddle
        y_mod = 0

        #move up
        if (y < target_y):
            y_mod = 1

        #if the ball is close enough to the center of the paddle, don't move
        #helps prevent excessive stuttering
        #to be updated later to move exact distance to match ball    
        elif(y <= target_y + 10 and y >= target_y - 10): 
            y_mod = 0
    
        #move down
        else: 
            y_mod = -1

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

player_paddle = paddle(0, CENTER_Y - 55, speed = 10, is_player=True)
computer_paddle = paddle(WIDTH - 20, CENTER_Y - 55)

"""
Attributes of ball:
-size (is both length and width)
-speed
-x, y coords
-color
"""

class ball:
    def __init__(self, sz, x, y, c = RED, sp = INIT_SPEED):
        self.size = sz
        self.speed_base = sp
        self.x_pos = x
        self.y_pos = y
        self.color = c

        #allow for change of direction
        self.x_speed = 1
        self.y_speed = 1

        # rectangle/draw objects
        self.rect = pg.Rect(x, y, sz, sz)
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def get_y(self):
        return self.y_pos
    
    def get_rect(self):
        return self.rect_draw
    
    def inc_speed(self):
        #print("incspeed: " + str(self.speed_base) + "    x: " + str(self.x_speed) + "    y: " + str(self.y_speed))
        cos_ratio = self.speed_base / self.x_speed
        sin_ratio = self.speed_base / self.y_speed

        self.speed_base += 1
        self.x_speed = self.speed_base / cos_ratio
        self.y_speed = self.speed_base / sin_ratio

        #print("postspeed: " + str(self.speed_base) + "    x: " + str(self.x_speed) + "    y: " + str(self.y_speed))
    
    def bounce(self):
        self.x_speed = -self.x_speed
        self.y_speed = -self.y_speed
    
    def reset(self):
        self.x_pos = WIDTH/2 - self.size
        self.y_pos = HEIGHT/2 - self.size
        self.speed_base = INIT_SPEED

        #time for trigonometry!!
        #full explanation just in case:
            
        #for speed to remain constant while the
        #direction changes randomly. Imagine
        #the speed as the hypotenuse of a right 
        #triangle where the ball is at one end
        #of the hypotenuse. to keep the hypotenuse
        #the same length while randomly changing
        #the triangle, we can randomly generate
        #the x value of the speed and then 
        #derive the y value from that to keep
        #the size of the hypotenuse constant. 

        self.x_speed = random.uniform(-self.speed_base, self.speed_base)
        #adjust x so that the ball is not going very vertically
        if (self.x_speed > 0 and self.x_speed < self.speed_base/2):
            self.x_speed += 0.5
        elif (self.y_speed < 0 and self.y_speed > -self.speed_base/2):
            self.y_speed -= 0.5
        
    
        if (self.x_speed == 0 or self.x_speed == self.speed_base or self.x_speed == -self.speed_base): #can't be a right triangle if one of the sides l = 0 or l = hypotenuse
            self.reset()

        #a = sqrt(c^2 - b^2)
        self.y_speed = math.sqrt(math.pow(self.speed_base, 2) - math.pow(self.x_speed, 2))
        
        #randomize y direction
        y_dir = random.randint(1, 2)
        if (y_dir == 2):
            y_dir == -1

        self.y_speed *= y_dir

    def display(self):
        self.rect_draw = pg.draw.rect(screen, self.color, self.rect)

    def update(self):
        global player_score, computer_score

        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

        #border hit conditions & reverse direction to bounce

        #if ball is on left border, computer scores
        if(self.x_pos <= 0):
           computer_score += 1
           pg.time.wait(300)
           self.reset()
           print("COM: " + str(computer_score) + "  PLY:" + str(player_score))
        #if ball is on right border, player score
        if (self.x_pos >= WIDTH - self.size):
            player_score += 1
            pg.time.wait(300)
            self.reset()
            print("COM: " + str(computer_score) + "  PLY:" + str(player_score))
        #if ball is heading offscreen vertically
        if ((self.y_pos <= 0 and self.y_speed <= 0) or (self.y_pos >= HEIGHT - self.size and self.y_speed >= 1)):
            self.y_speed = -self.y_speed


        self.rect = pg.Rect(self.x_pos, self.y_pos, self.size, self.size)

game_ball = ball(20, CENTER_X - 20, CENTER_Y - 20)

#contains game logic
def game_loop():

    running = True

    #outside of main loop to provide a few milliseconds
    #for user to process screen before game beings 
    screen.fill((0, 0, 0))
    player_paddle.display()
    computer_paddle.display() 
    game_ball.reset()  
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

        #collision detection
        if (pg.Rect.colliderect(game_ball.get_rect(), computer_paddle.get_rect())):
            game_ball.inc_speed()
            game_ball.bounce()

        elif (pg.Rect.colliderect(game_ball.get_rect(), player_paddle.get_rect())):
            game_ball.inc_speed()
            game_ball.bounce()

        #update graphics 
        player_paddle.update(y_mod)
        game_ball.update()
        player_paddle.display()
        computer_paddle.display()   
        game_ball.display()         
        pg.display.update()
        clock.tick(FPS)
            
game_loop()