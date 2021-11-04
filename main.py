from objet import *
from map import *
import pygame

# initialisation fenetre + pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("snake")
screen = pygame.display.set_mode((1080, 720))

# variable
running = True
keyValidation = "right"
list_content_all_position = []


# Fonction qui permet de choisir l'espace entre la queu et la tête et la tête et la queue
# permet d'alleger le traitement des informations par micro second et empecher que le serpent ralentisse
def initialisationOfQueu():

    # espaceQueuTete = int(input("Initialisation -> Choisir votre espace entre la tête et la queu : "))
    nombre_corp_generate = int(input("Initialisation -> Choisir le nombre de corps généré : "))

    return nombre_corp_generate

# on definit des variables pour pouvoir faire nos réglages
numberBodyGenerate = initialisationOfQueu()

# initialisation des objets
tomato = Tomato()
notGoodTomato = NotGoodTomato()

snakeHead = SnakeHead()

mainMap = Map()

allBody = AllPartsBodySnake()


# boucle qui fait tourner le jeu en continue
while running:
    # FPS Gestion
    clock.tick(30)
    #print(clock.get_fps())

    # on charge les images/assets/objet
    screen.blit(mainMap.background, (0, 0))
    screen.blit(snakeHead.image, snakeHead.rect)
    screen.blit(tomato.image, tomato.rect)

    # On actualise les coordonnées du joueur, et on effectue le border paramètre
    snakeHead.rect.x, snakeHead.rect.y = mainMap.border(snakeHead.rect.x, snakeHead.rect.y)
    # on fait bouger le serpent sans le changer d'angle
    snakeHead.move(0)
    # en fonction de ce qu'on touche ou non on fait une action
    running = snakeHead.collisionDetector(screen, list_content_all_position, notGoodTomato, tomato, allBody, snakeHead, numberBodyGenerate)

    snakeHead.gestionCooTab(allBody)

    # s'il y a un corps minimum dans la liste alors on le fait apparaitre à l'écran et on le fait suivre la tête
    if len(allBody.list_storageALLBodies) > 0:
        allBody.followMod(screen, snakeHead, snakeHead.spaceQueuHead)    

    # met-à-jour le jeu
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

        # nous permet de faire bouger notre serpent 
        elif event.type == pygame.KEYDOWN:
            # systeme de controle
            snakeHead.snakeControl(event, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP)