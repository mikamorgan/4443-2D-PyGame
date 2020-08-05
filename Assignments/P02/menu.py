import sys
import pygame as pg
from state import State

class Menu(State):
    def __init__(self):
        super(Menu, self).__init__()
        self.persist["screen_color"] = "black"
        self.next_state = "LEVEL_01"
        pg.display.set_caption("Main Menu")
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.done = True

    def draw(self, surface):
        bg = pg.image.load("./assets/graphics/bg.jpg")
        bg = pg.transform.scale(bg,(800,600))

        title = pg.image.load("./assets/graphics/game_title.png")
        
        surface.blit(bg, (0,0))
        surface.blit(title, (10,150))

