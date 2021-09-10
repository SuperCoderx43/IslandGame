import pygame
from pygame.locals import *
import numpy as np

class Monster:

    def __init__(self, name, sl_image, sr_image, al_image, ar_image, scale, health, attacks, music, behavior, coords, speed, jumpspeed, loot = None):
        self.name = name
        
        self.sl_image = pygame.transform.scale(pygame.image.load(sl_image), scale)
        self.al_image = pygame.transform.scale(pygame.image.load(al_image), scale)
        self.sr_image = pygame.transform.scale(pygame.image.load(sr_image), scale)
        self.ar_image = pygame.transform.scale(pygame.image.load(ar_image), scale)

        self.currentImage = self.sl_image
        self.rect = self.currentImage.get_rect()
        self.health = health
        self.maxhealth = health
        self.attacks = attacks
        self.music = music
        self.attackable = False
        self.behavior = behavior

        self.coords = coords
        self.rect.center = (coords[0], coords[1])
        self.speed = speed
        self.jumpspeed = jumpspeed

        self.xdirs = ['l', 'r']
        self.ydirs = ['u', 'd']
        self.xdir = self.xdirs[np.random.randint(0, len(self.xdirs))]
        self.ydir = self.ydirs[np.random.randint(0, len(self.ydirs))]

        self.temp = True
        self.inmotion = False

        self.attackspot = (0,0)
        self.attacking = False
        self.alive = True
        self.loot = loot

        self.upLimit = 0
        self.downLimit = 1000
        self.leftLimit = 0
        self.rightLimit = 1300

    def updateImage(self):
        if self.attacking:
            if self.xdir == 'r':
                self.currentImage = self.ar_image
            elif self.xdir == 'l':
                self.currentImage = self.al_image
        else:
            if self.xdir == 'r':
                self.currentImage = self.sr_image
            elif self.xdir == 'l':
                self.currentImage = self.sl_image

    def move(self, currentTile, player, speed = 0):
        if speed == 0:
            speed = self.jumpspeed
        playerRect = player.rect
        if self.behavior == 'rabid':
            # if player is close to monster
            
            if np.sqrt((self.rect.centerx - playerRect.centerx)**2) <= 300 and np.sqrt((self.rect.centery - playerRect.centery)**2) <= 300:
                if self.xdir == 'l':
                    if playerRect.centerx < self.rect.centerx:
                        self.attacking = True
                    else:
                        self.attacking = False
                elif self.xdir == 'r':
                    if playerRect.centerx > self.rect.centerx:
                        self.attacking = True
                    else:
                        self.attacking = False
            else:
                self.attacking = False

            # move in diagonals up and down on the screen
            tempRect = self.rect
            moveable = True
            yconstant = 3
            if self.xdir == 'r':
                if self.ydir == 'd':
                    tempRect.centerx += speed
                    tempRect.centery += yconstant
                    for wall in currentTile.walls:
                        if tempRect.colliderect(wall.rect):
                            moveable = False
                            if self.temp: 
                                self.xdir = 'l'
                                self.temp = False
                            else: 
                                self.ydir = 'u'
                                self.temp = True
                            break
                    if tempRect.top <= self.upLimit or tempRect.left <= self.leftLimit or tempRect.right >= self.rightLimit or tempRect.bottom >= self.downLimit:
                        moveable = False
                        if self.temp: 
                            self.xdir = 'l'
                            self.temp = False
                        else: 
                            self.ydir = 'u'
                            self.temp = True
                elif self.ydir == 'u':
                    tempRect.centerx += speed
                    tempRect.centery -= yconstant
                    for wall in currentTile.walls:
                        if tempRect.colliderect(wall.rect):
                            moveable = False
                            if self.temp: 
                                self.xdir = 'l'
                                self.temp = False
                            else: 
                                self.ydir = 'd'
                                self.temp = True
                            break
                    if tempRect.top <= self.upLimit or tempRect.left <= self.leftLimit or tempRect.right >= self.rightLimit or tempRect.bottom >= self.downLimit:
                        moveable = False
                        if self.temp: 
                            self.xdir = 'l'
                            self.temp = False
                        else: 
                            self.ydir = 'd'
                            self.temp = True
            elif self.xdir == 'l':
                if self.ydir == 'd':
                    tempRect.centerx -= speed
                    tempRect.centery += yconstant
                    for wall in currentTile.walls:
                        if tempRect.colliderect(wall.rect):
                            moveable = False
                            if self.temp: 
                                self.xdir = 'r'
                                self.temp = False
                            else: 
                                self.ydir = 'u'
                                self.temp = True
                            break
                    if tempRect.top <= self.upLimit or tempRect.left <= self.leftLimit or tempRect.right >= self.rightLimit or tempRect.bottom >= self.downLimit:
                        moveable = False
                        if self.temp: 
                            self.xdir = 'r'
                            self.temp = False
                        else: 
                            self.ydir = 'u'
                            self.temp = True
                elif self.ydir == 'u':
                    tempRect.centerx -= speed
                    tempRect.centery -= yconstant
                    for wall in currentTile.walls:
                        if tempRect.colliderect(wall.rect):
                            moveable = False
                            if self.temp: 
                                self.xdir = 'r'
                                self.temp = False
                            else: 
                                self.ydir = 'd'
                                self.temp = True
                            break
                    if tempRect.top <= self.upLimit or tempRect.left <= self.leftLimit or tempRect.right >= self.rightLimit or tempRect.bottom >= self.downLimit:
                        moveable = False
                        if self.temp: 
                            self.xdir = 'r'
                            self.temp = False
                        else: 
                            self.ydir = 'd'
                            self.temp = True
            if moveable:
                self.updateImage()
                self.rect = tempRect
    
    def playerDetection(self, player):
        playerRect = player.rect
        if self.attacking:
            if np.sqrt((self.rect.centerx - playerRect.centerx)**2) <= 150 and np.sqrt((self.rect.centery - playerRect.centery)**2) <= 150:
                return
            # use attack dictionaries to get the current attack being used and apply the damage to player


    def rabidAttack(self, playerRect):
        moveable = True
        tempRect = self.rect
        self.attacking = True
        if not self.inmotion:
            self.attackspot = (playerRect.centerx, playerRect.centery)
            self.inmotion = True
        if self.attackspot[0] > self.rect.centerx:
            self.currentImage = self.ar_image
            self.xdir = 'r'
        elif self.attackspot[0] < self.rect.centerx:
            self.currentImage = self.al_image
            self.xdir = 'l'
        if self.xdir == 'r':
            print("attacking right!")
            tempRect.centerx += self.jumpspeed
            if self.attackspot[1] < self.rect.centery:
                tempRect.centery -= self.jumpspeed / 2
            elif self.attackspot[1] > self.rect.centery:
                tempRect.centery += self.jumpspeed / 2
            if self.attackspot[0] < self.rect.centerx:
                self.xdir = 'l'
                self.attacking = False
                self.updateImage()
                self.inmotion = False
        elif self.xdir == 'l':
            print("attacking left!")
            tempRect.centerx -= self.jumpspeed
            if self.attackspot[1] < self.rect.centery:
                tempRect.centery -= self.jumpspeed / 2
            elif self.attackspot[1] > self.rect.centery:
                tempRect.centery += self.jumpspeed / 2
            if self.attackspot[0] > self.rect.centerx:
                self.xdir = 'r'
                self.attacking = False
                self.updateImage()
                self.inmotion = False
        if tempRect.top <= self.upLimit + 100 or tempRect.left <= self.leftLimit + 100 or tempRect.right >= self.rightLimit - 100 or tempRect.bottom >= self.downLimit - 100:
            moveable = False
            print("situation B")
        if moveable:
            self.rect = tempRect
    
    def setStartPos(self):
        self.rect.center = self.coords
    
    
        

                

