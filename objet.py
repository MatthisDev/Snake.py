import time
from random import randint
import pygame


class SnakeHead(pygame.sprite.Sprite):

    def __init__(self, velocity, body_generate, space_queu_head):
        super().__init__()
        self.image = pygame.image.load('image/tête.png')
        self.image = pygame.transform.scale(self.image, (45, 40))

        self.rect = self.image.get_rect()
        self.rect.y = randint(0, 720)
        self.rect.x = randint(-15, 1080)
    
        self.speedTime = 0.0025
        self.direction = "right"
        # garde les coo d'une boucle avant
        # [self.rect.x],[self.rect.y]
        self.list_virtualCoo = [[], []]
        
        self.placeActual = 0
        # nombre de place attendu
        self.placeWatting = 0

        self.body_generate = body_generate
        # 5
        self.velocity = velocity
        # 4
        self.spaceQueuHead = space_queu_head
        


    def move(self, angle):

        # go to the right
        if self.direction == "right":
            # time.sleep() règle la vitesse de la tête
            time.sleep(self.speedTime)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.x += self.velocity
        # go to the left
        elif self.direction == "left":
            time.sleep(self.speedTime)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.x -= self.velocity
        # go to the top
        elif self.direction == "top":
            time.sleep(self.speedTime)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.y -= self.velocity
        # go to the down
        elif self.direction == "down":
            time.sleep(self.speedTime)
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect.y += self.velocity

    def snakeControl(self, event, right, down, left, top):

        if event.key == right and self.direction != "left":
            if self.direction == "top":
                self.direction = "right"
                self.move(-90)
            elif self.direction == "down":
                self.direction = "right"
                self.move(90)
        elif event.key == down and self.direction != "top":
            if self.direction == "right":
                self.direction = "down"
                self.move(-90)
            elif self.direction == "left":
                self.direction = "down"
                self.move(90)
        elif event.key == left and self.direction != "right":
            if self.direction == "down":
                self.direction = "left"
                self.move(-90)
            elif self.direction == "top":
                self.direction = "left"
                self.move(90)
        elif event.key == top and self.direction != "down":
            if self.direction == "left":
                self.direction = "top"
                self.move(-90)
            elif self.direction == "right":
                self.direction = "top"
                self.move(90)

    # tête selon ce qui est touché, ou pas
    # paramètre : objet écran/affichage, tab contient toutes les pos, objet mauvaise tomate, objet bonne tomate, si on gère la tomate, si on gère le corps
    def collisionDetector(self, screen, list_content_all_position, notGoodTomato, tomato, allBody, snakeHead):
        # on traite ce qu'il y a faire au sujet de la tomate
        # si la tomate est touché
        if self.rect.colliderect(tomato.rect):
            print("SnakeHead.collisionDetector -> tomate touchée")
            tomato.ifIsTouchingOr(screen, list_content_all_position, notGoodTomato, True)
            # on informe notre tête qu'il faut x_nombres de têtes en plus
            self.placeWatting += self.body_generate
            return False
        # on actualise toujours la tomate
        elif self.rect.colliderect(notGoodTomato.rect):
            print("SnakeHead.collisionDetector -> tomate périmé touché")
            return True
        elif pygame.sprite.spritecollideany(snakeHead, allBody.group_Part):
            print("spritecollideany(snakeHead, allBody.group_Part) -> Propre corps touché ")
            return True
        else:
            tomato.ifIsTouchingOr(screen, list_content_all_position, notGoodTomato, False)
            return False
        

    # organisation du tableau = 0 est la position tête, x derniere position = position de la dernière partie de la queu
    def gestionCooTab(self, AllPartsBodySnake):
        # 1 -> Premier juste actualisation du tableau (garde même nombre de place)
        if self.placeActual - self.spaceQueuHead == self.placeWatting:
            self.list_virtualCoo[0].insert(0, int(self.rect.x))
            self.list_virtualCoo[1].insert(0, int(self.rect.y))
            self.list_virtualCoo[0].pop(len(self.list_virtualCoo[0])-1)
            self.list_virtualCoo[1].pop(len(self.list_virtualCoo[1])-1)
        # 2 -> Deuxième on ajoute 1 place au tableau 
        else:
            self.list_virtualCoo[0].insert(0, int(self.rect.x))
            self.list_virtualCoo[1].insert(0, int(self.rect.y))

            AllPartsBodySnake.IsGenerateOneBody(self.placeActual , self.spaceQueuHead, self.placeWatting,  self.list_virtualCoo)
            self.placeActual += 1


class PartBodySnake(pygame.sprite.Sprite):

    def __init__(self, last_part_position_x, last_part_position_y):
        super().__init__()
        # une parcelle du corps (image + pos)
        self.image = pygame.image.load('image/corps.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = last_part_position_x
        self.rect.y = last_part_position_y
        # simple paramètre de mouvement
        self.velocity = 1
        self.speedTime = 0.0025
        # designe la direction dans la quelle il faut aller
        self.direction = None

class AllPartsBodySnake(pygame.sprite.Sprite):
    def __init__(self, bodies_no_detected):
        super().__init__()
        # contient toutes les parties, pour former les corps du serpent
        self.list_storageALLBodies = []
        self.nombreParcelles = 0
        self.group_Part = pygame.sprite.Group()
        self.bodies_no_detected = bodies_no_detected

    def IsGenerateOneBody(self, placeActual, spaceQueuHead, placeWatting, list_virtualCoo):

        x = len(list_virtualCoo[0]) - 1
        y = len(list_virtualCoo[1]) - 1
        len_AllBodies = len(self.list_storageALLBodies) - 1

        if placeWatting > 0:
            if placeActual - spaceQueuHead  < placeWatting:
                self.list_storageALLBodies.append(PartBodySnake(list_virtualCoo[0][x], list_virtualCoo[1][y]))
                if placeActual - spaceQueuHead > 7:
                    self.group_Part.add(self.list_storageALLBodies[len_AllBodies])

    def followMod(self, screen, snakeHead, spaceQueuHead):
        i = 0
        len_AllBodies = len(self.list_storageALLBodies) - 1
        while i < len_AllBodies:
            self.list_storageALLBodies[i].rect.x = snakeHead.list_virtualCoo[0][spaceQueuHead + i]
            self.list_storageALLBodies[i].rect.y = snakeHead.list_virtualCoo[1][spaceQueuHead + i]
            screen.blit(self.list_storageALLBodies[i].image, self.list_storageALLBodies[i].rect)
            i += 1

class Tomato(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/tomate.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = randint(-15, 1080)
        self.rect.y = randint(0, 720)

    def generation(self):

        positionX, positionY = Tomato.spawnTomato()
        self.rect.x = positionX
        self.rect.y = positionY

    def ifIsTouchingOr(self, screen, list_content_all_position, notGoodTomato, isTouching):
        # selon si elle est touché ou pas on traite l'information différement
        if isTouching:
            notGoodTomato.randomSpawn(screen, True)
            # genere un nouveau point de spawn aléatoir
            self.generation()
        if not isTouching:
            notGoodTomato.randomSpawn(screen, False)

    @classmethod
    def spawnTomato(cls):
        return randint(-15, 1080), randint(0, 720)


class NotGoodTomato(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # basique initialisation objet
        self.image = pygame.image.load('image/tomatePérimé.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        # position quand elle n'est pas la
        self.rect.x = -4000
        self.rect.y = -4000
        # on dit qu'elle n'est pas la de base
        self.IsHere = False
        # initialisation var temps ou la tomate restera
        self.timeStart = 0

    def generation(self):
        positionX, positionY = Tomato.spawnTomato()
        self.rect.x = positionX
        self.rect.y = positionY

    # paramettre : objet ecran/affichage, tab toutes positions, bool qui dit si elle vient d'être touché
    def randomSpawn(self, screen, isTouching):
        # 1 chance sur 3 de faire spawn la tomate
        if not self.IsHere and isTouching:
            verif = randint(0, 2)
            print("NOTGOODTOMATO -> tirage au sort : ", verif)
            if verif == 2:
                # tomate pas bonne spawn donc elle est la
                self.IsHere = True
                self.generation()

        # tant que la tomate est la alors on continue de l'afficher
        if self.IsHere and not isTouching:
            # on regarde le timer
            isFinish, self.timeStart = NotGoodTomato.timer(15, self.timeStart)
            if isFinish:
                self.rect.x = -4000
                self.rect.y = -4000
                self.IsHere = False
        # on actualise l'image de la tomate
        screen.blit(self.image, self.rect)

    @classmethod
    # paramettre : durer en S, le time worldS ou ca a commence
    def timer(cls, second, timeStart):

        # il ne peut qu'egaler 0 s'il on enregistre pas le temps world
        if timeStart == 0:
            timeStart = time.time()

        # on regarde le temps actuel
        timeNow = time.time()

        # et si le temps actuel est sup ou egal au temps pris y a X second
        if timeNow >= timeStart + second:
            # le temps est atteind, on remet le timer a 0
            timeStart = 0
            return True, timeStart
        else:
            return False, timeStart