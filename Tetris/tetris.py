import pygame
import sys
from game import Game
from blocks import Colors
import subprocess

def select_difficulty(screen, title_font):
    difficulty_surface = title_font.render("Difficulty: 1-Easy, 2-Med, 3-Hard", True, Colors.white)
    screen.fill(Colors.dark_green)
    screen.blit(difficulty_surface, (25, 290))
    pygame.display.update()

    difficulty_speeds = {'Easy': 500, 'Medium': 300, 'Hard': 100}
    difficulty = 'Medium'  # Default difficulty

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 'Easy', difficulty_speeds['Easy']
                elif event.key == pygame.K_2:
                    return 'Medium', difficulty_speeds['Medium']
                elif event.key == pygame.K_3:
                    return 'Hard', difficulty_speeds['Hard']

# Initialize pygame
pygame.init()

# Font for game text
title_font = pygame.font.Font(None, 40)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
play_again_surface = title_font.render("Play again? (Y/N)", True, Colors.white)

# Main game window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

# Initialize game
game = Game()

# Start by selecting difficulty
difficulty, drop_speed = select_difficulty(screen, title_font)

# Event for game updates, adjusted for difficulty
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, drop_speed)

# Game loop variables
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
play_again_rect = pygame.Rect(150, 300, 200, 60)# Position for play again message


BASE_SPEED = 500  # milliseconds between moves at the start
SCORE_INCREASE_THRESHOLD = 300

# Initialize Pygame and other game components
pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Speed and scoring
current_drop_speed = BASE_SPEED
last_speed_adjust_score = 0

# Game variables
score = 0
game_over = False
def adjust_speed(base_speed, score):
    speed_increase = score // 300  # Calculate how many times the speed should have increased
    new_speed = max(base_speed - speed_increase * 50, 50)  # Decrease interval by 50ms per increment, not less than 50ms
    return new_speed

current_drop_speed = drop_speed  # Set initial drop speed based on selected difficulty

last_speed_adjust_score = 0

if score // SCORE_INCREASE_THRESHOLD > last_speed_adjust_score // SCORE_INCREASE_THRESHOLD:
    last_speed_adjust_score = score
    current_drop_speed = adjust_speed(BASE_SPEED, score)
    print(f"Score: {score}, New Speed: {current_drop_speed}")  # Debugging output
    pygame.time.set_timer(pygame.USEREVENT+1, current_drop_speed)
# Main game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if game.game_over:
                if event.key == pygame.K_y:
                    # Reset game and reselect difficulty
                    game.reset()
                    game.game_over = False
                    difficulty, drop_speed = select_difficulty(screen, title_font)
                    pygame.time.set_timer(GAME_UPDATE, drop_speed)
                elif event.key == pygame.K_n:
                    pygame.quit()
                    subprocess.Popen(["python3", "MenuIntegration/Gmenu.py"])
                    sys.exit()

                continue

            # Control movement and action if game is playing
            if not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_UP:
                    game.rotate()

        # Auto move piece down
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()
            game.update_score(0, 1)# Update the score by moving down

        if game.score // 300 > last_speed_adjust_score // 300:
            last_speed_adjust_score = game.score
            current_drop_speed = adjust_speed(drop_speed, game.score)
            pygame.time.set_timer(GAME_UPDATE, current_drop_speed)

    # Redraw game state
    screen.fill(Colors.dark_green)
    score_value_surface = title_font.render(f"Score: {game.score}", True, Colors.white)
    screen.blit(score_value_surface, (320, 10))

    pygame.draw.rect(screen, Colors.dark_blue, score_rect)
    pygame.draw.rect(screen, Colors.dark_grey, next_rect)

    if game.game_over:
        screen.blit(game_over_surface, (150, 250))
        screen.blit(play_again_surface, play_again_rect)
    else:
        game.draw(screen)  # Draw the game state (board, pieces)

    pygame.display.update()

