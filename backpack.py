import pygame
from pygame import *

class Backpack:
    # images
    background = "ArtAssets/menus/BPbackground.png"
    emptyslot = "ArtAssets/menus/BPemptyslot.png"
    selected = "ArtAssets/menus/BPselected.png"

    # maybe keep backpack framework in this class but keep track of player inventory within player class and simply display the info in this class
    def __init__(self):
        background = Backpack.background
        emptyslot = Backpack.emptyslot
        selected = Backpack.selected

        self.backgroundimage = pygame.transform.scale(pygame.image.load(background), (800, 700))
        self.backgroundrect = self.backgroundimage.get_rect()
        self.backgroundrect.center = (650, 500)

        # self.live_items = [] # basically holds player inv except equipped item

        self.slotscale = (100, 100)
        
        self.emptyslot0 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot1 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot2 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot3 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot4 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot0rect = self.emptyslot0.get_rect()
        self.emptyslot1rect = self.emptyslot1.get_rect()
        self.emptyslot2rect = self.emptyslot2.get_rect()
        self.emptyslot3rect = self.emptyslot3.get_rect()
        self.emptyslot4rect = self.emptyslot4.get_rect()
        self.row1 = [self.emptyslot0rect, self.emptyslot1rect, self.emptyslot2rect, self.emptyslot3rect, self.emptyslot4rect]

        self.emptyslot5 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot6 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot7 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot8 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot9 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot5rect = self.emptyslot5.get_rect()
        self.emptyslot6rect = self.emptyslot6.get_rect()
        self.emptyslot7rect = self.emptyslot7.get_rect()
        self.emptyslot8rect = self.emptyslot8.get_rect()
        self.emptyslot9rect = self.emptyslot9.get_rect()
        self.row2 = [self.emptyslot5rect, self.emptyslot6rect, self.emptyslot7rect, self.emptyslot8rect, self.emptyslot9rect]
        
        self.emptyslot10 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot11 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot12 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot13 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot14 = pygame.transform.scale(pygame.image.load(emptyslot), self.slotscale)
        self.emptyslot10rect = self.emptyslot10.get_rect()
        self.emptyslot11rect = self.emptyslot11.get_rect()
        self.emptyslot12rect = self.emptyslot12.get_rect()
        self.emptyslot13rect = self.emptyslot13.get_rect()
        self.emptyslot14rect = self.emptyslot14.get_rect()
        self.row3 = [self.emptyslot10rect, self.emptyslot11rect, self.emptyslot12rect, self.emptyslot13rect, self.emptyslot14rect]
        
        self.selecteditem = False
        self.selected = pygame.transform.scale(pygame.image.load(selected), self.slotscale)
        self.selectedrect = self.selected.get_rect()
        self.selectedIndex = 20
        
        self.allslots = [self.emptyslot0, self.emptyslot1, self.emptyslot2, self.emptyslot3, self.emptyslot4, self.emptyslot5, self.emptyslot6, self.emptyslot7, self.emptyslot8, self.emptyslot9, self.emptyslot10, self.emptyslot11, self.emptyslot12, self.emptyslot13, self.emptyslot14]
        self.allslotsrects = [self.emptyslot0rect, self.emptyslot1rect, self.emptyslot2rect, self.emptyslot3rect, self.emptyslot4rect, self.emptyslot5rect, self.emptyslot6rect, self.emptyslot7rect, self.emptyslot8rect, self.emptyslot9rect, self.emptyslot10rect, self.emptyslot11rect, self.emptyslot12rect, self.emptyslot13rect, self.emptyslot14rect]

        self.setupSlots()

    def setupSlots(self):
        increment = 100
        startposx = 375
        currentposx = 375
        row1y = 330
        row2y = 475
        row3y = 650
        for slot in self.row1:
            slot.center = (currentposx, row1y)
            currentposx += increment
        currentposx = startposx
        for slot in self.row2:
            slot.center = (currentposx, row2y)
            currentposx += increment
        currentposx = startposx
        for slot in self.row3:
            slot.center = (currentposx, row3y)
            currentposx += increment
        self.selectedrect.center = (917, 330)

    def addItem(self, item):
        return
    
    def removeItem(self, item):
        return

