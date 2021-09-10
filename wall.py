import pygame
from pygame.locals import *

class Wall:

    def __init__(self, name, orient, left, top, width, height):
        self.name = name
        self.orient = orient # orient = 0 means horizontal, orient = 1 means vertical
        self.rect = Rect(left,top,width,height)