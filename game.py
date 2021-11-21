import objet
from map import Map

class Game: 
    def __init__(self, Starting_screen) -> None:
        print("Starting_screen.velocity, Starting_screen.body_generate, Starting_screen.space_queu_head : ", Starting_screen.velocity, Starting_screen.body_generate, Starting_screen.space_queu_head)
        self.snakeHead = objet.SnakeHead(Starting_screen.velocity, Starting_screen.body_generate, Starting_screen.space_queu_head)
        self.tomato = objet.Tomato()
        self.notGoodTomato = objet.NotGoodTomato()
        self.allBody = objet.AllPartsBodySnake(Starting_screen.bodies_no_detected)
        self.map = Map()
        self.list_AllPositions = []

    def game_update(self, screen):

        # on charge les images/assets/objet
        screen.blit(self.map.background, (0, 0))
        screen.blit(self.snakeHead.image, self.snakeHead.rect)
        screen.blit(self.tomato.image, self.tomato.rect)

        # On actualise les coordonnées du joueur, et on effectue le border paramètre
        self.snakeHead.rect.x, self.snakeHead.rect.y = self.map.border(self.snakeHead.rect.x, self.snakeHead.rect.y)
        # on fait bouger le serpent sans le changer d'angle
        self.snakeHead.move(0)
        # en fonction de ce qu'on touche ou non on fait une action
        game_over = self.snakeHead.collisionDetector(screen, self.list_AllPositions, self.notGoodTomato, self.tomato,
                                                    self.allBody, self.snakeHead)

        self.snakeHead.gestionCooTab(self.allBody)

        # s'il y a un corps minimum dans la liste alors on le fait apparaitre à l'écran et on le fait suivre la tête
        if len(self.allBody.list_storageALLBodies) > 0:
            self.allBody.followMod(screen, self.snakeHead, self.snakeHead.spaceQueuHead)
            
        return game_over