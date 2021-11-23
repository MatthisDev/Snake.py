import pygame

class Map(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.background = pygame.image.load('image/Fondnoir.jpg').convert()
        self.background = pygame.transform.scale(self.background, (1080, 720))
        self.rect = self.background.get_rect()
        
        self.LEFT_BORDER = -5
        self.RIGHT_BORDER = 1050
        self.TOP_BORDER = -10
        self.DOWN_BORDER = 700

    def apply_border_parameters(self, snake_position_x, snake_position_y):
        
        if snake_position_x >= self.RIGHT_BORDER:
            snake_position_x = self.LEFT_BORDER
            return snake_position_x, snake_position_y

        elif snake_position_x <= self.LEFT_BORDER:
            snake_position_x = self.RIGHT_BORDER
            return snake_position_x, snake_position_y

        elif snake_position_y >= self.DOWN_BORDER:
            snake_position_y = self.TOP_BORDER
            return snake_position_x, snake_position_y

        elif snake_position_y <= self.TOP_BORDER:
            snake_position_y += self.DOWN_BORDER
            return snake_position_x, snake_position_y

        else:
            return snake_position_x, snake_position_y