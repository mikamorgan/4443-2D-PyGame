# Import and initialize the pygame library
import pygame, sys, os, glob

#P01.2  Mika Morgan

# This is a Python game similar to agar.io. This second part expands on the game setup and player movement created in 
# P01.1. New game play added in this code is the background image is stretched to 5 times the game window width and 5 
# times the game window height. As the player moves, the top down view camera moves with them, scrolling around the 
# portion of the image within current view. When the player hits the image border, a red wall indicating the end of 
# the game world appears. The camera is allowed to scroll past the image end to keep the camera centered around the player 
# at all times. An empty black background pads the game play image to provide a buffer when the player reaches a game 
# border and the camera needs to stay centered around the player.

# Function that reads in the command line parameters and returns them as a dictionary, split around the =
def mykwargs(argv):
    '''
    Processes argv list into plain args and kwargs.
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}
        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def usage():
    # Params in square brackets are optional
    # The kwargs function script needs key=value to NOT have spaces
    print("Usage: python basic.py title=string img_path=string img_path=string width=int height=int [jsonfile=string]")
    print("Example:\n\n\t python basic.py title='Game 1' bg_path=bg.jpg img_path=sprite.png width=640 height=480 \n")
    sys.exit()

# Background function that creates the background image using the file path and screen
# sizes passed in as params. This function will be used to spawn groups of sprites in future
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        x = int(kwargs['width'], 10)
        y = int(kwargs['height'], 10)
        
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (x * 5, y * 5))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, folder_name):
        super(BasicSprite, self).__init__()
        self.images = []
        for image in glob.glob('./'+ folder_name +'/*.png'):
            self.images.append(pygame.image.load(image))

        self.index = 0
        self.image = self.images[self.index]

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def get_width(self):
        p_x = self.image.get_width()
        return p_x

    def get_height(self):
        p_y = self.image.get_height()
        return p_y
# Main function that creates background and sprite, controls movement, and checks for updates (keyboard entry)
def main(**kwargs):
    # Initialize PyGame
    pygame.init()

    # Use the width and height passed into dictionary to get game window size
    # Need to convert values from string to int, specify using base 10
    x = int(kwargs['width'], 10)
    y = int(kwargs['height'], 10)

    # Create variables to hold "camera position" for part of game world to display
    camX = 0
    camY = 0

    # Create colors for the world border alerts and empty background padding
    RED =   (255,0,0)
    BLACK = (0,0,0)

    # Use the Background function to create a background using the file path passed in as a parameter
    # Position it offset from the world boundary so the camera can stay with player, even on world edge
    empty_surface = pygame.Surface((1000, 1000))
    empty_surface.fill(BLACK)
    BackGround = Background(kwargs['bg_path'], [x/2,y/2])

    # Create a player using the file path passed in as a parameter
    # Set the initial size to the width and height passed in as parameters
    # Since the dictionary values are passed in as strings, convert them to ints in base 10 to use as size
    player = BasicSprite(kwargs['img_path'])
    player.image = player.images[3]
    player.image = pygame.transform.scale(player.image, (int(kwargs['player_start_x'], 10), int(kwargs['player_start_y'],10)))

    # Because the player size will change throughout the game, we need functions to continuously check size
    # This information will be used to set boundary windows (keep sprite on screen) and compare the player
    # size to virus sizes or other player sizes (needed for "eating")
    p_w = player.get_width()
    p_h = player.get_height()

    # Spawn the player in the middle of the game window
    p_x = x / 2 - p_w
    p_y = y / 2 - p_h

    # Create the comet tail animation sprite
    # Set the initial x and y offsets to 0
    comet = BasicSprite('comet_tail')
    com_X = 0
    com_Y = 0

    # Set the window title to what was passed in as a parameter
    pygame.display.set_caption(kwargs['title'])

    # Set up the drawing window using the width and height passed in as parameters
    screen = pygame.display.set_mode([x,y])
    screen_rect=screen.get_rect()

    # Load and play background music. -1 means loop forever
    pygame.mixer.music.load('bg.mp3')
    pygame.mixer.music.play(-1)

    # Game update. Run until the user asks to quit
    running = True
    while running:
        # Reset the comet tail offset each loop
        com_X = 0
        com_Y = 0

        # Check to see if the quit button was pressed
        # If it is, break out of the game play loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement based on keyboard entry
        # Use the arrow keys to change the player's x and y location
        # Need to use get_pressed() method instead of get events to allow for continuous movement
        # (if the button is held down). The 2 represents the player speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: 
            p_y -= 2
            camY -= 2
            com_Y += p_h
            player.image = player.images[3]
        if keys[pygame.K_LEFT]: 
            p_x -= 2
            camX -= 2
            com_X += p_w
            player.image = player.images[1]
        if keys[pygame.K_DOWN]:  
            p_y += 2
            camY += 2
            com_Y -= p_h
            player.image = player.images[0]
        if keys[pygame.K_RIGHT]: 
            p_x += 2
            camX += 2
            com_X -= p_w
            player.image = player.images[2]

        x = x * 5
        y = y * 5

        # Create boolean flags to hold whether or not the player is hitting a world border
        x_min = False
        x_max = False
        y_min = False
        y_max = False

        # Boundary check to keep the camera within the world. The screen boundary is 0-screen width and
        # 0-screen height. If the camera tries to go beyond one of these boundaries, reset it's location 
        # to the boundary line. Subtract the screen's width and height while checking the upper limits. 
        if camX < (-x/10): camX = (-x/10)
        if camX > (x - (x/5)): camX = x - (x/5)
        if camY < (-y/10): camY = (-y/10)
        if camY > (y - (y/5)): camY = y - (y/5)
        
        # Boundary check to keep the player on the screen. The screen boundary is 0-screen width and
        # 0-screen height. If the player tries to go beyond one of these boundaries, reset their location 
        # to the boundary line. Subtract the player's width and height while checking the upper limits
        # because the player location is based on the top, left corner. Offset the limit so the player
        # can't go offscreen the distance of the player size.
        if p_x > (x - p_w): 
            p_x = x - p_w
            x_max = True
        if p_x < 0: 
            p_x = 0
            x_min = True
        if p_y > (y - p_h): 
            p_y = y - p_h
            y_max = True
        if p_y < 0: 
            p_y = 0
            y_min = True

        x = x / 5
        y = y / 5

        comet.update()
        player.image = pygame.transform.scale(player.image, (int(kwargs['player_start_x'], 10), int(kwargs['player_start_y'],10)))

        # Draw / render the screen. Continuously draw the background to cover up images of old
        # player locations. Blit the player after the screen so it is top layer (visible)
        screen.blit(empty_surface, (0, 0))
        screen.blit(BackGround.image, (0 - camX,0 - camY))
        screen.blit(comet.image,(((p_x - p_w * 2) - camX + com_X),((p_y - p_h) - camY + com_Y)))
        screen.blit(player.image,(p_x - camX,p_y - camY))

        ## If the player is hitting a world border, display a red border line
        if x_min: pygame.draw.rect(screen,RED,(x/2,(0-y/2),5,y * 5))
        if y_min: pygame.draw.rect(screen,RED,((0-x/2),y/2,x * 5,5))
        if x_max: pygame.draw.rect(screen,RED,(x-5,(0-y/2),5,y*5))
        if y_max: pygame.draw.rect(screen,RED,((0-x/2),y-5,x*5,5))

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    """
    This example has 7 required parameters, so after stripping the file name out of
    the list argv, I can test the len() of argv to see if it has 7 params in it.
    """
    argv = sys.argv[1:]

    if len(argv) < 7:
        print(len(argv))
        usage()

    args,kwargs = mykwargs(argv)

    # Create the game window passing in the dictionary of command line arguments
    main(**kwargs)