import pygame
import sys
from game import Game
from colors import Colors

#initialize pygame
pygame.init()

#font for game text
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
play_again_surface = title_font.render("Play again? (Y/N)", True, Colors.white)

#rectangles for position, backgrounf, piece, and play again
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
play_again_rect = pygame.Rect(150, 300, 200, 60)  # Adjust as necessary

#main game window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

#controlling frame rate
clock = pygame.time.Clock()

#intialize game
game = Game()

#event for game updates
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

#check to see if game is over to ask to play again
asking_play_again = False

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if asking_play_again:
                #play again response
                if event.key == pygame.K_y:
                    game.reset()
                    game.game_over = False
                    asking_play_again = False
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
                continue  # Skip other key events if asking to play again

            if game.game_over:
                asking_play_again = True  # Start asking to play again
                continue

                #control movement and action if game is playing
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()

        #auto move piece down
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    #redraw screen
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_green)
    screen.blit(score_surface, (360, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    pygame.draw.rect(screen, Colors.dark_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.dark_grey, next_rect, 0, 10)

    if game.game_over:
        #game over screen and prompt
        screen.blit(game_over_surface, (150, 250, 200, 50))  # Adjust position as needed
        screen.blit(play_again_surface, play_again_rect)
    else:
        #if game isnt over draw current state
        game.draw(screen)

    #update display and control frame rate
    pygame.display.update()
    clock.tick(60)


