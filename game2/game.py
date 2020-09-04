import pygame
from pygame import *
import os
from dino import *
import time
import floor
import cactus
import pter
import random

pygame.init()
screen = display.set_mode( (1080, 720) )
obj_group = sprite.Group()
objects = []
di = dino(100, 60, '', 200, 600, 10 )
objects.append( di )
fl = floor.Floor()
enemies = []
print(fl.rect.x)
obj_group.add( di )
obj_group.add( fl )
background = image.load('textures/background.png')
f = font.SysFont('Arial', 60)
end_text = f.render('Game over', True, (255,0, 0) )
score_f = font.SysFont('Arial', 32)
v_text = f.render('Вы победили!', True, (255,0, 0) )

score = 0
scorepoint = 1000
stone_speed = 15
pter_speed = 20
op = 0

while True:
    for e in pygame.event.get():
        if (e.type == QUIT) or (e.type == KEYDOWN and e.key == K_ESCAPE):
            os._exit(0)
        if e.type == KEYDOWN and e.key == K_LALT and di.direct not in ['endgame', 'bob', 'victory']:
            objects[0].direct = 'jump'
            
        if e.type == KEYDOWN and e.key == K_s and di.direct not in ['endgame', 'jump', 'victory'] :
            di.image = Surface((60, 50))
            di.image = image.load('textures/dino2.png')
            di.direct = 'bob'
            di.rect = Rect(di.rect.x, di.rect.y + 50, 60, 50)
        if e.type == KEYUP and e.key == K_s and di.direct not in ['endgame', 'jump', 'victory'] and di.direct == 'bob':
            di.image = Surface((60, 100))
            di.image = image.load('textures/dino.png')
            di.direct = 'stay'
            di.rect = Rect(di.rect.x, di.rect.y - 50, 60, 100)


            
        if e.type == KEYDOWN and e.key == K_f:
            obj_group.remove(di)
            objects.remove(di)
            del(di)
            di = dino(100, 60, '', 200, 600, 10 )
            obj_group.add(di)
            objects.append(di)
            score = 0
            scorepoint = 1000
            stone_speed = 15
            pter_speed = 20
            for en in enemies:
                obj_group.remove(en)
            enemies.clear()
            di.direct = 'stay'
            
    screen.blit(background, (0,0))
    if score > scorepoint:
        stone_speed += 3
        pter_speed += 3
        scorepoint += 400
        
    if di.direct not in ['endgame', 'victory']:
        score += 2
    score_text = score_f.render('Score: {0}'.format(score), True, (0,0,0) )
    
    if score > 10000:
        di.direct = 'victory'
        
    if di.direct == 'endgame':
        for en in enemies:
            en.speed = 0
        screen.blit(end_text, (420, 200))

    if di.direct == 'victory':
        for en in enemies:
            en.speed = 0
        screen.blit(v_text, (420, 200))
        
    if len(enemies) == 0: #Если нет врагов
        if random.randint(0, 1) == 0: #Случайная генерация врагов
            enemies.append(cactus.cactus(stone_speed))
        else:
            enemies.append(pter.pterodactile(pter_speed))        
        obj_group.add(enemies[0])

    if enemies[0].rect.x < 500 and len(enemies) == 1:
        if random.randint(0, 1) == 0: #Случайная генерация врагов
            enemies.append(cactus.cactus(stone_speed))
        else:
            enemies.append(pter.pterodactile(pter_speed))        
        obj_group.add(enemies[1])

               
    for en in enemies:
        if en.rect.x <= -50:
            enemies.remove(en)
            obj_group.remove(en)
        en.update() #обновляем положение каждого варага
    for obj in objects:
        obj.update(fl, enemies)

        
    obj_group.draw(screen)
    screen.blit(score_text, (900, 30))
    
    pygame.display.update()
    time.sleep(0.01)
