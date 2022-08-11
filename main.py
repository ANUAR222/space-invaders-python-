import random

import pygame
import os

pygame.init()
size = (800, 500)
# Crear ventana

FPS = 60
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join('C:\\Users\\anuar\\PycharmProjects\\pythonProject6', "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate((pygame.transform.scale(YELLOW_SPACESHIP, (50, 50))), 90)
RED_SPACESHIP = pygame.image.load('C:\\Users\\anuar\\PycharmProjects\\pythonProject6\\spaceship_red.png')
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (50, 50))
balas = pygame.image.load(
    os.path.join('C:\\Users\\anuar\\PycharmProjects\\pythonProject6', "Sin título.png"))
balas = pygame.transform.scale(balas, (50, 50))
space = pygame.image.load(
    os.path.join('C:\\Users\\anuar\\PycharmProjects\\pythonProject6', "space.png"))
clock = pygame.time.Clock()
run = True
class bulid_map():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))
class enenmy_spaceship:
    def __init__(self, x, y, hp, damage):
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.image = pygame.image.load(
            os.path.join('C:\\Users\\anuar\\PycharmProjects\\pythonProject6', "spaceship_red.png"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def enemi_ia(self,player):
        if self.x < player.x:
            self.x += 1
        elif self.x > player.x:
            self.x -= 1
        elif self.y < player.y:
            self.y += 1
        elif self.y > player.y:
            self.y -= 1
        self.rect.x = self.x
        self.rect.y = self.y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def shoot(self, screen):
        screen.blit(balas, (self.x, self.y))
    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()
    def kill(self):
        pass

class Spaceship:
    def __init__(self, x, y, width, height):
        self.screen = pygame.display.set_mode(size)
        self.atackx = 0
        self.x = x
        self.y = y
        self.damage = 10
        self.hp = 10
        self.width = width
        self.height = height
        self.vel = 5
        self.alaive = True
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.atack = False

    def draw(self, enemy):
        self.screen.fill((215, 224, 217))
        #change the bakground to the image of the space
        self.screen.blit(space, (0, 0))
        self.move()
        if self.alaive:
            #draw the hp of the spaceship
            print(self.hp)
            self.screen.blit(YELLOW_SPACESHIP, (self.x, self.y))
        for k in range(len(enemy)):
            if enemy[k].alaive:
                self.enemies_move_to_the_playe_self(enemy)
                self.screen.blit(RED_SPACESHIP, (enemy[k].x, enemy[k].y))
        self.move()
        pygame.display.update()

    def enemies_move_to_the_playe_self(self, enemy):
        for k in range(len(enemy)):
            x = 0.01
            for j in range(len(enemy)):
                    if enemy[k].x < self.x :
                        enemy[k].x += x
                    if enemy[k].x > self.x :
                        enemy[k].x -= x
                    if enemy[k].y < self.y:
                        enemy[k].y += x
                    if enemy[k].y > self.y:
                        enemy[k].y -= x
                    if enemy[k].x == self.x and enemy[k].y == self.y:
                        self.hp -= enemy[k].damage
                        if enemy[k].hp <= 0:
                            enemy[k].alaive = False

    def move(self):
        if self.left:
            self.x -= self.vel
        if self.right:
            self.x += self.vel
        if self.up:
            self.y -= self.vel
        if self.down:
            self.y += self.vel
    def atack_enemy(self, enemy):
        if self.atack:
            self.atackx = self.x
            while self.atackx <= 800:
                self.screen.blit(balas, (self.atackx, self.y))
                self.atackx += 50
            for k in range(len(enemy)):
                if enemy[k].alaive:
                    if 30 + enemy[k].y > self.y > enemy[k].y-30:
                        enemy[k].hp -= self.damage
                        if enemy[k].hp <= 0:
                            enemy[k].alaive = False
                    if enemy[k].hp <= 0:
                        enemy[k].alaive = False
                pygame.display.update()

    def keydown(self, key):
        if key == pygame.K_LEFT:
            self.left = True
        if key == pygame.K_RIGHT:
            self.right = True
        if key == pygame.K_UP:
            self.up = True
        if key == pygame.K_DOWN:
            self.down = True
        if key == pygame.K_SPACE:
            self.atack = True

    def keyup(self, key):
        if key == pygame.K_LEFT:
            self.left = False
        if key == pygame.K_RIGHT:
            self.right = False
        if key == pygame.K_UP:
            self.up = False
        if key == pygame.K_DOWN:
            self.down = False
        if key == pygame.K_SPACE:
            self.atack = False
def __getitem__(self,key):
    return self.__dict__[key]

spaceship = Spaceship(100, 100, 100, 100)
enmispaceship = Spaceship(300, 100, 100, 100)
# create a array of enemies
enemies = []
for i in range(10):
    enemies.append(Spaceship(random.randint(0, 800), random.randint(0, 500), 100, 100))
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            spaceship.keydown(event.key)

        if event.type == pygame.KEYUP:
            spaceship.keyup(event.key)
    spaceship.atack_enemy(enemies)
    spaceship.move()
    spaceship.draw(enemies)
