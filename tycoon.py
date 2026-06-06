import sys
import pygame
import os
pygame.init()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, 'image-Photoroom.png')
screen = pygame.display.set_mode((800, 600))
run = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('cooper', 36)
money = 1
score = 0
w = 230
h = 50
x = 90
y = 490
l10 = [5, 10, 20, 30, 50, 70, 80, 100, 120, 150]
pp = False
back = pygame.image.load(IMAGE_PATH).convert()
bg = pygame.transform.scale(back, (400, 300))
level1 = 0
levmoney = 100
while run:
    screen.fill((0, 0, 0))
    screen.blit(bg, (500, 0))
    text1 = font.render('Твой баланс: ' + str(score), True, (0, 0, 0))
    text = font.render('Получить ' + str(money) + ' монет', True, (0, 0, 0))
    uluc1 = font.render('Улучшить: ' + str(level1) + '    ' + str(levmoney) + ' монет', True, (0, 0, 0))
    pygame.draw.rect(screen, (173, 216, 230), (x, y, w, h), border_radius = 50)
    pygame.draw.rect(screen, (200, 200, 200), (25, 42, 350, 50))
    pygame.draw.rect(screen, (200, 200, 200), (25, 100, 350, 50))
    screen.blit(text, (100, 500))
    screen.blit(text1, (50, 50))
    screen.blit(uluc1, (50, 110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.draw.rect(screen, (173, 216, 230), (x, y, w, h), border_radius = 50).collidepoint(event.pos):
                    score += money
                    w = 260
                    h = 70
                    x = 75
                    y = 480
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                w = 230
                h = 50   
                x = 90
                y = 490
        if level1 != 'Макс. уровень':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.draw.rect(screen, (200, 200, 200), (25, 100, 350, 50)).collidepoint(event.pos):
                        if score >= levmoney:
                            score -= levmoney
                            level1 += 1
                            levmoney *= 2
                            money = l10[level1 - 1]
    if level1 == 10:
        level1 = 'Макс. уровень'
    pygame.display.flip()
    clock.tick(30)
pygame.quit()