import pygame
from pygame.draw import rect
from pygame.locals import *

class Item:

    def __init__(self, name, image, type, property, scale, imageR = None, imageL = None, imageF = None, imageB = None):
        self.name = name
        self.preimage = image
        self.image = pygame.transform.scale(image, scale)
        self.rect = self.image.get_rect()
        self.backpackimage = pygame.transform.scale(image, (20, 50))
        self.backpackrect = self.backpackimage.get_rect()
        self.type = type
        self.scale = scale
        self.property = property
        self.currentimage = image
        self.currentrect = self.rect
        self.found = False
        if self.type == 'weapon':
            self.rightside = pygame.transform.scale(imageR, (100, 40))
            self.rightrect = self.rightside.get_rect()
            self.leftside = pygame.transform.scale(imageL, (100, 40))
            self.leftrect = self.leftside.get_rect()
            self.frontside = pygame.transform.scale(imageF, (40, 100))
            self.frontrect = self.frontside.get_rect()
            self.backside = pygame.transform.scale(imageB, (40, 100))
            self.backrect = self.backside.get_rect()
        else:
            self.rightside = None
            self.rightrect = None
            self.leftside = None
            self.leftrect = None
            self.frontside = None
            self.frontrect = None
            self.backside = None
            self.backrect = None
    
    def determineCraftables(self, dict):
        craftables = []
        crafts = []
        for things in dict:
            if things['item'].type == 'craft':
                crafts.append(things)
        # need way to import craftable items (maybe put this method in player class)
        wood_count = 0
        tooth = 0
        blade = 0
        beaconable = 0 
        for thing in crafts:
            if thing['item'].name == "Wood":
                wood_count = thing['item'].quantity
            elif thing['item'].name == "Loose Tooth":
                tooth = 1
            elif thing['item'].name == "Blade Fragments":
                blade = 1
            else:
                beaconable += 1
        # weapon checker
        if wood_count >= 5 and tooth == 1:
            craftables.append()
        # beacon checker
        return craftables
    
    def copy(self):
        return self.name, self.preimage, self.type, self.property, self.scale, self.rightside, self.leftside, self.frontside, self.backside
