# -*- coding:utf-8 -*-
# 1 import library
import pygame
import math
import random
from pygame.locals import*

# 2 initialize the game
pygame.init()
pygame.mixer.init()
width,height = 500,500                                  #定义整个游戏边框的宽和高
screen = pygame.display.set_mode((width,height))
keys = [False, False, False, False]                     #设置WASD初始状态是松开
pacmanposx = 0                                          #定义pacman初始x坐标
pacmanposy = 0                                          #定义pacman初始y坐标
monsters = [[150,150],[350,350],[225,225]]  #monster1和monster2的初始位置
hp = 22              #22值HP
count0 = 0                                              #每一次while，count0+1，使得pacman和monster动起来
pos0 = (random.randint(50,450),random.randint(50,450))  #设置bean0-4的随机位置
pos1 = (random.randint(50,450),random.randint(50,450))
pos2 = (random.randint(50,450),random.randint(50,450))
pos3 = (random.randint(50,450),random.randint(50,450))
pos4 = (random.randint(50,450),random.randint(50,450))
pos5 = (random.randint(50,450),random.randint(50,450))
pos6 = (random.randint(50,450),random.randint(50,450))
beans = [pos0,pos1,pos2,pos3,pos4,pos5,pos6]
score = 0   
isCollide0 = 0
isCollide1 = 0
isCollide2 = 0
isCollide3 = 0
isCollide4 = 0
isCollide5 = 0
isCollide6 = 0

# 3 load images
background = pygame.image.load("resources/images/background.png")     #灰色背景
eatright = pygame.image.load("resources/images/pacmaneatright.png")       #开口pacman（吃豆人）
eatleft = pygame.image.load("resources/images/pacmaneatleft.png")       #开口pacman（吃豆人）
eatup = pygame.image.load("resources/images/pacmaneatup.png")       #开口pacman（吃豆人）
eatdown = pygame.image.load("resources/images/pacmaneatdown.png")       #开口pacman（吃豆人）
closeright = pygame.image.load("resources/images/pacmancloseright.png")   #闭口pacman
closeleft = pygame.image.load("resources/images/pacmancloseleft.png")   #闭口pacman
closeup = pygame.image.load("resources/images/pacmancloseup.png")       #开口pacman（吃豆人）
closedown = pygame.image.load("resources/images/pacmanclosedown.png")       #开口pacman（吃豆人）
monster01 = pygame.image.load("resources/images/monster01.png")       #动态1 monster（怪物）
monster02 = pygame.image.load("resources/images/monster02.png")       #动态2 monster
bean = pygame.image.load("resources/images/bean.png")               #5种不同颜色的bean（豆子）
win = pygame.image.load("resources/images/win.png")
lose = pygame.image.load("resources/images/lose.png")


# 3.1 load music
pygame.mixer.music.load("resources/audio/1.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(1)

# 4 keep looping through
running = 1
exitcode = 0
pacmaneat = eatright
pacmanclose = closeright
while running:
    count0 += 1

    # 5 clear the screen before drawing it again
    screen.fill(0)

    # 6 draw the screen elements
    
    # 6.1 draw background
    screen.blit(background, (0,0))

    # 6.2 draw pacman             
    if count0 % 2 == 0:
        screen.blit(pacmanclose, (pacmanposx,pacmanposy))
    else:
        screen.blit(pacmaneat, (pacmanposx,pacmanposy))

    # 6.3 draw beans
    screen.blit(bean, beans[0])
    screen.blit(bean, beans[1])
    screen.blit(bean, beans[2])
    screen.blit(bean, beans[3])
    screen.blit(bean, beans[4])
    screen.blit(bean, beans[5])
    screen.blit(bean, beans[6])

    
    # 6.4 draw monsters
    speedmon = 70    #monster移动速度
    for monster in monsters:
        if count0 % 128 == random.randint(0,33):          #count0除以128余数为[0,32]，monster向右移动
                monster[0] += speedmon
        elif count0 % 128 == random.randint(33,65):       #count0除以128余数为[33,64]，monster向上移动
                monster[1] -= speedmon
        elif count0 % 128 == random.randint(65,97):       #count0除以128余数为[64,96]，monster向左移动
                monster[0] -= speedmon
        elif count0 % 128 == random.randint(97,128):      #count0除以128余数为[97,127]，monster向下移动
                monster[1] += speedmon
        if monster[0] < 100:        #如果x<100，停留在横坐标50的位置
            monster[0] = 50
        if monster[0] > 400:        #如果x>400，停留在横坐标400的位置
            monster[0] = 400
        if monster[1] < 100:        #如果y<100，停留在纵坐标50的位置
            monster[1] = 50
        if monster[1] > 400:        #如果y>400，停留在纵坐标400的位置
            monster[1] = 400
        if count0%2 == 0:                          #画动态monster的动态位置(更改除数可改变动态频率，负相关)
            screen.blit(monster01, monster)
        else:
            screen.blit(monster02, monster)

    # 6.5 check for pacman and monster's collisions
    pacrect = pygame.Rect(pacmanclose.get_rect())
    pacrect.left = pacmanposx
    pacrect.top = pacmanposy
    for monster in monsters:
        monrect1 = pygame.Rect(monster01.get_rect())
        monrect1.left = monster[0]
        monrect1.top = monster[1]
        monrect2 = pygame.Rect(monster02.get_rect())
        monrect2.left = monster[0]
        monrect2.top = monster[1]
        if monrect1.colliderect(pacrect) and monrect2.colliderect(pacrect):
            hp -= 1
       
    # 6.6 check for pacman eating bean:
    bean0rect = pygame.Rect(bean.get_rect())
    bean0rect.left = pos0[0]
    bean0rect.top = pos0[1]
    if bean0rect.colliderect(pacrect) and isCollide0 == 0:
        isCollide0 = 1
        beans[0] = (-30,-30)
        score += 1
        
    bean1rect = pygame.Rect(bean.get_rect())
    bean1rect.left = pos1[0]
    bean1rect.top = pos1[1]
    if bean1rect.colliderect(pacrect) and isCollide1 == 0:
        isCollide1 = 1
        beans[1] = (-30,-30)
        score += 1
        
    bean2rect = pygame.Rect(bean.get_rect())
    bean2rect.left = pos2[0]
    bean2rect.top = pos2[1]
    if bean2rect.colliderect(pacrect) and isCollide2 == 0:
        isCollide2 = 1
        beans[2] = (-30,-30)
        score += 1
        
    bean3rect = pygame.Rect(bean.get_rect())
    bean3rect.left = pos3[0]
    bean3rect.top = pos3[1]
    if bean3rect.colliderect(pacrect) and isCollide3 == 0:
        isCollide3 = 1
        beans[3] = (-30,-30)
        score += 1
        
    bean4rect = pygame.Rect(bean.get_rect())
    bean4rect.left = pos4[0]
    bean4rect.top = pos4[1]
    if bean4rect.colliderect(pacrect) and isCollide4 == 0:
        isCollide4 = 1
        beans[4] = (-30,-30)
        score += 1
        
    bean5rect = pygame.Rect(bean.get_rect())
    bean5rect.left = pos5[0]
    bean5rect.top = pos5[1]
    if bean5rect.colliderect(pacrect) and isCollide5 == 0:
        isCollide5 = 1
        beans[5] = (-30,-30)
        score += 1
        
    bean6rect = pygame.Rect(bean.get_rect())
    bean6rect.left = pos6[0]
    bean6rect.top = pos6[1]
    if bean6rect.colliderect(pacrect) and isCollide6 == 0:
        isCollide6 = 1
        beans[6] = (-30,-30)
        score += 1

    # 6.8 draw life    #右上角画HP值
    pygame.font.init()
    font = pygame.font.Font(None, 30)
    lifetext = font.render("HP"+" "+str(hp).zfill(1),True,(232,232,232))   
    lifetextRect = lifetext.get_rect()
    lifetextRect.topright = [490,10]
    screen.blit(lifetext,lifetextRect)

    # 7 update the screen
    pygame.display.flip()

    # 8 loop through the events
    for event in pygame.event.get():
        
        # 8.1 check for quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            SystemExit(0)

        # 8.2 move pacman
        if event.type == pygame.KEYDOWN:        #定义按下WASD时移动pacman
            if event.key == pygame.K_w:
                pacmaneat = eatup
                pacmanclose = closeup
                keys[0] = True
            elif event.key == pygame.K_a:
                pacmaneat = eatleft
                pacmanclose = closeleft
                keys[1] = True
            elif event.key == pygame.K_s:
                pacmaneat = eatdown
                pacmanclose = closedown
                keys[2] = True
            elif event.key == pygame.K_d:
                pacmaneat = eatright
                pacmanclose = closeright
                keys[3] = True
            if event.key == pygame.K_F7:
                pygame.mixer.music.set_volume(0)
            if event.key == pygame.K_F8:
                pygame.mixer.music.set_volume(1)
        if event.type == pygame.KEYUP:          #定义松开WASD时停止移动pacman
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    # 9 Move pacman
    speedpac = 3                  #速度初始值，方便更改pacman移动快慢
    if keys[0]:                      #按W键pacman不可以向上超过边框
        if pacmanposy - 5 > 0:
            pacmanposy -= speedpac
        elif pacmanposy -5 < 0:
            pacmanposy = 0
    elif keys[2]:                    #按S键pacman不可以向下超过边框
        if pacmanposy - 450 < 0:
            pacmanposy += speedpac
        elif pacmanposy - 450 > 0:
            pacmanposy = 450
    if keys[1]:                      #按A键pacman不可以向左超过边框
        if pacmanposx - 5 > 0:
            pacmanposx -= speedpac
        elif pacmanposx - 5 < 0:
            pacmanposx = 0
    elif keys[3]:                    #按D键pacman不可以向右超过边框
        if pacmanposx - 450 < 0:
            pacmanposx += speedpac
        elif pacmanposx - 450 < 0:
            pacmanposx = 450

    # 10 win/lose check
    if score == 7:    #全部豆豆被吃掉就exitcode=1，赢
        running = 0
        exitcode = 1
    if hp <= 0:         #hp减到小于零就exitcode=0,输
        running = 0
        exitcode = 0

# 11 win/lose display
if exitcode == 0:
    pygame.mixer.music.set_volume(0)
    font = pygame.font.Font(None,40)
    losescoretext = font.render("Score:"+str(score),True,(255,0,0))
    losescoretextRect = losescoretext.get_rect()
    losescoretextRect.centerx = screen.get_rect().centerx-10
    losescoretextRect.centery = screen.get_rect().centery+40
    losetimetext = font.render("Time"+" "+str(pygame.time.get_ticks()/60000)+":"+str(pygame.time.get_ticks()/1000%60).zfill(2),True,(255,0,0))
    losetimetextRect = losetimetext.get_rect()
    losetimetextRect.centerx = screen.get_rect().centerx-10
    losetimetextRect.centery = screen.get_rect().centery+5
    screen.blit(lose,(0,0))
    screen.blit(losetimetext,losetimetextRect)
    screen.blit(losescoretext,losescoretextRect)
if exitcode == 1:
    pygame.mixer.music.set_volume(0)
    font = pygame.font.Font(None,40)
    winscoretext = font.render("Score:"+str(score),True,(255,126,0))
    winscoretextRect = winscoretext.get_rect()
    winscoretextRect.centerx = screen.get_rect().centerx-10
    winscoretextRect.centery = screen.get_rect().centery+40
    wintimetext = font.render("Time"+" "+str(pygame.time.get_ticks()/60000)+":"+str(pygame.time.get_ticks()/1000%60).zfill(2),True,(255,126,0))
    wintimetextRect = wintimetext.get_rect()
    wintimetextRect.centerx = screen.get_rect().centerx-10
    wintimetextRect.centery = screen.get_rect().centery+5
    screen.blit(win,(0,0))
    screen.blit(wintimetext,wintimetextRect)
    screen.blit(winscoretext,winscoretextRect)

# 12 exit
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            SystemExit(0)
        pygame.display.flip()
        

