import time
from random import randint
import pygame


class Snake_Head(pygame.sprite.Sprite):

    def __init__(self, snake_velocity, body_generate, space_queu_head):
        super().__init__()
        self.image = pygame.image.load('image/tête.png')
        self.image = pygame.transform.scale(self.image, (45, 40))

        self.rect = self.image.get_rect()
        self.rect.y = randint(0, 720)
        self.rect.x = randint(-15, 1080)
    
        self.time_program_stop = 0.0025
        self.direction = "right"

        # [self.rect.x],[self.rect.y]
        self.list_virtual_position = [[], []]
        
        self.current_place = 0
        self.expected_place = 0

        self.body_generate = body_generate
        self.snake_velocity = snake_velocity
        self.space_tail_head = space_queu_head
        

    def move(self, angle):

        if self.direction == "right":
            # time.sleep() adjust the snake's speed
            time.sleep(self.time_program_stop)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.x += self.snake_velocity
        
        elif self.direction == "left":
            time.sleep(self.time_program_stop)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.x -= self.snake_velocity

        elif self.direction == "top":
            time.sleep(self.time_program_stop)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.y -= self.snake_velocity

        elif self.direction == "down":
            time.sleep(self.time_program_stop)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.y += self.snake_velocity

    # key = keyboard key
    def get_activate_key(self, event, right, down, left, top):

        if event.key == right and not self.direction == "left":
            if self.direction == "top":
                self.direction = "right"
                self.move(-90)
            elif self.direction == "down":
                self.direction = "right"
                self.move(90)

        elif event.key == down and not self.direction == "top":
            if self.direction == "right":
                self.direction = "down"
                self.move(-90)
            elif self.direction == "left":
                self.direction = "down"
                self.move(90)

        elif event.key == left and not self.direction == "right":
            if self.direction == "down":
                self.direction = "left"
                self.move(-90)
            elif self.direction == "top":
                self.direction = "left"
                self.move(90)

        elif event.key == top and not self.direction == "down":
            if self.direction == "left":
                self.direction = "top"
                self.move(-90)
            elif self.direction == "right":
                self.direction = "top"
                self.move(90)


    def detect_snake_collision(self, not_good_tomato, tomato, snake_tail, snake_head):

        # collision snake_head -> tomato
        if self.rect.colliderect(tomato.rect):
            print("SnakeHead.collisionDetector -> tomate touchée")
            tomato.get_collision(not_good_tomato, True)
            self.expected_place += self.body_generate
            return False  
        # collision snake_head -> not_good_tomato
        elif self.rect.colliderect(not_good_tomato.rect):
            print("SnakeHead.collisionDetector -> tomate périmé touché")
            return True
        # collision snake_head -> snake_tail
        elif pygame.sprite.spritecollideany(snake_head, snake_tail.group_tail_with_collision):
            print("spritecollideany(snakeHead, allBody.group_Part) -> Propre corps touché ")
            return True
        else:
            tomato.get_collision(not_good_tomato, False)
            return False
        

    # we modify list_virtual_snake_position because we need new positions for snake_tail
    def change_virtual_snake_positions(self, snake_tail):
        # if we didn't need to extend the snake_tail
        if self.current_place - self.space_tail_head == self.expected_place:
            self.list_virtual_position[0].insert(0, int(self.rect.x))
            self.list_virtual_position[1].insert(0, int(self.rect.y))
            self.list_virtual_position[0].pop(len(self.list_virtual_position[0])-1)
            self.list_virtual_position[1].pop(len(self.list_virtual_position[1])-1)
        # if we need to extend, we just add one part of the snake_tail to the snake_tail
        else:
            self.list_virtual_position[0].insert(0, int(self.rect.x))
            self.list_virtual_position[1].insert(0, int(self.rect.y))

            snake_tail.create_one_tail_part(self.current_place - self.space_tail_head, self.expected_place,  self.list_virtual_position)
            self.current_place += 1

# the snake_tail is built with many little part_snake_tail
class One_Part_Snake_tail(pygame.sprite.Sprite):

    def __init__(self, last_part_position_x, last_part_position_y):
        super().__init__()
        self.image = pygame.image.load('image/corps.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = last_part_position_x
        self.rect.y = last_part_position_y

class Snake_Tail(pygame.sprite.Sprite):
    def __init__(self, parts_without_collision):
        super().__init__()

        self.list_parts_snake_tail = []
        self.group_tail_with_collision = pygame.sprite.Group()
        self.parts_without_collision = parts_without_collision

    def create_one_tail_part(self, current_place, expected_place, list_virtual_position):

        PARTS_WITHOUT_COLLISION = int(7)
        virtual_position_x = len(list_virtual_position[0]) - 1
        virtual_position_y = len(list_virtual_position[1]) - 1
        len_snake_tail = len(self.list_parts_snake_tail) - 1

        if expected_place > 0 :
            if current_place < expected_place:
                self.list_parts_snake_tail.append(One_Part_Snake_tail(list_virtual_position[0][virtual_position_x], list_virtual_position[1][virtual_position_y]))
                if current_place > PARTS_WITHOUT_COLLISION:
                    self.group_tail_with_collision.add(self.list_parts_snake_tail[len_snake_tail])
    
    # we move the tail in order to it can follow the snake_head
    def change_tail_position(self, screen, snake_head, space_tail_head):
        
        len_snake_tail = len(self.list_parts_snake_tail) - 1
        i = 0
        while i < len_snake_tail:
            self.list_parts_snake_tail[i].rect.x = snake_head.list_virtual_position[0][space_tail_head + i]
            self.list_parts_snake_tail[i].rect.y = snake_head.list_virtual_position[1][space_tail_head + i]
            screen.blit(self.list_parts_snake_tail[i].image, self.list_parts_snake_tail[i].rect)
            i += 1

class Tomato(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/tomate.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = randint(-15, 1080)
        self.rect.y = randint(0, 720)

    def create(self):
        position_x, position_y = Tomato.change_spawn()
        self.rect.x = position_x
        self.rect.y = position_y

    def get_collision(self, not_good_tomato, is_touching):
        if is_touching:
            not_good_tomato.create_random_spawn(is_touching)
            self.create()
        if not is_touching:
            not_good_tomato.create_random_spawn(is_touching)

    @classmethod
    def change_spawn(cls):
        return randint(-5, 1050), randint(-10, 700)


class Not_Good_Tomato(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('image/tomatePérimé.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        self.rect.x = -4000
        self.rect.y = -4000

        self.is_here = False
        self.time_start = 0

    def create(self):
        position_x, position_y = Tomato.change_spawn()
        self.rect.x = position_x
        self.rect.y = position_y

    def create_random_spawn(self, tomato_is_touching):
        # in second
        TIME_NOT_GOOD_TOMATO_STAY = int(15)  
        
        if not self.is_here and tomato_is_touching:
            LUCK = (int(0), int(2))
            # 1 luck on 3
            control = randint(LUCK[0], LUCK[1])
            print("NOTGOODTOMATO -> tirage au sort : ", control)
            if control == 2:
                self.is_here = True
                self.create()

        if self.is_here and not tomato_is_touching:
            is_finish, self.time_start = Not_Good_Tomato.timer(TIME_NOT_GOOD_TOMATO_STAY, self.time_start)
            if is_finish:
                self.rect.x = -4000
                self.rect.y = -4000
                self.is_here = False

    @classmethod
    def timer(cls, time_in_second, started_time):

        # we take the current time if time is not already activated
        if started_time == 0:
            started_time = time.time()

        current_time = time.time()
        # if the set time is finished the timer reset to 0 
        if current_time >= started_time + time_in_second:
            started_time = 0
            return True, started_time
        else:
            return False, started_time