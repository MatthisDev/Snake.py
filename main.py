"""
faire interface - début de partie - paramètre (
    mode : 
    - son
    - niveau type = faible medium hard impossible
    - taille fenêtre
    bouttons : 
    lancer partie 
    quitter jeu
)
"""
from game import *
import pygame
from interfaces import *

def game_function():
    # initialisation fenetre + pygame
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("snake")
    screen = pygame.display.set_mode((1080, 720))

    # variable
    running = True
    # contient une partie qui est entrain d'être jouer
    game = None
    starting_windows = StartingWindows(screen)
    exit_button = Button_exit()

    go = 0
    # running arrête le jeu si = "True"
    while running:  
        # FPS Gestion
        clock.tick(30)
        # print(clock.get_fps())

        starting_windows.starting_update(screen)

        # si fenêtre début n'est pas activé alors jeu marche
        if not starting_windows.isActivate:
            starting_windows.isActivate = game.game_update(screen)
            exit_button.exit_update(screen)

        # met-à-jour le jeu
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu")

        # nous permet de faire bouger notre serpent 
            elif event.type == pygame.KEYDOWN:
            # touches pour controler le serpent
                game.snakeHead.snakeControl(event, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP)

            elif event.type == pygame.MOUSEBUTTONDOWN and starting_windows.isActivate:
            # si clique sur button play alors on lance le jeu
                if starting_windows.button_play_rect.collidepoint(event.pos):
                # on cree une nouvelle partie
                    game = Game(starting_windows)
                    starting_windows.isActivate = False
                    
                if starting_windows.button_levels_rect.collidepoint(pygame.mouse.get_pos()):

                    level_text = switch(starting_windows.actual_level)
                    if level_text == "error":
                        print("level_text chagement -> ERROR")
                        running = False
                    else :
                        starting_windows.actual_level = level_text
                        del starting_windows.button_levels_text
                        starting_windows.button_levels_text_pos()
                        # starting_windows.button_levels_text = pygame.image.load(level_text)
                        # starting_windows.button_levels_text = pygame.transform.scale(starting_windows.button_levels_text , (40, 40))
            elif event.type == pygame.MOUSEBUTTONDOWN and not starting_windows.isActivate:
                if exit_button.exit_rect.collidepoint(event.pos):
                    starting_windows.isActivate = True
                    
                    

# on cree la fonction switch
def switch(value):
    return {
        'image/text_easy.png' : 'image/text_medium.png',
        'image/text_medium.png' : 'image/text_hard.png',
        'image/text_hard.png' : 'image/text_expert.png',
        'image/text_expert.png' : 'image/text_easy.png' 
    }.get(value, "error")

game_function()

