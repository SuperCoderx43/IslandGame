from GameController import GameController

class Runner:

    def __init__(self):
        self.playing = True
        # add stats and achievements
    
    def play(self):
        while(self.playing):
            # need menus and stuff
            newGame = GameController()
            newGame.main()
