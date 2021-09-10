import pygame
from pygame.locals import *

class Player:

    def __init__(self, speed, windowWidth, windowHeight, inventory, scale, hp):
        self.instantiateImages(scale)
        self.currentImage = self.FS_image
        self.rect = self.currentImage.get_rect()
        self.speed = speed
        self.upLimit = 0
        self.WINDOWWIDTH = windowWidth
        self.WINDOWHEIGHT = windowHeight
        self.downLimit = windowHeight
        self.leftLimit = 0
        self.rightLimit = windowWidth
        self.setStartPos()
        self.inventory = inventory #format: list of {'item': item object, 'quantity': int count}
        # might have to create seperate inventory for backpack and for real life
        self.hp = hp
        self.maxhp = hp
        self.equipped = {'item': None, 'quantity': 0}
    
    def instantiateImages(self, scale):
        # front face
        self.FS_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/frontstillMAIN.png'), scale)
        self.FW_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/frontwalkMAIN.png'), scale)
        self.FA_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/frontattackMAIN.png'), scale)
        # left face 
        self.LS_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/leftstillMAIN.png'), scale)
        self.LW_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/leftwalkMAIN.png'), scale)
        self.LA_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/leftattackMAIN.png'), scale)
        # back face
        self.BS_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/backstillMAIN.png'), scale)
        self.BW_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/backwalkMAIN.png'), scale)
        self.BA_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/backattackMAIN.png'), scale)
        # right face
        self.RS_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/rightstillMAIN.png'), scale)
        self.RW_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/rightwalkMAIN.png'), scale)
        self.RA_image = pygame.transform.scale(pygame.image.load('ArtAssets/character/rightattackMAIN.png'), scale)

        
    def updatePicture(self, up, down, left, right, attacking , i):

        # include walking images sometime somehow 
        if i < 30:
            # still image 
            if attacking:
                if up:
                    self.currentImage = self.BA_image
                elif down:
                    self.currentImage = self.FA_image
                elif right:
                    self.currentImage = self.RA_image
                elif left:
                    self.currentImage = self.LA_image
                else:
                    # if player is not moving but wants to attack
                    if self.currentImage == self.BS_image or self.currentImage == self.BW_image:
                        self.currentImage = self.BA_image
                    elif self.currentImage == self.FS_image or self.currentImage == self.FW_image:
                        self.currentImage = self.FA_image
                    elif self.currentImage == self.RS_image or self.currentImage == self.RW_image:
                        self.currentImage = self.RA_image
                    elif self.currentImage == self.LS_image or self.currentImage == self.LW_image:
                        self.currentImage = self.LA_image
            elif not attacking:
                if up:
                    self.currentImage = self.BS_image
                elif down:
                    self.currentImage = self.FS_image
                elif right:
                    self.currentImage = self.RS_image
                elif left:
                    self.currentImage = self.LS_image
                else:
                    # player done attacking but staying still
                    if self.currentImage == self.BA_image:
                        self.currentImage = self.BS_image
                    elif self.currentImage == self.FA_image:
                        self.currentImage = self.FS_image
                    elif self.currentImage == self.RA_image:
                        self.currentImage = self.RS_image
                    elif self.currentImage == self.LA_image:
                        self.currentImage = self.LS_image
        else:
            # walking image
            if attacking:
                # attack in a direction
                if up:
                    self.currentImage = self.BA_image
                elif down:
                    self.currentImage = self.FA_image
                elif right:
                    self.currentImage = self.RA_image
                elif left:
                    self.currentImage = self.LA_image
                else:
                    # if player is not moving but wants to attack
                    if self.currentImage == self.BS_image or self.currentImage == self.BW_image:
                        self.currentImage = self.BA_image
                    elif self.currentImage == self.FS_image or self.currentImage == self.FW_image:
                        self.currentImage = self.FA_image
                    elif self.currentImage == self.RS_image or self.currentImage == self.RW_image:
                        self.currentImage = self.RA_image
                    elif self.currentImage == self.LS_image or self.currentImage == self.LW_image:
                        self.currentImage = self.LA_image
            elif not attacking:
                if up:
                    self.currentImage = self.BW_image
                elif down:
                    self.currentImage = self.FW_image
                elif right:
                    self.currentImage = self.RW_image
                elif left:
                    self.currentImage = self.LW_image
                else:
                    # player done attacking but staying still
                    if self.currentImage == self.BA_image:
                        self.currentImage = self.BS_image
                    elif self.currentImage == self.FA_image:
                        self.currentImage = self.FS_image
                    elif self.currentImage == self.RA_image:
                        self.currentImage = self.RS_image
                    elif self.currentImage == self.LA_image:
                        self.currentImage = self.LS_image
        if self.equipped['quantity'] != 0:
            if self.equipped['item'].type == 'weapon':
                if attacking:
                    distanceconstant = 150
                    if self.currentImage == self.BA_image:
                        self.equipped['item'].currentrect = self.equipped['item'].backrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 35, self.rect.centery - distanceconstant)
                        self.equipped['item'].currentimage = self.equipped['item'].backside
                    elif self.currentImage == self.FA_image:
                        self.equipped['item'].currentrect = self.equipped['item'].frontrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx - 30, self.rect.centery + distanceconstant)
                        self.equipped['item'].currentimage = self.equipped['item'].frontside
                    elif self.currentImage == self.LA_image:
                        self.equipped['item'].currentrect = self.equipped['item'].leftrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx - distanceconstant, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].leftside
                    elif self.currentImage == self.RA_image:
                        self.equipped['item'].currentrect = self.equipped['item'].rightrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx + distanceconstant, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].rightside
                else:
                    if self.currentImage == self.BS_image or self.currentImage == self.BW_image:
                        self.equipped['item'].currentrect = self.equipped['item'].backrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 35, self.rect.centery - 50)
                        self.equipped['item'].currentimage = self.equipped['item'].backside
                    elif self.currentImage == self.FS_image or self.currentImage == self.FW_image:
                        self.equipped['item'].currentrect = self.equipped['item'].frontrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx - 30, self.rect.centery + 50)
                        self.equipped['item'].currentimage = self.equipped['item'].frontside
                    elif self.currentImage == self.LS_image or self.currentImage == self.LW_image:
                        self.equipped['item'].currentrect = self.equipped['item'].leftrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx - 75, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].leftside
                    elif self.currentImage == self.RS_image or self.currentImage == self.RW_image:
                        self.equipped['item'].currentrect = self.equipped['item'].rightrect
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 75, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].rightside
            else:
                if attacking:
                    if self.currentImage == self.BA_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 100, self.rect.centery - 100)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                    elif self.currentImage == self.FA_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 10, self.rect.centery + 100)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                    elif self.currentImage == self.LA_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx - 50, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                    elif self.currentImage == self.RA_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 130, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                else:
                # need still and attacking equipped item positions
                    if self.currentImage == self.BS_image or self.currentImage == self.BW_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 100, self.rect.centery - 40)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                    elif self.currentImage == self.FS_image or self.currentImage == self.FW_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 10, self.rect.centery + 40)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                    elif self.currentImage == self.LS_image or self.currentImage == self.LW_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 10, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage
                    elif self.currentImage == self.RS_image or self.currentImage == self.RW_image:
                        self.equipped['item'].currentrect.center = (self.rect.centerx + 70, self.rect.centery + 20)
                        self.equipped['item'].currentimage = self.equipped['item'].backpackimage

    def move(self, up, down, left, right, walls):
        # collision = pygame.Rect.collidelist(walls)
        tempRect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        if up:
            tempRect.centery -= self.speed
        if down:
            tempRect.centery += self.speed
        if right:
            tempRect.centerx += self.speed
        if left:
            tempRect.centerx -= self.speed
        collision = -1
        for i in range(len(walls)):
            if tempRect.colliderect(walls[i].rect):
                collision = i
                # print("collided with wall")
        if collision != -1:
            return
            """
            # if there is a collision
            orient = walls[collision].orient
            collided = walls[collision].rect
            if orient == 0:
                # horizontal wall
                if collided.centery < self.rect.centery:
                    # collided is above self
                    if up:
                        return
                elif collided.centery > self.rect.centery:
                    # collided is below self
                    if down:
                        return
            elif orient == 1:
                # vertical wall
                if collided.centerx < self.rect.centerx:
                    # collided is to left of self
                    if left:
                        return
                elif collided.centerx > self.rect.centerx:
                    # collided is to right of self
                    if right:
                        return
            """
            
        if up and right and self.rect.top > self.upLimit and self.rect.right < self.rightLimit:
            self.rect.center = (self.rect.centerx + self.speed, self.rect.centery - self.speed)
            return
        if up and left and self.rect.top > self.upLimit and self.rect.left > self.leftLimit:
            self.rect.center = (self.rect.centerx - self.speed, self.rect.centery - self.speed)
            return
        if down and left and self.rect.bottom < self.downLimit and self.rect.left > self.leftLimit:
            self.rect.center = (self.rect.centerx - self.speed, self.rect.centery + self.speed)
            return
        if down and right and self.rect.bottom < self.downLimit and self.rect.right < self.rightLimit:
            self.rect.center = (self.rect.centerx + self.speed, self.rect.centery + self.speed)
            return
        if up and self.rect.top > self.upLimit:
            self.rect.top -= self.speed
        if left and self.rect.left > self.leftLimit:
            self.rect.left -= self.speed
        if right and self.rect.right < self.rightLimit:
            self.rect.right += self.speed
        if down and self.rect.bottom < self.downLimit:
            self.rect.bottom += self.speed
    
    def dash(self, up, down, left, right, walls):
        if not up and not down and not left and not right:
            if self.currentImage == self.BA_image or self.currentImage == self.BS_image or self.currentImage == self.BW_image:
                up = True
            elif self.currentImage == self.FA_image or self.currentImage == self.FS_image or self.currentImage == self.FW_image:
                down = True
            elif self.currentImage == self.LA_image or self.currentImage == self.LS_image or self.currentImage == self.LW_image:
                left = True
            elif self.currentImage == self.RA_image or self.currentImage == self.RS_image or self.currentImage == self.RW_image:
                right = True
        for i in range(5):
            self.move(up, down, left, right, walls)

    def setStartPos(self):
        self.rect.center = (self.WINDOWWIDTH / 2, self.WINDOWHEIGHT / 2)
    
    def determineCraftables(self):
        # used to load up crafting menu with what is possible to craft and how many of different ingredients is needed
        return