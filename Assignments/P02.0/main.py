import pygame as pg
import random
from settings import *
from sprites import Spritesheet
from sprites import Platform
from sprites import Player
from sprites import Cloud
from sprites import Pow
from sprites import Mob
from sprites import Portal
from sprites import Shortcut
from os import path


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        # load spritesheet image
        img_dir = path.join(self.dir, 'img')
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        # cloud images
        self.cloud_images = []
        for i in range(1, 4):
            self.cloud_images.append(pg.image.load(path.join(img_dir, 'cloud{}.png'.format(i))).convert())
        # load sounds
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'hop.wav'))
        self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir, 'carrot.wav'))
        self.portal_sound = pg.mixer.Sound(path.join(self.snd_dir, 'portal.wav'))
        self.game_over_sound = pg.mixer.Sound(path.join(self.snd_dir, 'game_over.wav'))

    def new(self, level):
        # start a new game
        if level == 5:
            self.playing = False
            g.show_go_screen()

        self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        self.portal = pg.sprite.Group()
        self.shortcut = pg.sprite.Group()
        self.player = Player(self)

        pg.mixer.music.load(path.join(self.snd_dir, 'gameplay.mp3'))
        pg.mixer.music.set_volume(.3)
        pg.mixer.music.play(loops=-1)

        if level == 1:
            for plat in PLATFORM_LIST_1:
                Platform(self, *plat)
        if level == 2:
            for plat in PLATFORM_LIST_2:
                Platform(self, *plat)
        if level == 3:
            for plat in PLATFORM_LIST_3:
                Platform(self, *plat)

        Portal(self)
        Shortcut(self)

        self.mob_timer = 0

        for i in range(8):
            c = Cloud(self)
            c.rect.y += 500
        self.run(level)

    def run(self, level):
        # Game Loop
        #pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw(level)
        #pg.mixer.music.fadeout(500)

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

        for cloud in self.shortcut:
            cloud.rect.x += 2

        # spawn a mob?
        now = pg.time.get_ticks()
        if now - self.mob_timer > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Mob(self)

        # hit mobs?
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False, pg.sprite.collide_mask)
        if mob_hits:
            self.playing = False
            level = 5
            pg.mixer.music.fadeout(500)
            g.show_go_screen()


        portal_collide = pg.sprite.spritecollide(self.player, self.portal, True)
        if portal_collide:
            self.playing = False
            self.portal_sound.play()


        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                   self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

            ride = pg.sprite.spritecollide(self.player, self.shortcut, False)
            if ride:
                for cloud in ride:
                    cloud.rect.y += .5
                    self.player.pos.x = cloud.rect.x + 30
                    self.player.pos.y = cloud.rect.y + 20
                    self.player.vel.y = 0
                    self.player.jumping = False


        # if player collects a carrot
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
        for pow1 in pow_hits:
            self.boost_sound.play()
            self.score += 1

        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False
            level = 5
            pg.mixer.music.fadeout(500)
            g.show_go_screen()
            


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self, level):
        # Game Loop - draw
        img_dir = path.join(self.dir, 'img')
        if level == 1:
            bg = pg.image.load(path.join(img_dir, 'level_1.jpg'))
            bg = pg.transform.scale(bg,(WIDTH,HEIGHT))
            self.screen.blit(bg, (0,0))
        elif level == 2:
            bg = pg.image.load(path.join(img_dir, 'level_2.jpg'))
            bg = pg.transform.scale(bg,(WIDTH,HEIGHT))
            self.screen.blit(bg, (0,0))
        elif level == 3:
            bg = pg.image.load(path.join(img_dir, 'level_3.jpg'))
            bg = pg.transform.scale(bg,(WIDTH,HEIGHT))
            self.screen.blit(bg, (0,0))

        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pg.mixer.music.load(path.join(self.snd_dir, 'bg.mp3'))
        pg.mixer.music.play(loops=-1)

        img_dir = path.join(self.dir, 'img')
        bg = pg.image.load(path.join(img_dir, 'splash.jpg'))
        bg = pg.transform.scale(bg,(WIDTH,HEIGHT))
        self.screen.blit(bg, (0,0))
        
        waiting = True
        cloud = pg.image.load(path.join(img_dir, 'cloud1.png'))
        x = 0
        y = random.randint(0, HEIGHT / 2)

        while waiting:
            self.clock.tick(FPS)
            self.screen.blit(bg, (0,0))
            self.screen.blit(cloud, (x,y))
            pg.display.flip()

            x += 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False


    def show_menu_screen(self):
        img_dir = path.join(self.dir, 'img')
        bg = pg.image.load(path.join(img_dir, 'bg.jpg'))
        bg = pg.transform.scale(bg,(WIDTH,HEIGHT))
        self.screen.blit(bg, (0,0))

        title_img = pg.image.load(path.join(img_dir, 'game_title.png'))       
        cloud = pg.image.load(path.join(img_dir, 'cloud1.png'))
        x = 0
        y = random.randint(0, HEIGHT / 2) 
        y2 = random.randint(0, HEIGHT / 2)
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            self.screen.blit(bg, (0,0))
            self.screen.blit(title_img, (210, 100))

            self.draw_text("ARROW KEYS to move, SPACEBAR to jump", 30, GREY, WIDTH / 2, 420)
            self.draw_text("Collect carrots to score. Avoid the grumpy clouds!", 30, GREY, WIDTH / 2, 480)
            self.draw_text("Press any key to play", 30, GREY, WIDTH / 2, 515)
            self.draw_text("High Score: " + str(self.highscore), 30, GREY, WIDTH / 2, 30)
            self.screen.blit(cloud, (x,y))
            self.screen.blit(cloud, (WIDTH - x,y2))
            pg.display.flip()
            x += 1

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
        
        pg.display.flip()
        pg.mixer.music.fadeout(500)

    def show_go_screen(self):
        # game over/continue
        #if not self.running:
        #    return
        self.game_over_sound.play()

        img_dir = path.join(self.dir, 'img')
        bg = pg.image.load(path.join(img_dir, 'game_over.jpg'))
        bg = pg.transform.scale(bg,(WIDTH,HEIGHT))
        self.screen.blit(bg, (0,0))

        self.draw_text("Score: " + str(self.score), 50, WHITE, WIDTH / 2, HEIGHT / 2 + 150)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 50, WHITE, WIDTH / 2, HEIGHT / 2 - 100)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 50, WHITE, WIDTH / 2, HEIGHT / 2 - 250)
        pg.display.flip()

        self.wait_for_key()
        self.running = False

    def wait_for_key(self):
        waiting = True

        while waiting:
            self.clock.tick(FPS)
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
g.show_menu_screen()
level = 1
while g.running:
    g.new(level)
    level += 1
    g.new(level)
    level += 1
    g.new(level)

g.show_go_screen()
pg.quit()