import sys
import pygame as pg
from state import State

class Gameover(State):
    def __init__(self):
        super(Gameover, self).__init__()
        self.persist["screen_color"] = "black"
        self.next_state = "MENU"
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True


    def draw(self, surface):
        bg = pg.image.load("./assets/graphics/game_over.jpg")
        bg = pg.transform.scale(bg,(800,600))
        surface.blit(bg, (0,0))
