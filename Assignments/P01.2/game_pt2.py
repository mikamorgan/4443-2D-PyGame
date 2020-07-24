# Import and initialize the pygame library
import pygame, sys, os

#A05.1  Mika Morgan

# This is a Python game similar to agar.io. This first part sets up the game window based on user input 
# passed in as command line arguments. The user can designate the window title, screen size, background image, 
# sprite image, and sprite size for the player. A GUI window will spawn to the specified size and the specified
# background image will fill the screen (scaled to fit). A single player will spawn in the middle of the window, 
# using the image and size passed in.The player can be moved using the up, down, left, and right arrow keys on the 
# keyboard. Because this is a 2D game using a top-down perspective, the up and down arrows move the player's 
# y position on the screen, and the left and right arrows move the player's x position on the screen.

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

# Main function that creates background and sprite, controls movement, and checks for updates (keyboard entry)
def main(**kwargs):
    # Initialize PyGame
    pygame.init()

    # Use the width and height passed into dictionary to get game window size
    # Need to convert values from string to int, specify using base 10
    x = int(kwargs['width'], 10)
    y = int(kwargs['height'], 10)

    camX = 0
    camY = 0

    RED = (255,0,0)

    # Use the Background function to create a background using the file path passed in as a parameter
    # Position it at 0,0 (top left corner of game window), and scale it to fit window size
    BackGround = Background(kwargs['bg_path'], [0,0])

    # Create a player using the file path passed in as a parameter
    # Set the initial size to the width and height passed in as parameters
    # Since the dictionary values are passed in as strings, convert them to ints in base 10 to use as size
    player = pygame.image.load(kwargs['img_path'])
    player = pygame.transform.scale(player, (int(kwargs['player_start_x'], 10), int(kwargs['player_start_y'],10)))

    # Because the player size will change throughout the game, we need functions to continuously check size
    # This information will be used to set boundary windows (keep sprite on screen) and compare the player
    # size to virus sizes or other player sizes (needed for "eating")
    p_w = player.get_width()
    p_h = player.get_height()

    # Spawn the player in the middle of the game window
    p_x = x / 2 - p_w
    p_y = y / 2 - p_h

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
        if keys[pygame.K_LEFT]: 
            p_x -= 2
            camX -= 2
        if keys[pygame.K_DOWN]:  
            p_y += 2
            camY += 2
        if keys[pygame.K_RIGHT]: 
            p_x += 2
            camX += 2

        x = x * 5
        y = y * 5

        x_min = False
        x_max = False
        y_min = False
        y_max = False

        if camX < 0: camX = 0
        #if camX > x: camX = x
        if camY < 0: camY = 0
        #if camY > y: camY = y
        
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
            x_max = True
        if p_y < 0: 
            p_y = 0
            y_min = True

        x = x / 5
        y = y /5

        # Draw / render the screen. Continuously draw the background to cover up images of old
        # player locations. Blit the player after the screen so it is top layer (visible)
        screen.blit(BackGround.image, (0 - camX,0 - camY))
        screen.blit(player,(p_x - camX,p_y - camY))
        if x_min: pygame.draw.rect(screen,RED,(0,0,5,y))
        if y_min: pygame.draw.rect(screen,RED,(0,0,x,5))
        if x_max: pygame.draw.rect(screen,RED,(x,0,5,y))
        if y_max: pygame.draw.rect(screen,RED,(0,y,5,x))
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