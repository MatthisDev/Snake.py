import pygame


class Map(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('image/Fondnoir.jpg').convert()
        self.background = pygame.transform.scale(self.background, (1080, 720))
        self.rect = self.background.get_rect()

    @classmethod
    # border parametre dit que si la position de la tete touche une bordure alors on fait apparaitre a l oppose
    def border(cls, positionEntite_x, positionEntite_y):
        # variables contenant le position reel des borders
        left_border = -15
        right_border = 1080
        top_border = 0
        down_border = 720

        # fait apparaitre au côté opposé l'entité
        if positionEntite_x >= right_border:
            positionEntite_x = left_border
            return positionEntite_x, positionEntite_y

        elif positionEntite_x <= left_border:
            positionEntite_x = right_border
            return positionEntite_x, positionEntite_y

        elif positionEntite_y >= down_border:
            positionEntite_y = top_border
            return positionEntite_x, positionEntite_y

        elif positionEntite_y <= top_border:
            positionEntite_y += down_border
            return positionEntite_x, positionEntite_y

        else:
            return positionEntite_x, positionEntite_y
