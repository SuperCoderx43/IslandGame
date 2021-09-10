import pygame
from pygame.locals import *

class Weapon:

    def __init__(self, name, damage, image, scale):
        self.name = name
        self.damage = damage
        self.preimage = image
        self.image = pygame.transform.scale(pygame.image.load(image), scale)
        self.rect = self.image.get_rect()
    
    def copy(self):
        return self.name, self.damage, self.preimage, self.type