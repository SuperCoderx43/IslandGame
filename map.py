from maps import *
WINDOWWIDTH = 1300
WINDOWHEIGHT = 1000


class Map:
    BEACHx1
    BEACHx2
    CAMP
    FORESTx1
    FORESTx2
    RUINSx1
    RUINSx2
    RUINSx3
    MOUNTAINx1
    MOUNTAINx2
    POND
    SPRING
    FIELD
    CLEARING
    TEMPLE
    SECRET

    CROCxFIGHT
    SPIDERxFIGHT
    MONKEYxFIGHT
    GLADxFIGHT
    SAMxFIGHT
    DRAGxFIGHT

    def __init__(self):
        self.map = [[        None,   None, SAMxFIGHT,       None,       None,         None],
                    [        None,   None,  CLEARING, DRAGxFIGHT, GLADxFIGHT,         None],
                    [        None,   None,     FIELD, MOUNTAINx2,    RUINSx3,         None],
                    [MONKEYxFIGHT, TEMPLE,  FORESTx2, MOUNTAINx1,    RUINSx1,      RUINSx2],
                    [        None,   None,      POND,       CAMP,   FORESTx1, SPIDERxFIGHT],
                    [        None,   None,    SPRING,    BEACHx2,    BEACHx1,         None],
                    [        None,   None,CROCxFIGHT,     SECRET,       None,         None],]
                    # add secret to ruinsx1
        self.current_tileR = 5
        self.current_tileC = 4
        self.current_tile = self.map[self.current_tileR][self.current_tileC]
    
    def updateTiles(self, R, C):
        self.current_tileR = R
        self.current_tileC = C
        self.current_tile = self.map[R][C]
    
    def moveTiles(self, direction):
        if direction == 'up':
            # print("Checking up")
            if self.current_tile.up:
                    self.next_tile = self.map[self.current_tileR - 1][self.current_tileC]
                    self.current_tile = self.next_tile
                    self.current_tileR = self.current_tileR-1
                    self.current_tile.rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
                    # print(self.current_tile.name)
                    return True
                    
        elif direction == 'down':
            # print("Checking down")
            if self.current_tile.down:
                    self.next_tile = self.map[self.current_tileR + 1][self.current_tileC]
                    self.current_tile = self.next_tile
                    self.current_tileR = self.current_tileR + 1
                    self.current_tile.rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
                    # print(self.current_tile.name)
                    return True
                    
        elif direction == 'left':
            # print("Checking Left")
            if self.current_tile.left:
                    self.next_tile = self.map[self.current_tileR][self.current_tileC-1]
                    self.current_tile = self.next_tile
                    self.current_tile.rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
                    self.current_tileC = self.current_tileC-1
                    # print(self.current_tile.name)
                    return True
                    
        elif direction == 'right':
            # print("Checking Right")
            if self.current_tile.right:
                    self.next_tile = self.map[self.current_tileR][self.current_tileC+1]
                    self.current_tile = self.next_tile
                    self.current_tile.rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
                    self.current_tileC = self.current_tileC+1
                    # print(self.current_tile.name)
                    return True
                    
        return False
