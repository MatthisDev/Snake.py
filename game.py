from objet import *
from map import Map

class Game: 
    def __init__(self, Starting_screen) -> None:
        # create objets need 
        self.snake_head = Snake_Head(Starting_screen.velocity, Starting_screen.body_generate, Starting_screen.space_queu_head)
        self.tomato = Tomato()
        self.not_good_tomato = Not_Good_Tomato()
        self.snake_tail = Snake_Tail(Starting_screen.bodies_no_detected)
        self.map = Map()
        self.exit_button()
        # when snake is moving what's the angle to which it is orientated 
        self.snake_move_angle = 0

    def game_update(self, screen):

        # display on screen
        screen.blit(self.map.background, (0, 0))
        screen.blit(self.snake_head.image, self.snake_head.rect)
        screen.blit(self.tomato.image, self.tomato.rect)
        screen.blit(self.not_good_tomato.image, self.not_good_tomato.rect)
        screen.blit(self.exit_image, self.exit_rect)

        self.snake_head.rect.x, self.snake_head.rect.y = self.map.apply_border_parameters(self.snake_head.rect.x, self.snake_head.rect.y)

        self.snake_head.move(0)

        game_over = self.snake_head.detect_snake_collision(self.not_good_tomato, self.tomato, self.snake_tail, self.snake_head)

        self.snake_head.change_virtual_snake_positions(self.snake_tail)

        # if there is a tail we display it
        if len(self.snake_tail.list_parts_snake_tail) > 0:
            self.snake_tail.change_tail_position(screen, self.snake_head, self.snake_head.space_tail_head)
            
        return game_over
    
    def exit_button(self):
        self.exit_image = pygame.image.load('image/button_exit.png')
        self.exit_image = pygame.transform.scale(self.exit_image, (40, 40))
        self.exit_rect = self.exit_image.get_rect()
        self.exit_rect.x = 1020
        self.exit_rect.y = 650