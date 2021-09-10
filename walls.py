from wall import Wall
WINDOWWIDTH = 1300
WINDOWHEIGHT = 1000

# beachx1 walls
beachx1w1 = Wall('beachx1.oceanwall', 0, 0, WINDOWHEIGHT - 200, WINDOWWIDTH, 200)
beachx1w2 = Wall('beachx1.floralwall', 0, 0, 0, WINDOWWIDTH, 100)
beachx1_walls = [beachx1w1, beachx1w2]

# beachx2 walls
beachx2w1 = Wall('beachx2.oceanwall', 0, 0, WINDOWHEIGHT - 200, WINDOWWIDTH, 200)
beachx2w2 = Wall('beachx2.floralwall', 0, 500, 0, 900, 100)
beachx2w3 = Wall('beachx2.rockwall', 1, 0, 0, 150, WINDOWHEIGHT)
beachx2_walls = [beachx2w1, beachx2w2, beachx2w3]

# secret walls
secretw1 = Wall('secret.rightpath', 1, 500, 0, 1, 600)
secretw2 = Wall('secret.oceanbarrier', 0, 502, 560, WINDOWWIDTH - 502, 1)
secret_walls = [secretw1, secretw2]

# camp walls
campw1 = Wall('camp.topright', 0, 1150, 0, 150, 100)
campw2 = Wall('camp.bottomright', 0, 500, 800, WINDOWWIDTH - 500, 200)
campw3 = Wall('camp.bottomleft', 1, 0, 800, 100, 150)
campw4 = Wall('camp.topleft', 0, 0, 0, 150, 100)
campw5 = Wall('camp.bottomrightvert', 1, 610, 800, 50, 200)
camp_walls = [campw1, campw2, campw3, campw4]

# pond walls
pondw1 = Wall('pond.topright', 0, WINDOWWIDTH - 200, 0, 200, 100)
pondw2 = Wall('pond.bottomright', 1, WINDOWWIDTH - 150, 800, 150, 150)
pondw3 = Wall('pond.rockwall', 1, 0, 0, 100, WINDOWHEIGHT)
pond_walls = [pondw1, pondw2, pondw3]

# forestx1 walls
forestx1w1 = Wall('forest1.bottom', 0, 0, 800, WINDOWWIDTH, 200)
forestx1w2 = Wall('forest1.topleft', 0, 0, 0, 200, 100)
forestx1w3 = Wall('forest1.topright', 1, 900, 0, WINDOWWIDTH - 900, 100) 
forestx1w4 = Wall('forestx.toprighthori', 0, 900, 0, WINDOWWIDTH - 900, 100)
forestx1_walls = [forestx1w1, forestx1w2, forestx1w3, forestx1w4]

# spring walls
springw1 = Wall('spring.topright', 0, WINDOWWIDTH - 150, 0, 150, 100)
springw2 = Wall('spring.topleft', 0, 0, 0, 150, 100)
springw3 = Wall('spring.leftspringtop', 0, 0, 500, 350, 100)
springw4 = Wall('spring.leftspringright', 1, 350, 650, 10, 350)
springw5 = Wall('spring.rightspringtop', 0, 950, 500, 350, 100)
springw6 = Wall('spring.rightspringleft', 1, 950, 650, 10, 350)
spring_walls = [springw1, springw2, springw3, springw4, springw5, springw6]

# fightxcroc walls
crocw1 = Wall('croc.topright', 0, 950, 0, 350, 50)
crocw2 = Wall('croc.topleft', 0, 0, 0, 350, 50)
crocw3 = Wall('croc.bottomright', 0, 1000, 950, 300, 50)
crocw4 = Wall('croc.bottomleft', 0, 0, 950, 350, 50)
fightxcroc_walls = [crocw1, crocw2, crocw3, crocw4]

# fightxspider walls
spiderw1 = Wall('spider.bottomleft', 1, 0, 700, 40, 300)
spiderw2 = Wall('spider.topleft', 1, 0, 0, 40, 300)
fightxspider_walls = [spiderw1, spiderw2]

# ruinsx1 walls
ruinx1w1 = Wall('ruin1.left', 1, 0, 0, 200, WINDOWHEIGHT)
ruinx1w2 = Wall('ruin1.toprightvert', 1, 950, 0, WINDOWWIDTH - 950, 150)
# ruinx1w3 = Wall('ruin1.toprighthoriz', 0, 950, 150, WINDOWWIDTH - 950, 50)
ruinx1w4 = Wall('ruin1.bottomrightvert', 1, 900, WINDOWHEIGHT - 310, 40, 300)
ruinx1w5 = Wall('ruin1.bottomrighthoriz', 0, 950, WINDOWHEIGHT - 300, WINDOWWIDTH - 950, 50)
ruinsx1_walls = [ruinx1w1, ruinx1w2, ruinx1w4, ruinx1w5]

# ruinsx2 walls
ruinx2w1 = Wall('ruin2.topleftvert', 1, 0, 0, 450, 150)
# ruinx2w2 = Wall('ruin2.toplefthoriz', 0, 0, 100, 440, 10)
ruinx2w3 = Wall('ruin2.bottomleftvert', 1, 460, WINDOWHEIGHT - 320, 40, 300)
ruinx2w4 = Wall('ruin2.bottomrighthoriz', 0, 0, WINDOWHEIGHT - 300, 450, 40)
ruinx2w5 = Wall('ruin2.rockwall', 1, WINDOWWIDTH - 75, 0, 75, WINDOWHEIGHT)
ruinsx2_walls = [ruinx2w1, ruinx2w3, ruinx2w4, ruinx2w5]

# ruinsx3 walls
ruinx3w1 = Wall('ruin3.bottomright', 0, 955, WINDOWHEIGHT - 50, WINDOWWIDTH - 955, 50)
ruinx3w2 = Wall('ruin3.bottomleft', 0, 0, WINDOWHEIGHT - 50, 200, 50)
ruinx3w3 = Wall('ruin3.leftstadium', 0, 0, 0, 400, 45)
ruinx3w4 = Wall('ruin3.rightstadium', 0, 900, 0, 400, 45)

ruinsx3_walls = [ruinx3w1, ruinx3w2, ruinx3w3, ruinx3w4]

# fightxglad walls
gladw1 = Wall('glad.top', 0, 0, 0, WINDOWWIDTH, 100)

fightxglad_walls = [gladw1]

# mountainx1 walls
mx1w1 = Wall('m1.left', 1, 0, 0, 150, WINDOWHEIGHT)
mx1w2 = Wall('m1.right', 1, WINDOWWIDTH - 150, 0, 150, WINDOWHEIGHT)
mountainx1_walls = [mx1w1, mx1w2]

# mountainx2 walls
mx2w1 = Wall('m2.left', 1, 0, 0, 150, WINDOWHEIGHT)
mx2w2 = Wall('m2.right', 1, WINDOWWIDTH - 150, 0, 150, WINDOWHEIGHT)
mx2w3 = Wall('m2.topleft', 0, 0, 0, 400, 200)
mx2w4 = Wall('m2.topright', 0, WINDOWWIDTH - 400, 0, 400, 200)

mountainx2_walls = [mx2w1, mx2w2, mx2w3, mx2w4]

# fightxdrag walls
dragw1 = Wall('drag.top', 0, 0, 0, WINDOWWIDTH, 75)
dragw2 = Wall('drag.bottomleft', 0, 0, WINDOWHEIGHT - 50, 400, 50)
dragw3 = Wall('drag.bottomright', 0, WINDOWWIDTH - 200, WINDOWHEIGHT - 50, 400, 50)

fightxdrag_walls = [dragw1, dragw2, dragw3]

# forestx2 walls
forestx2w1 = Wall('forestx2.bottomleft', 0, 0, 900, 100, 100)
forestx2w2 = Wall('forestx2.topleft', 0, 0, 0, 200, 100)
forestx2w3 = Wall('forestx2.right', 1, 1100, 0, 200, WINDOWHEIGHT)
forestx2_walls = [forestx2w1, forestx2w2, forestx2w3]

# temple walls
templew1 = Wall('temple.top', 0, 0, 0, WINDOWWIDTH, 100)
templew2 = Wall('temple.bottom', 0, 0, 900, WINDOWWIDTH, 100)
templew3 = Wall('temple.doorbottom', 1, 75, 800, 50, 200)
templew4 = Wall('templedoortop', 1, 75, 0, 50, 200)
temple_walls = [templew1, templew2, templew3, templew4]

# fightxmonkey walls
monkeyw1 = Wall('monkey.top', 0, 0, 0, WINDOWWIDTH, 50)
monkeyw2 = Wall('monkey.bottom', 0, 0, 950, WINDOWWIDTH, 50)
monkeyw3 = Wall('monkey.left', 1, 0, 0, 50, WINDOWHEIGHT)
monkeyw4 = Wall('monkey.topright', 1, WINDOWWIDTH - 50, 0, 50, 200)
monkeyw5 = Wall('monkey.bottomright', 1, WINDOWWIDTH - 50, 800, 50, 200)
fightxmonkey_walls = [monkeyw1, monkeyw2, monkeyw3, monkeyw4, monkeyw5]

# field walls
fieldw1 = Wall("field.bottomright", 0, 1100, 900, 200, 100)
fieldw2 = Wall('field.bottomleft', 0, 0, 900, 200, 100)
field_walls = [fieldw1, fieldw2]

# clearing walls
clearing_walls = []

# fightxsam walls
samw1 = Wall('sam.top', 0, 0, 0, WINDOWWIDTH, 100)

fightxsam_walls = [samw1]