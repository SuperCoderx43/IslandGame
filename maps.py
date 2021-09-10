import pygame
from pygame.locals import *

from maptile import *
import items
from monsters import Crocodile
import utils
import walls
import weapons

RESOLUTION = (1300, 1000)

# add a secret part of the map maybe that is only accessible my teleport

tile_speed = 100
# connections = [up, down, left, right]
BEACHx1 = Maptile('beach1', [False, False, True, False], RESOLUTION, pygame.image.load("ArtAssets/map/BEACHx1.png"), tile_speed, [], [], [], walls.beachx1_walls)
BEACHx2 = Maptile('beach2', [True, True, False, True], RESOLUTION, pygame.image.load("ArtAssets/map/BEACHx2.png"), tile_speed, [items.rustyBlade], [], [], walls.beachx2_walls)
CAMP = Maptile('camp', [True, True, True, True], RESOLUTION, pygame.image.load("ArtAssets/map/CAMP.png"), tile_speed, [], [], [utils.Tent, utils.Campfire], walls.camp_walls)
FORESTx1 = Maptile('forest1', [True, False, True, True], RESOLUTION, pygame.image.load("ArtAssets/map/FORESTx1.png"), tile_speed, [items.Wood], [], [], walls.forestx1_walls)
FORESTx2 = Maptile('forest2',[True, True, True, False], RESOLUTION, pygame.image.load("ArtAssets/map/FORESTx2.png"), tile_speed, [items.Wood], [], [], walls.forestx2_walls)
RUINSx1 = Maptile('ruins1',[True, True, False, True], RESOLUTION, pygame.image.load("ArtAssets/map/RUINSx1.png"), tile_speed, [], [], [], walls.ruinsx1_walls)
RUINSx2 = Maptile('ruins2',[False, False, True, False], RESOLUTION, pygame.image.load("ArtAssets/map/RUINSx2.png"), tile_speed, [], [], [], walls.ruinsx2_walls)
RUINSx3 = Maptile('ruins3',[True, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/RUINSx3.png"), tile_speed, [], [], [], walls.ruinsx3_walls)
MOUNTAINx1 = Maptile('mountain1',[True, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/MOUNTAINx1.png"), tile_speed, [], [], [], walls.mountainx1_walls)
MOUNTAINx2 = Maptile('mountain2',[True, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/MOUNTAINx2.png"), tile_speed, [], [], [], walls.mountainx2_walls)
POND = Maptile('pond',[True, True, False, True], RESOLUTION, pygame.image.load("ArtAssets/map/POND.png"), tile_speed, [items.Wood], [], [], walls.pond_walls)
SPRING = Maptile('spring',[True, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/SPRING.png"), tile_speed, [], [], [], walls.spring_walls)
FIELD = Maptile('field',[True, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/FIELD.png"), tile_speed, [items.Wood], [], [], walls.field_walls)
CLEARING = Maptile('clearing',[True, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/CLEARING.png"), tile_speed, [], [], [], walls.clearing_walls)
TEMPLE = Maptile('temple',[False, False, True, True], RESOLUTION, pygame.image.load("ArtAssets/map/TEMPLE.png"), tile_speed, [], [], [], walls.temple_walls)
SECRET = Maptile('secret', [True, False, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/SECRET.png"), tile_speed, [], [], [], walls.secret_walls)

CROCxFIGHT = Maptile('crocxfight',[True, False, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/FIGHTxCROC.png"), tile_speed, [], [], [], walls.fightxcroc_walls, Crocodile)
SPIDERxFIGHT = Maptile('spiderxfight',[False, False, True, False], RESOLUTION, pygame.image.load("ArtAssets/map/FIGHTxSPIDER.png"), tile_speed, [], [], [], walls.fightxspider_walls)
MONKEYxFIGHT = Maptile('monkeyxfight',[False, False, False, True], RESOLUTION, pygame.image.load("ArtAssets/map/FIGHTxMONKEY.png"), tile_speed, [], [], [], walls.fightxmonkey_walls)
GLADxFIGHT = Maptile('gladxfight',[False, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/FIGHTxGLAD.png"), tile_speed, [], [], [], walls.fightxglad_walls)
SAMxFIGHT = Maptile('samxfight',[False, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/FIGHTxSAM.png"), tile_speed, [], [], [], walls.fightxsam_walls)
DRAGxFIGHT = Maptile('dragxfight',[False, True, False, False], RESOLUTION, pygame.image.load("ArtAssets/map/FIGHTxDRAG.png"), tile_speed, [], [], [], walls.fightxdrag_walls)
