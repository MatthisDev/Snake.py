import pygame
import math 
class Home_Window(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super().__init__()
        self.isActivate = True

        self.create_button_play(screen)
        self.create_button_level(screen)

        # levels parametres 
        self.velocity = None
        self.body_generate = None
        self.space_queu_head = None
        self.body_no_detected = None
        
        self.change_level_text_pos()


    def create_button_play(self, screen):
        self.button_play = pygame.image.load('image/button_play.png')
        self.button_play_rect = self.button_play.get_rect()
        # adjust its position
        self.button_play_rect.x = math.ceil(screen.get_width() / 2.70)
        self.button_play_rect.y = math.ceil(screen.get_height() / 3)
        # adjust its size
        self.button_play_width = math.ceil(self.button_play.get_width()*1.35)
        self.button_play_height = math.ceil(self.button_play.get_height() *1.30)
        self.button_play = pygame.transform.scale(self.button_play, (self.button_play_width, self.button_play_height))
    
    def create_button_level(self, screen):
        self.button_level = pygame.image.load('image/button_bg.png')
        self.button_level_rect = self.button_level.get_rect()
        # adjust its position
        self.button_level_rect.x = math.ceil(screen.get_width()/ 2.50)
        self.button_level_rect.y = math.ceil(screen.get_height()/ 2.10)
        # adjust its size
        self.button_level_width = math.ceil(self.button_level.get_width()*1)
        self.button_level_height = math.ceil(self.button_level.get_height()*0.90)
        self.button_level = pygame.transform.scale(self.button_level, (self.button_level_width, self.button_level_height))
        
        # add text of level
        self.create_button_level_text()

    def create_button_level_text(self):        
        self.current_level = 'image/text_easy.png'
        self.button_level_text = pygame.image.load(self.current_level)
        self.button_level_text_rect = None
        self.change_level_text_pos()
    
    def change_level_text_pos(self):

        if self.current_level == 'image/text_easy.png':
            self.button_level_text = pygame.image.load(self.current_level)
            self.button_level_text = pygame.transform.scale(self.button_level_text , (100, 50))
            self.button_level_text_rect = self.button_level_text.get_rect()
            
            # adjust its position 
            self.button_level_text_rect.x = self.button_level_rect.x + (self.button_level.get_width() * 0.20)
            self.button_level_text_rect.y = self.button_level_rect.y + (self.button_level.get_height()* 0.12)

            self.level_parameters()

        elif self.current_level == 'image/text_medium.png':
            self.button_level_text = pygame.image.load(self.current_level)
            self.button_level_text = pygame.transform.scale(self.button_level_text , (130, 50))
            
            self.button_level_text_rect.x = self.button_level_rect.x + (self.button_level.get_width() * 0.15)

            self.level_parameters()

        elif self.current_level == 'image/text_hard.png':
            self.button_level_text = pygame.image.load(self.current_level)
            self.button_level_text = pygame.transform.scale(self.button_level_text , (100, 50))

            self.button_level_text_rect.x = self.button_level_rect.x + (self.button_level.get_width() * 0.225)

            self.level_parameters()

        elif self.current_level == 'image/text_expert.png':

            self.button_level_text = pygame.image.load(self.current_level)
            self.button_level_text = pygame.transform.scale(self.button_level_text , (120, 45))

            self.button_level_text_rect.x = self.button_level_rect.x + (self.button_level.get_width() * 0.15)
            self.button_level_text_rect.y = self.button_level_rect.y + (self.button_level.get_height() * 0.20)

            self.level_parameters()

    def level_parameters(self):
        if self.current_level == 'image/text_easy.png':
            self.velocity = int(7)
            self.body_generate = int(7)
            self.space_queu_head = int(6)
            self.bodies_no_detected = int(7)

        elif self.current_level == 'image/text_medium.png':
            self.velocity = int(12)
            self.body_generate = int(10)
            self.space_queu_head = int(4)
            self.bodies_no_detected = int(3)

        elif self.current_level == 'image/text_hard.png':
            self.velocity = int(15)
            self.body_generate = int(15)
            self.space_queu_head = int(3)
            self.bodies_no_detected = int(2)

        elif self.current_level == 'image/text_expert.png':
            self.velocity = int(18)
            self.body_generate = int(15)
            self.space_queu_head = int(3)
            self.bodies_no_detected = int(1)

    def starting_update(self, screen):
        screen.blit(self.button_play, self.button_play_rect)
        screen.blit(self.button_level, self.button_level_rect)
        screen.blit(self.button_level_text, self.button_level_text_rect)