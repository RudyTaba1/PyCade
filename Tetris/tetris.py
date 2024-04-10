import pygame
import sys
from game import Game
from colors import Colors

# Initialize pygame
pygame.init()

# Font for game text
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
play_again_surface = title_font.render("Play again? (Y/N)", True, Colors.white)
difficulty_surface = title_font.render("Difficulty: 1-Easy, 2-Med, 3-Hard", True, Colors.white)

# Rectangles for position, background, piece, and play again
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
play_again_rect = pygame.Rect(150, 300, 200, 60)  # Adjust as necessary

# Main game window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

# Controlling frame rate
clock = pygame.time.Clock()

# Difficulty Selection
screen.fill(Colors.dark_green)
screen.blit(difficulty_surface, (25, 290))
pygame.display.update()

difficulty_speeds = {'Easy': 500, 'Medium': 300, 'Hard': 100}
difficulty = 'Medium'  # Default difficulty

# Menu loop for difficulty selection
selecting_difficulty = True
while selecting_difficulty:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                difficulty = 'Easy'
                selecting_difficulty = False
            elif event.key == pygame.K_2:
                difficulty = 'Medium'
                selecting_difficulty = False
            elif event.key == pygame.K_3:
                difficulty = 'Hard'
                selecting_difficulty = False

# Set the drop speed based on selected difficulty
drop_speed = difficulty_speeds[difficulty]

# Initialize game
game = Game()

# Event for game updates, adjusted for difficulty
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, drop_speed)

# Check to see if game is over to ask to play again
asking_play_again = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if asking_play_again:
                # Play again response
                if event.key == pygame.K_y:
                    game.reset()
                    game.game_over = False
                    asking_play_again = False
                    pygame.time.set_timer(GAME_UPDATE, drop_speed)  # Reset timer for difficulty
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
                continue  # Skip other key events if asking to play again

            if game.game_over:
                asking_play_again = True  # Start asking to play again
                continue

            # Control movement and action if game is playing
            if not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate()

        # Auto move piece down
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Redraw screen
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_green)
    screen.blit(score_surface, (360, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    pygame.draw.rect(screen, Colors.dark_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.dark_grey, next_rect, 0, 10)

    if game.game_over:
        # Game over screen and prompt
        screen.blit(game_over_surface, (150, 250, 200, 50))  # Adjust position as needed
        screen.blit(play_again_surface, play_again_rect)
    else:
        # If game isn't over draw current state
        game.draw(screen)

    # Update display and control frame rate
    pygame.display.update()
    clock.tick(100)



