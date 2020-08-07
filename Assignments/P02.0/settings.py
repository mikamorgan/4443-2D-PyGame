# game options/settings
TITLE = "ADVENTURE GAME!"
WIDTH = 1200
HEIGHT = 670
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.1
PLAYER_GRAV = 0.8
PLAYER_JUMP = 19

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 20
MOB_FREQ = 2000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# Starting platforms
PLATFORM_LIST_1 = [(0, HEIGHT - 60),
                 (95, 400),
                 (105, 420),
                 (300, HEIGHT - 50),
                 (350, 320),
                 (620, 400),
                 (820, 420),
                 (920, 450),
                 (1000, HEIGHT - 50),
                 (WIDTH - 130, HEIGHT - 60)]

PLATFORM_LIST_2 = [(40, HEIGHT - 50),
                 (10, 410),
                 (5, 220),
                 (340, HEIGHT - 140),
                 (380, 340),
                 (550, 400),
                 (820, 420),
                 (920, 450),
                 (1000, HEIGHT - 60),
                 (WIDTH - 130, HEIGHT - 160)]

PLATFORM_LIST_3 = [(0, HEIGHT - 60),
                 (10, 440),
                 (20, 240),
                 (300, HEIGHT - 50),
                 (600, 300),
                 (700, 700),
                 (820, 420),
                 (920, 450),
                 (1000, HEIGHT - 60),
                 (WIDTH - 130, HEIGHT - 50)]
# define colors
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE