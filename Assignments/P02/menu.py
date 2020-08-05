import sys
import pygame as pg
from state import State

class Menu(State):
    def __init__(self):
        super(Menu, self).__init__()
        self.title = self.font.render("Splash Screen", True, pg.Color("dodgerblue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.persist["screen_color"] = "black"
        self.next_state = "LEVEL_01"
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            self.persist["screen_color"] = "gold"
            self.done = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.persist["screen_color"] = "dodgerblue"
            self.done = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
