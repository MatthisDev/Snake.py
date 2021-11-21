import pygame
import math 
class StartingWindows(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super().__init__()
        self.isActivate = True
        # button play initialisation 
        self.button_play = pygame.image.load('image/button_play.png')
        self.button_play_rect = self.button_play.get_rect()
        # positionne le boutton play
        self.button_play_rect.x = math.ceil(screen.get_width() / 2.70)
        self.button_play_rect.y = math.ceil(screen.get_height() / 3)
        # change la taille du boutton play
        self.button_play_width = math.ceil(self.button_play.get_width()*1.35)
        self.button_play_height = math.ceil(self.button_play.get_height() *1.30)
        self.button_play = pygame.transform.scale(self.button_play, (self.button_play_width, self.button_play_height))


        
        # button level initialisation
        self.button_levels = pygame.image.load('image/button_bg.png')
        self.button_levels_rect = self.button_levels.get_rect()
        # positionne le boutton level
        self.button_levels_rect.x = math.ceil(screen.get_width()/ 2.50)
        self.button_levels_rect.y = math.ceil(screen.get_height()/ 2.10)
        # change la taille du boutton levels
        self.button_levels_width = math.ceil(self.button_levels.get_width()*1)
        self.button_levels_height = math.ceil(self.button_levels.get_height()*0.90)
        self.button_levels = pygame.transform.scale(self.button_levels, (self.button_levels_width, self.button_levels_height))
        
        # initialisation du button levels text par defaut sur le mode easy
        self.actual_level = 'image/text_easy.png'
        self.button_levels_text = pygame.image.load(self.actual_level)
        self.button_levels_text_rect = None

        # parametres 
        self.velocity = None
        self.body_generate = None
        self.space_queu_head = None
        self.body_no_detected = None
        
        self.button_levels_text_pos()



    def starting_update(self, screen):
        screen.blit(self.button_play, self.button_play_rect)
        screen.blit(self.button_levels, self.button_levels_rect)
        screen.blit(self.button_levels_text, self.button_levels_text_rect)
    
    def button_levels_text_pos(self):

        if self.actual_level == 'image/text_easy.png':
            self.button_levels_text = pygame.image.load(self.actual_level)
            self.button_levels_text = pygame.transform.scale(self.button_levels_text , (100, 50))
            self.button_levels_text_rect = self.button_levels_text.get_rect()
            
            # modifie ses coordonnées 
            self.button_levels_text_rect.x = self.button_levels_rect.x + (self.button_levels.get_width() * 0.20)
            self.button_levels_text_rect.y = self.button_levels_rect.y + (self.button_levels.get_height()* 0.12)

            self.level_parameters()

        elif self.actual_level == 'image/text_medium.png':
            self.button_levels_text = pygame.image.load(self.actual_level)
            self.button_levels_text = pygame.transform.scale(self.button_levels_text , (130, 50))
            
            self.button_levels_text_rect.x = self.button_levels_rect.x + (self.button_levels.get_width() * 0.15)

            self.level_parameters()

        elif self.actual_level == 'image/text_hard.png':
            self.button_levels_text = pygame.image.load(self.actual_level)
            self.button_levels_text = pygame.transform.scale(self.button_levels_text , (100, 50))

            self.button_levels_text_rect.x = self.button_levels_rect.x + (self.button_levels.get_width() * 0.225)

            self.level_parameters()

        elif self.actual_level == 'image/text_expert.png':

            self.button_levels_text = pygame.image.load(self.actual_level)
            self.button_levels_text = pygame.transform.scale(self.button_levels_text , (120, 45))

            self.button_levels_text_rect.x = self.button_levels_rect.x + (self.button_levels.get_width() * 0.15)
            self.button_levels_text_rect.y = self.button_levels_rect.y + (self.button_levels.get_height() * 0.20)

            self.level_parameters()

    def level_parameters(self):
        if self.actual_level == 'image/text_easy.png':
            self.velocity = int(7)
            self.body_generate = int(7)
            self.space_queu_head = int(6)
            self.bodies_no_detected = int(7)

        elif self.actual_level == 'image/text_medium.png':
            self.velocity = int(12)
            self.body_generate = int(10)
            self.space_queu_head = int(4)
            self.bodies_no_detected = int(3)

        elif self.actual_level == 'image/text_hard.png':
            self.velocity = int(15)
            self.body_generate = int(15)
            self.space_queu_head = int(3)
            self.bodies_no_detected = int(2)

        elif self.actual_level == 'image/text_expert.png':
            self.velocity = int(18)
            self.body_generate = int(15)
            self.space_queu_head = int(3)
            self.bodies_no_detected = int(1)


class Button_exit(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.exit_image = pygame.image.load('image/button_exit.png')
        self.exit_image = pygame.transform.scale(self.exit_image, (40, 40))
        self.exit_rect = self.exit_image.get_rect()
        self.exit_rect.x = 1020
        self.exit_rect.y = 650
        

    def exit_update(self, screen):
        screen.blit(self.exit_image, self.exit_rect)


