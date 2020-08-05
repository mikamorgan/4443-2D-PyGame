import sys
import pygame as pg
from state import State

class SplashScreen(State):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.persist["screen_color"] = "black"
        self.next_state = "MENU"
        pg.display.set_caption("Loading")
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.done = True

    def draw(self, surface):
        bg = pg.image.load("./assets/graphics/splash.jpg")
        bg = pg.transform.scale(bg,(800,600))
        surface.blit(bg, (0,0))
