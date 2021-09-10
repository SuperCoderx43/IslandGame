import numpy as np
import pygame, sys
import copy
from pygame import mouse
from pygame.event import event_name
from pygame.locals import *
from pygame.mixer import pause

from player import Player
from map import Map
from backpack import Backpack

Nature = 'Soundtrack/Nature.mp3'
MainTheme = 'Soundtrack/MainTheme.mp3'
Music = [MainTheme, Nature]

FPS = 30
WINDOWWIDTH = 1300
WINDOWHEIGHT = 1000
RESOLUTION = (WINDOWWIDTH, WINDOWHEIGHT)

# Color    = (RRR, GGG, BBB)
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
DARKGREY   = (100, 100, 100)
LIGHTGREY  = (200, 200, 200)
RED        = (255,   0,   0)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)

class GameController:

    def main(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT
        pygame.init()
        pygame.mixer.init()
        self.font = pygame.font.Font("ArtAssets/slkscr.ttf", 36)
        self.NatureSound = pygame.mixer.Sound(Nature)
        self.songChannel = pygame.mixer.Channel(1)
        self.effectChannel = pygame.mixer.Channel(0)
        pygame.display.set_caption('Stranded')
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load('ArtAssets/logo.png'), (100,100)))
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

        self.showStartScreen()
        while True:
            self.runGame()
            self.showGameOverScreen()



    def showStartScreen(self):
        # have start menu with start game, exit to desktop, and credits
        return

    def runGame(self):
        # need to plot a note saying general game info (basic lore, no saving, etc.)
        # things
        self.days = 0
        self.state = 'running' # keep track of game state
        self.dash_timer = pygame.USEREVENT + 1 
        self.dash_enabled = False
        self.dash_count = 3
        # instantiate objects: player, map, items
        player_speed = 35
        player_scale = (80,160)
        player_health = 25
        self.player_one = Player(player_speed, WINDOWWIDTH, WINDOWHEIGHT, [], player_scale, player_health)
        self.leftHeld = False
        self.rightHeld = False
        self.upHeld = False
        self.downHeld = False
        self.enterHeld = False
        self.attacking = False
        self.dash = None
        self.inventory = False
        self.pause = False

        self.backpack_inv = Backpack()

        self.game_map = Map()
        self.current_tile = self.game_map.current_tile

        DISPLAYSURF.fill(BLACK)
        

        # Game Loop
        while True:
            print("Days: " + str(self.days))
            dayEnd = False
            
            #play a song
            self.songChannel.stop()
            self.NatureSound.set_volume(0.05)
            self.songChannel.play(self.NatureSound, 1, 0, 1000)
            self.songChannel.set_volume(0.1)
            # Day Loop
            while True:
                self.draw(self.current_tile.image, self.current_tile.rect)
                if self.current_tile.monsters != None and self.current_tile.monsters.alive == True:
                    self.bossFight()
                    continue
                # event handler
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.terminate()
                    elif event.type == self.dash_timer:
                        self.dash_count -= 1
                        if self.dash_count == 0:
                            pygame.time.set_timer(self.dash_timer, 0)
                            self.dash_enabled = False
                    elif event.type == KEYDOWN:
                        if event.key == K_w or event.key == K_UP:
                            self.upHeld = True
                        elif event.key == K_d or event.key == K_RIGHT:
                            self.rightHeld = True
                        elif event.key == K_s or event.key == K_DOWN:
                            self.downHeld = True
                        elif event.key == K_a or event.key == K_LEFT:
                            self.leftHeld = True
                        elif event.key == K_SPACE:
                            self.attacking = True
                        elif event.key == K_RETURN:
                            self.enterHeld = True
                        elif event.key == K_LSHIFT:
                            if not self.dash_enabled:
                                self.dash = True          
                        elif event.key == K_ESCAPE:
                            self.state = 'paused'
                        elif event.key == K_b:
                            self.inventory = True
                    elif event.type == KEYUP:
                        if event.key == K_w or event.key == K_UP:
                            self.upHeld = False
                        elif event.key == K_d or event.key == K_RIGHT:
                            self.rightHeld = False
                        elif event.key == K_s or event.key == K_DOWN:
                            self.downHeld = False
                        elif event.key == K_a or event.key == K_LEFT:
                            self.leftHeld = False
                        elif event.key == K_SPACE:
                            self.attacking = False
                        elif event.key == K_RETURN:
                            self.enterHeld = False
                        elif event.key == K_LSHIFT:
                            self.dash = False
                        elif event.key == K_b:
                            self.inventory = False
                # check for pause
                if self.state == 'paused':
                    self.paused()
                    self.state = 'running'
                # check for backpack
                if self.inventory:
                    self.drawBackpack()
                # move things
                if self.dash:
                    self.dash_count = 3
                    pygame.time.set_timer(self.dash_timer, 1000)
                    self.dash_enabled = True
                    self.player_one.dash(left=self.leftHeld, right=self.rightHeld, down=self.downHeld, up=self.upHeld, walls=self.current_tile.walls)
                    self.dash = False
                self.player_one.move(left=self.leftHeld, right=self.rightHeld, down=self.downHeld, up=self.upHeld, walls=self.current_tile.walls)
                playerwalk = np.random.randint(0, 60)
                self.player_one.updatePicture(self.upHeld, self.downHeld, self.leftHeld, self.rightHeld, self.attacking, playerwalk)
                
                
                # player item interract
                
                if self.enterHeld:
                    for util in self.current_tile.utilities:
                        if self.player_one.rect.colliderect(util.rect):
                            if util.name == 'Tent':
                                print("found the tent")
                                # sleep function messes up with the days
                                self.sleep()
                                dayEnd = True
                                self.enterHeld = False
                                break
                            elif util.name == 'Campfire':
                                self.crafting()
                                self.enterHeld = False
                                break
                if dayEnd:
                    self.days += 1
                    break
                # detect collisions
                if self.player_one.rect.top <= 10:
                    if self.game_map.moveTiles('up'):
                        self.player_one.rect.bottom = WINDOWHEIGHT - 11
                elif self.player_one.rect.bottom >= WINDOWHEIGHT - 10:
                    if self.game_map.moveTiles('down'):
                        self.player_one.rect.top = 11
                elif self.player_one.rect.left <= 10:
                    if self.game_map.moveTiles('left'):
                        self.player_one.rect.right = WINDOWWIDTH - 11
                elif self.player_one.rect.right >= WINDOWWIDTH - 10:
                    if self.game_map.moveTiles('right'):
                        self.player_one.rect.left = 11
                self.current_tile = self.game_map.current_tile

                if len(self.current_tile.live_items) != 0:
                    for item in self.current_tile.live_items:
                        if self.player_one.rect.colliderect(item.rect):
                            self.itemFound(item, self.current_tile)
                            break

                # draw things
                self.draw(self.current_tile.image, self.current_tile.rect)
                for util in self.current_tile.utilities:
                    self.draw(util.image, util.rect)
                self.draw(self.player_one.currentImage, self.player_one.rect)
                if self.backpack_inv.selecteditem:
                    self.draw(self.player_one.equipped['item'].currentimage, self.player_one.equipped['item'].currentrect)
                # draw tile items
                for item in self.current_tile.live_items:
                    if item != None:
                        self.draw(item.image, item.rect)
                # draw hud
                if self.dash_enabled:
                    DISPLAYSURF.blit(self.font.render(str(self.dash_count), False, BLACK), (WINDOWWIDTH - 50, WINDOWHEIGHT - 50))
                self.playerHealthBar()
                
                pygame.display.update()
                FPSCLOCK.tick(FPS)
            # perform end of day stuff
            for row in self.game_map.map:
                for tile in row:
                    if tile != None:
                        tile.clearItems()
                        tile.generateItems()
            print(self.player_one.inventory)


    def sleep(self):
        self.player_one.setStartPos()
        self.game_map.updateTiles(4, 3)
        self.current_tile = self.game_map.current_tile
        transparency = 255
        while True:
            DISPLAYSURF.fill((0, 0, 0, transparency))
            DISPLAYSURF.blit(self.font.render("DAYS: " + str(self.days + 1), False, WHITE), (WINDOWWIDTH / 2 - 50, WINDOWHEIGHT / 2 - 50))
            transparency -= 10
            
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            
            if transparency <= 25:
                break
            
        
    def bossFight(self):
        #make sure to add so if the player leaves the arena, then the monster health resets if it was not killed
        self.monster = self.current_tile.monsters
        self.monster.setStartPos()
        self.attack_timer = USEREVENT 
        pygame.time.set_timer(self.attack_timer, 1000)
        monstercount = 8
        attackcount = 1
        monsterattacking = False
        attackingpossible = False
        #add monster health bar

        # add monster loot pickup stuff
        while True:
            for event in pygame.event.get():
                    if event.type == QUIT:
                        self.terminate()
                    elif event.type == self.attack_timer:
                        monstercount -= 1
                        print("M: " + str(monstercount))
                        if monstercount < 1:
                            if self.monster.behavior == 'rabid':
                                monsterattacking = True
                                print("A: " + str(attackcount))
                                if attackcount == 0:
                                    monstercount = 8
                                    attackcount = 2
                                    monsterattacking = False
                                attackcount -= 1
                    elif event.type == self.dash_timer:
                        self.dash_count -= 1
                        if self.dash_count == 0:
                            pygame.time.set_timer(self.dash_timer, 0)
                            self.dash_enabled = False
                    elif event.type == KEYDOWN:
                        if event.key == K_w or event.key == K_UP:
                            self.upHeld = True
                        elif event.key == K_d or event.key == K_RIGHT:
                            self.rightHeld = True
                        elif event.key == K_s or event.key == K_DOWN:
                            self.downHeld = True
                        elif event.key == K_a or event.key == K_LEFT:
                            self.leftHeld = True
                        elif event.key == K_SPACE:
                            self.attacking = True
                        elif event.key == K_RETURN:
                            self.enterHeld = True
                        elif event.key == K_LSHIFT:
                            if not self.dash_enabled:
                                self.dash = True          
                        elif event.key == K_ESCAPE:
                            self.state = 'paused'
                        elif event.key == K_b:
                            self.inventory = True
                    elif event.type == KEYUP:
                        if event.key == K_w or event.key == K_UP:
                            self.upHeld = False
                        elif event.key == K_d or event.key == K_RIGHT:
                            self.rightHeld = False
                        elif event.key == K_s or event.key == K_DOWN:
                            self.downHeld = False
                        elif event.key == K_a or event.key == K_LEFT:
                            self.leftHeld = False
                        elif event.key == K_SPACE:
                            self.attacking = False
                            attackingpossible = True
                        elif event.key == K_RETURN:
                            self.enterHeld = False
                        elif event.key == K_LSHIFT:
                            self.dash = False
                        elif event.key == K_b:
                            self.inventory = False
            # check for pause
            if self.state == 'paused':
                self.paused()
                self.state = 'running'
            # check for inventory
            if self.inventory:
                self.drawBackpack()
            # move things
            if self.dash:
                self.dash_count = 3
                pygame.time.set_timer(self.dash_timer, 1000)
                self.dash_enabled = True
                self.player_one.dash(left=self.leftHeld, right=self.rightHeld, down=self.downHeld, up=self.upHeld, walls=self.current_tile.walls)
                self.dash = False
            self.player_one.move(left=self.leftHeld, right=self.rightHeld, down=self.downHeld, up=self.upHeld, walls=self.current_tile.walls)
            playerwalk = np.random.randint(0, 60)
            self.player_one.updatePicture(self.upHeld, self.downHeld, self.leftHeld, self.rightHeld, self.attacking, playerwalk)

            if monsterattacking: 
                self.monster.rabidAttack(self.player_one.rect)
            else: self.monster.move(self.current_tile, self.player_one, self.monster.speed)

            # player item interract

            # detect collisions
            # wall connections first
            leave = False
            if self.player_one.rect.top <= 10:
                if self.game_map.moveTiles('up'):
                    self.player_one.rect.bottom = WINDOWHEIGHT - 11
                    leave = True
            elif self.player_one.rect.bottom >= WINDOWHEIGHT - 10:
                if self.game_map.moveTiles('down'):
                    self.player_one.rect.top = 11
                    leave = True
            elif self.player_one.rect.left <= 10:
                if self.game_map.moveTiles('left'):
                    self.player_one.rect.right = WINDOWWIDTH - 11
                    leave = True
            elif self.player_one.rect.right >= WINDOWWIDTH - 10:
                if self.game_map.moveTiles('right'):
                    self.player_one.rect.left = 11
                    leave = True
            self.current_tile = self.game_map.current_tile
            if leave:
                if self.monster.alive:
                    self.monster.health = self.monster.maxhealth
                break
            
            # if player attacks monster
            if self.player_one.equipped['item'] != None:
                if self.player_one.equipped['item'].currentrect.colliderect(self.monster.rect) and self.attacking and attackingpossible:
                    self.monster.health -= self.player_one.equipped['item'].property
                    attackingpossible = False
            else:
                if self.attacking and attackingpossible:
                    self.monster.health -= 1
                    attackingpossible = False

            #if player attacked by monster
            

            # draw things
            self.draw(self.current_tile.image, self.current_tile.rect)
            self.draw(self.player_one.currentImage, self.player_one.rect)
            self.draw(self.monster.currentImage, self.monster.rect)
            if self.backpack_inv.selecteditem:
                self.draw(self.player_one.equipped['item'].currentimage, self.player_one.equipped['item'].currentrect)
            self.monsterHealthBar(self.monster)
            self.playerHealthBar()
            # draw tile items
            # once boss dies, add their loot to live_items and update th eloot on the ground!
            for item in self.current_tile.live_items:
                if item != None:
                    self.draw(item.image, item.rect)
            # draw hud
            if self.dash_enabled:
                DISPLAYSURF.blit(self.font.render(str(self.dash_count), False, BLACK), (WINDOWWIDTH - 50, WINDOWHEIGHT - 50))
            
            pygame.display.update()
            FPSCLOCK.tick(FPS)   

    def drawAndUpdate(self):
        return
    
    def initializeObjects(self, num):
        objects = []
        for i in range(num):
            objects.append(None)
        return objects


    def draw(self, image, rect):
        DISPLAYSURF.blit(image,rect)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def showGameOverScreen(self):
        return

    def paused(self):
        # pause screen
        unpause = False
        # need to learn buttons for menus!
        self.songChannel.pause()
        self.effectChannel.pause()

        pause_menu = pygame.transform.scale(pygame.image.load("ArtAssets/menus/pause.png"), (650, 500))

        # create buttons
        pause_text = self.font.render('PAUSED', False, BLACK)
        continue_text = self.font.render('continue', False, BLACK)
        control_text = self.font.render('controls', False, BLACK)
        quit_text = self.font.render("quit", False, BLACK)

        # pause_button = pygame.Rect(pause_text)
        
        # pause loop
        pygame.event.clear()
        while True:
            # draw buttons
            self.draw(self.current_tile.image, self.current_tile.rect)
            DISPLAYSURF.blit(pause_menu, ((WINDOWWIDTH - 650) / 2, (WINDOWHEIGHT - 500) / 2))
            DISPLAYSURF.blit(pause_text, (425, 350))
            DISPLAYSURF.blit(continue_text, (450, 450))
            DISPLAYSURF.blit(control_text, (450, 515))
            DISPLAYSURF.blit(quit_text, (450, 583))

            continue_button = pygame.Rect(450, 450, 150, 30)
            control_button = pygame.Rect(450, 515, 150, 30)
            quit_button = pygame.Rect(450, 583, 150, 30)

            for event in pygame.event.get():
                if event.type == QUIT:
                        self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    mousecoords = pygame.mouse.get_pos()
                    mouseRect = pygame.Rect(mousecoords[0], mousecoords[1], 2, 2)
                    
                    if mouseRect.colliderect(continue_button):
                        unpause = True
                        break
                    elif mouseRect.colliderect(control_button):
                        response = self.controls()
                        if response == 0:
                            continue
                        elif response == 1:
                            unpause = True
                            break
                    elif mouseRect.colliderect(quit_button):
                        self.terminate()
                    
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        unpause = True
                        break
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            if unpause:
                break
            continue
        self.songChannel.unpause()
        self.effectChannel.unpause()
    
    def controls(self):
        DISPLAYSURF.fill(BLACK)
        control = True
        back = False
        control_menu = pygame.transform.scale(pygame.image.load("ArtAssets/menus/controls.png"), (650, 500))
        self.draw(self.current_tile.image, self.current_tile.rect)
        DISPLAYSURF.blit(control_menu, ((WINDOWWIDTH - 650) / 2, (WINDOWHEIGHT - 500) / 2))
        back_text = self.font.render("<- BACK", False, BLACK)
        self.controlFont = pygame.font.Font("ArtAssets/slkscr.ttf", 26)
        control_text1 = self.controlFont.render("WASD/Arrow keys to Move", False, BLACK)
        control_text_0 = self.controlFont.render("Return/Enter to interact", False, BLACK)
        control_text2 = self.controlFont.render("Space to Attack", False, BLACK)
        control_text3 = self.controlFont.render("LShift to Dash", False, BLACK)
        control_text4 = self.controlFont.render("B for backpack", False, BLACK)
        control_text5 = self.controlFont.render("L to leave crafting menu", False, BLACK)
        back_button = pygame.Rect(425, 350, 150, 30)
        pygame.event.clear()
        self.draw(self.current_tile.image, self.current_tile.rect)
        back_button = pygame.Rect(425, 350, 150, 30)
        DISPLAYSURF.blit(control_menu, ((WINDOWWIDTH - 650) / 2, (WINDOWHEIGHT - 500) / 2))
        DISPLAYSURF.blit(back_text, (425, 350))
        DISPLAYSURF.blit(control_text1, (400, 450))
        DISPLAYSURF.blit(control_text2, (400, 480))
        DISPLAYSURF.blit(control_text3, (400, 510))
        DISPLAYSURF.blit(control_text4, (400, 540))
        DISPLAYSURF.blit(control_text_0, (400, 570))
        DISPLAYSURF.blit(control_text5, (400, 600))
        # control menu loop
        while True:
            self.draw(self.current_tile.image, self.current_tile.rect)
            back_button = pygame.Rect(425, 350, 150, 30)
            DISPLAYSURF.blit(control_menu, ((WINDOWWIDTH - 650) / 2, (WINDOWHEIGHT - 500) / 2))
            DISPLAYSURF.blit(back_text, (425, 350))
            DISPLAYSURF.blit(control_text1, (400, 450))
            DISPLAYSURF.blit(control_text2, (400, 480))
            DISPLAYSURF.blit(control_text3, (400, 510))
            DISPLAYSURF.blit(control_text4, (400, 540))
            DISPLAYSURF.blit(control_text_0, (400, 570))
            DISPLAYSURF.blit(control_text5, (400, 600))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    mousecoords = pygame.mouse.get_pos()
                    mouseRect = pygame.Rect(mousecoords[0], mousecoords[1], 2, 2)
                    if mouseRect.colliderect(back_button):
                        control = False
                        break
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        back = True
                        break
            if not control: return 0
            if back: return 1
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def playerHealthBar(self):
        self.playerFont = pygame.font.Font("ArtAssets/slkscr.ttf", 20)
        
        green_length = int((self.player_one.hp / self.player_one.maxhp) * 200)
        red_length = 200 - green_length

        pygame.draw.rect(DISPLAYSURF, DARKGREY, (WINDOWWIDTH / 2 - 110, 10, 220, 60))
        pygame.draw.rect(DISPLAYSURF, RED, (WINDOWWIDTH / 2 - 100 + green_length, 15, red_length, 50))
        pygame.draw.rect(DISPLAYSURF, GREEN, (WINDOWWIDTH / 2 - 100, 15, green_length, 50))
        DISPLAYSURF.blit(self.playerFont.render("Health", False, BLACK), (WINDOWWIDTH / 2- 100, 0))

    def monsterHealthBar(self, monster):
        GREY = (155, 155, 155)
        GREEN = (100, 218, 50)
        RED = (241, 72, 39)

        self.monsterFont = pygame.font.Font("ArtAssets/slkscr.ttf", 18)
        DISPLAYSURF.blit(self.monsterFont.render(monster.name + " Health", False, (0,0,0)), (500, 840))
        pygame.draw.rect(DISPLAYSURF, GREY, (450, 850, 400, 100))

        # green / red
        green_length = int((monster.health / monster.maxhealth) * 300)
        red_length = 300 - green_length
        pygame.draw.rect(DISPLAYSURF, RED, ((500 + green_length), 860, red_length, 80))
        pygame.draw.rect(DISPLAYSURF, GREEN, (500, 860, green_length, 80))
        DISPLAYSURF.blit(self.monsterFont.render(monster.name + " Health", False, (0,0,0)), (500, 840))
    
    def drawBackpack(self):
        looking = True
        self.quantFont = pygame.font.Font("ArtAssets/slkscr.ttf", 20)
        slotindex = 0
        itemquantities = []
        itemquantitiesrects = []
        
        # setup item positions on backpack
        for dict in self.player_one.inventory:
            itemrect = dict['item'].backpackrect
            itemrect.center = (self.backpack_inv.allslotsrects[slotindex].centerx, self.backpack_inv.allslotsrects[slotindex].centery - 15)
            itemquantities.append(self.quantFont.render(str(dict['quantity']), False, (0,0,0)))
            itemquantitiesrects.append(pygame.Rect(itemrect.left, itemrect.bottom + 20, 20, 20))
            slotindex += 1
        
        while True:
            #draw stuff
            self.draw(self.current_tile.image, self.current_tile.rect)
            self.draw(self.backpack_inv.backgroundimage, self.backpack_inv.backgroundrect)

            for i in range(len(self.backpack_inv.allslots)):
                self.draw(self.backpack_inv.allslots[i], self.backpack_inv.allslotsrects[i])

            for i in range(len(self.player_one.inventory)):
                self.draw(self.player_one.inventory[i]['item'].backpackimage, self.player_one.inventory[i]['item'].backpackrect)
                DISPLAYSURF.blit(itemquantities[i], itemquantitiesrects[i])


            if self.backpack_inv.selecteditem:
                DISPLAYSURF.blit(self.backpack_inv.selected, self.backpack_inv.selectedrect)
            for event in pygame.event.get():
                if event.type == QUIT:
                        self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    mousecoords = pygame.mouse.get_pos()
                    mouseRect = pygame.Rect(mousecoords[0], mousecoords[1], 2, 2)
                    
                    if self.backpack_inv.selecteditem and mouseRect.colliderect(self.backpack_inv.selectedrect):
                        self.backpack_inv.selecteditem = False
                        self.player_one.equipped = {'item': None, 'quantity': 0}
                    else:
                        for i in range(len(self.backpack_inv.allslots)):
                            slot = self.backpack_inv.allslotsrects[i]
                            if mouseRect.colliderect(slot):
                                if len(self.player_one.inventory) > i and len(self.player_one.inventory) > 0:
                                    self.player_one.equipped = {'item': self.player_one.inventory[i]['item'], 'quantity': self.player_one.inventory[i]['quantity']}
                                    self.backpack_inv.selectedrect.center = slot.center
                                    self.backpack_inv.selecteditem = True
                                    self.backpack_inv.selectedIndex = i
                                    break
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.paused()
                    elif event.key == K_b:
                        self.inventory = False
                        looking = False
                        break
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            if not looking:
                break
    
    def itemFound(self, item, tile):
        for thing in tile.inventory:
            if item.name == thing.name:
                if item.name == "Rusty Blade":
                    thing.found = True
        for thing in self.player_one.inventory:
            if thing['item'].name == item.name:
                thing['quantity'] += 1
                self.current_tile.live_items.remove(item)
                return
        self.player_one.inventory.append({'item': item, 'quantity': 1})
        self.current_tile.live_items.remove(item)
    
    def crafting(self):
        leave = False
        craftchoice = pygame.transform.scale(pygame.image.load('ArtAssets/menus/craftchoice.png'), (800, 500))
        craftchoicerect = craftchoice.get_rect()
        craftchoicerect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

        self.craftFont = pygame.font.Font("ArtAssets/slkscr.ttf", 25)
        campfire_txt = self.font.render("Campfire", False, (0,0,0))
        cooking_txt = self.craftFont.render("Cooking", False, (0,0,0))
        cooking_txt_rect = pygame.Rect(400, 405, 400, 60)
        crafting_txt = self.craftFont.render("Crafting", False, (0,0,0))
        crafting_txt_rect = pygame.Rect(400, 485, 200, 60)

        while True:
            DISPLAYSURF.blit(craftchoice, craftchoicerect)
            DISPLAYSURF.blit(campfire_txt, (380, 300))
            DISPLAYSURF.blit(cooking_txt, cooking_txt_rect)
            DISPLAYSURF.blit(crafting_txt, crafting_txt_rect)
            for event in pygame.event.get():
                if event.type == QUIT:
                        self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    mousecoords = pygame.mouse.get_pos()
                    mouseRect = pygame.Rect(mousecoords[0], mousecoords[1], 2, 2)
                    if mouseRect.colliderect(cooking_txt_rect):
                        # cook food loop
                        self.foodLoop()
                    elif mouseRect.colliderect(crafting_txt_rect):
                        # craft stuff loop
                        self.itemLoop()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        leave = True
                        break
                    elif event.key == K_l:
                        leave = True
                        break
            pygame.display.update()
            FPSCLOCK.tick(FPS)

            if leave:
                break    
    
    def foodLoop(self):
        craftfood = pygame.transform.scale(pygame.image.load("ArtAssets/menus/craftfood.png"), (800, 500))
        craftfoodrect = craftfood.get_rect()
        craftfoodrect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        leave = False
        while True:
            DISPLAYSURF.blit(craftfood, craftfoodrect)
            for event in pygame.event.get():
                if event.type == QUIT:
                        self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    mousecoords = pygame.mouse.get_pos()
                    mouseRect = pygame.Rect(mousecoords[0], mousecoords[1], 2, 2)
                    continue
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        leave = True
                        break
                    elif event.key == K_l:
                        leave = True
                        break
            pygame.display.update()
            FPSCLOCK.tick(FPS)
             
            if leave:
                break
    
    def itemLoop(self):
        crafttool = pygame.transform.scale(pygame.image.load('ArtAssets/menus/craftmenu.png'), (800, 500))
        crafttoolrect = crafttool.get_rect()
        crafttoolrect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        leave = False
        while True:
            DISPLAYSURF.blit(crafttool, crafttoolrect)
            for event in pygame.event.get():
                if event.type == QUIT:
                        self.terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    mousecoords = pygame.mouse.get_pos()
                    mouseRect = pygame.Rect(mousecoords[0], mousecoords[1], 2, 2)
                    continue
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        leave = True
                        break
                    elif event.key == K_l:
                        leave = True
                        break
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            if leave:
                break
            
