from game import *
import pygame
from interface import *

def game_function():
    # create a window + initialize pygame 
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("snake")
    screen = pygame.display.set_mode((1080, 720))

    running = True
    game = None
    home_screen = Home_Window(screen)

    # if running is True there is a screen
    while running:  
        # FPS
        clock.tick(55)
        # print(clock.get_fps())

        home_screen.starting_update(screen)

        # if we click on PLAY
        if not home_screen.isActivate:
            home_screen.isActivate = game.game_update(screen)

        # update the screen
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu")


            elif event.type == pygame.KEYDOWN:
                                                # keyboard key to control the snake 
                game.snake_head.get_activate_key(event, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP)

            # IN THE HOME WINDOW : event when you click on button 
            elif event.type == pygame.MOUSEBUTTONDOWN and home_screen.isActivate:
                # play button so we create a new game
                if home_screen.button_play_rect.collidepoint(event.pos):
                    game = Game(home_screen)
                    home_screen.isActivate = False
                # level button so we change the level feature
                if home_screen.button_level_rect.collidepoint(pygame.mouse.get_pos()):
                    level_text = switch(home_screen.current_level)
                    
                    if level_text == "error":
                        print("level_text chagement -> ERROR")
                        running = False
                    else :
                        home_screen.current_level = level_text
                        del home_screen.button_level_text
                        home_screen.change_level_text_pos()

            # IN THE GAME WINDOW : if you click on the red button it stop the current game
            elif event.type == pygame.MOUSEBUTTONDOWN and not home_screen.isActivate:

                if game.exit_rect.collidepoint(event.pos):
                    home_screen.isActivate = True
                    
# we create a switch function 
def switch(value):
    return {
        'image/text_easy.png' : 'image/text_medium.png',
        'image/text_medium.png' : 'image/text_hard.png',
        'image/text_hard.png' : 'image/text_expert.png',
        'image/text_expert.png' : 'image/text_easy.png' 
    }.get(value, "error")

game_function()