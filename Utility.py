import pygame
from pygame.locals import *

class Utility:

    def __init__(self, name, image, scale, Coordx, Coordy):
        self.name = name
        self.image = pygame.transform.scale(image, scale)
        self.rect = image.get_rect()
        self.Coordx = Coordx
        self.Coordy = Coordy
        self.rect.center = (Coordx, Coordy)

