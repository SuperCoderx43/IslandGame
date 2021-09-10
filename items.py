import pygame
from pygame.locals import *

from item import Item

# have some variable for perm locations for not random spawning, maybe do something in the generate items variable

Wood = Item("Wood", pygame.image.load("ArtAssets/items/wood.png"), 'craft', 1, (120,60))
Meat = Item('Wood', pygame.image.load("ArtAssets/items/meat.png"), 'craft', 1, (120,60))

# somehow switch status to empty and full (maybe through prop)
Water = Item('Water Bottle', pygame.image.load("ArtAssets/items/waterbottleEMPTY.png"), 'water', 1, (120,60))

fruitBlue = Item('Blue Fruit', pygame.image.load("ArtAssets/items/fruitBLUE.png"), 'fruit', 1, (120,60))
fruitPurple = Item('Blue Meal', pygame.image.load("ArtAssets/items/fruitPURPLE.png"), 'fruit', 1, (120,60))
fruitRed = Item('Blue Meal', pygame.image.load("ArtAssets/items/fruitRED.png"), 'fruit', 1, (120,60))
fruitWhite = Item('Blue Meal', pygame.image.load("ArtAssets/items/fruitWHITE.png"), 'fruit', 1, (120,60))

# need to find a way to add health and increase max health through constant variable saved somewhere
mealPlain = Item('Plain Meal', pygame.image.load("ArtAssets/items/mealPLAIN.png"), 'meal', 0, (120,60))
mealBlue = Item('Blue Meal', pygame.image.load("ArtAssets/items/mealBLUE.png"), 'meal', 0, (120,60))
mealPurple = Item('Purple Meal', pygame.image.load("ArtAssets/items/mealPURPLE.png"), 'meal', 0, (120,60))
mealRed = Item('Red Meal', pygame.image.load("ArtAssets/items/mealRED.png"), 'meal', 0, (120,60))
mealWhite = Item('White Meal', pygame.image.load("ArtAssets/items/mealWHITE.png"), 'meal', 0, (120,60))

goldMonkey = Item('Golden Monkey', pygame.image.load("ArtAssets/items/goldMONKEY.png"), 'craft', 1, (120,60))
gladBlood = Item('Gladiator Blood', pygame.image.load("ArtAssets/items/gladiatorBLOOD.png"), 'craft', 1, (120,60))
spiderEye = Item('Spider Eye', pygame.image.load("ArtAssets/items/spiderEYE.png"), 'craft', 1, (120,60))
powerSource = Item('Power Source', pygame.image.load("ArtAssets/items/powerSource.png"), 'craft', 1, (120,60))

beacon = Item('Beacon', pygame.image.load("ArtAssets/items/beacon.png"), 'craft', 1, (120,60))

looseTooth = Item('Loose Tooth', pygame.image.load("ArtAssets/items/looseTooth.png"), 'craft', 1, (120,60))
bladeFrags = Item('Blade Fragments', pygame.image.load("ArtAssets/items/bladeFRAGS.png"), 'craft', 1, (120,60))

rustyBlade = Item('Rusty Blade', pygame.image.load('ArtAssets/weapons/RustyBladeMain.png'), 'weapon', 5, (20,65), pygame.image.load('ArtAssets/weapons/RustyBladeAR.png'), pygame.image.load('ArtAssets/weapons/RustyBladeAL.png'), pygame.image.load('ArtAssets/weapons/RustyBladeAF.png'), pygame.image.load('ArtAssets/weapons/RustyBladeAB.png'))
fangBlade = Item("Fang Blade", pygame.image.load('ArtAssets/weapons/FangBladeMain.png'), 'weapon', 10, (20, 65), pygame.image.load('ArtAssets/weapons/FangBladeAR.png'), pygame.image.load('ArtAssets/weapons/FangBladeAL.png'), pygame.image.load('ArtAssets/weapons/FangBladeAF.png'), pygame.image.load('ArtAssets/weapons/FangBladeAB.png'))
samBlade = Item("Samurai Blade", pygame.image.load('ArtAssets/weapons/SamuraiSwordMain.png'), 'weapon', 20, (20, 65), pygame.image.load('ArtAssets/weapons/SamuraiSwordAR.png'), pygame.image.load('ArtAssets/weapons/SamuraiSwordAL.png'), pygame.image.load('ArtAssets/weapons/SamuraiSwordAF.png'), pygame.image.load('ArtAssets/weapons/SamuraiSwordAB.png'))

