https://nightshadow.tistory.com/entry/pygame-%EC%9D%98-%EC%8A%A4%ED%94%84%EB%9D%BC%EC%9D%B4%ED%8A%B8-%EC%B6%A9%EB%8F%8C%EC%B2%B4%ED%81%AC-%EB%B0%A9%EB%B2%95?category=149211

import pygame, random


pygame.init()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))
background = pygame.Surface(screen.get_size())
BK = (0, 0, 0)
WH = (255, 255, 255)
pacmanpos = [100, 100]
keys = [False, False, False, False]


class Block(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()

pacman = pygame.image.load("resources/images/pacman1.png").convert_alpha()
dot = pygame.image.load("resources/images/small_circle.png").convert_alpha()


block_list = pygame.sprite.Group()

for i in range(1,4):
    block = Block(dot)
    block.rect.x = i * 50
    block.rect.y = 50
    block_list.add(block)


b_pacman = Block(pacman)
b_pacman.mask = pygame.mask.from_surface(b_pacman.image)
b_dot = Block(dot)
b_dot.mask = pygame.mask.from_surface(b_dot.image)
hit_list = pygame.sprite.spritecollide()


while True:

    screen.fill(BK)
    block_list.draw(background)
    screen.blit(background,(0, 0))
    screen.blit(pacman, pacmanpos)
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            if event.key == pygame.K_a:
                keys[1] = True
            if event.key == pygame.K_s:
                keys[2] = True
            if event.key == pygame.K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            if event.key == pygame.K_a:
                keys[1] = False
            if event.key == pygame.K_s:
                keys[2] = False
            if event.key == pygame.K_d:
                keys[3] = False
    if keys[0]:
        pacmanpos[1] -= 0.3
    elif keys[2]:
        pacmanpos[1] += 0.3
    elif keys[1]:
        pacmanpos[0] -= 0.3
    elif keys[3]:
        pacmanpos[0] += 0.3

    pygame.display.update()
