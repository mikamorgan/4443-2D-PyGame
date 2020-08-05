import sys
import pygame as pg

from game import Game
from state import State
from splash_state import SplashScreen
from menu import Menu
from level_01 import Level_01
from level_02 import Level_02
from level_03 import Level_03
from gameover import Gameover


#########################
#          Main         #
#     Entry Point       #
#########################

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))
    states = {"SPLASH": SplashScreen(),
              "MENU":   Menu(),
              "LEVEL_01": Level_01(),
              "LEVEL_02": Level_02(),
              "LEVEL_03": Level_03(),
              "GAMEOVER": Gameover()}

    game = Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()
