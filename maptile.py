import pygame
from pygame.locals import *
import numpy as np

from item import Item


class Maptile:

    # add something for spawning things (wood, fish, animals)
    def __init__(self, name, connections, resolution, image, speed, inventory, live_items, utilities, walls = [], monsters = None):
        self.name = name
        self.image = pygame.transform.scale(image, resolution)
        self.rect = self.image.get_rect()
        self.up = connections[0]
        self.down = connections[1]
        self.left = connections[2]
        self.right = connections[3]
        self.speed = speed # for tile shifting // irrelavent now
        self.inventory = inventory
        self.live_items = live_items
        self.utilities = utilities
        self.walls = walls
        self.monsters = monsters
        self.generateItems()
    
    def move(self, direction):
        if direction == "up":
            self.rect.top -= self.speed
        elif direction == "down":
            self.rect.top += self.speed
        elif direction == "right":
            self.rect.left += self.speed
        elif direction == 'left':
            self.rect.left -= self.speed
    
    def generateItems(self):
        for allowed in self.inventory:
            if allowed.found == False:
                n, i, t, p, s, r, l, f, b = allowed.copy()
                item = Item(n, i, t, p, s, r, l, f, b)
                self.live_items.append(item) 
        for thing in self.live_items:
            # if thing is this item or this item or whatever
            thing.rect.midtop = (np.random.randint(10, 1300 - 10), np.random.randint(10, 1000 - 10))
            for wall in self.walls:
                while True:
                    collided = False
                    if thing.rect.colliderect(wall.rect):
                        collided = True
                    if collided:
                        thing.rect.midtop = (np.random.randint(10, 1300 - 10), np.random.randint(10, 1000 - 10))
                        continue
                    else:
                        break
    
    def clearItems(self):
        self.live_items = []
                
    def initializeObjects(self, num):
        objects = []
        for i in range(num):
            objects.append(None)
        return objects
    