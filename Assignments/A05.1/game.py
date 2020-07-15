# Import and initialize the pygame library
import pygame, sys, os, json, pprint

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


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        x = int(kwargs['width'], 10)
        y = int(kwargs['height'], 10)
        
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def main(**kwargs):
    pygame.init()

    #Use the width and height passed into dictionary to set game window size
    #Need to convert values from string to int, specify using base 10
    x = int(kwargs['width'], 10)
    y = int(kwargs['height'], 10)

    BackGround = Background(kwargs['bg_path'], [0,0])

    player = pygame.image.load(kwargs['img_path'])
    player = pygame.transform.scale(player, (70, 70))
    player_rect = player.get_rect()

    #p_w = player.get_width()
    #p_h = player.get_height()

    p_x = x / 2 - player.get_width()
    p_y = y / 2 - player.get_height()

    # sets the window title
    pygame.display.set_caption(kwargs['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode([x,y])
    screen_rect=screen.get_rect()

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: p_y -= 2
        if keys[pygame.K_LEFT]: p_x -= 2
        if keys[pygame.K_DOWN]:  p_y += 2
        if keys[pygame.K_RIGHT]: p_x += 2
        #player.clamp_ip(screen_rect) # ensure player is inside screen

        # Draw / render
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(player, (p_x, p_y))
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    """
    This example has 5 required parameters, so after stripping the file name out of
    the list argv, I can test the len() of argv to see if it has 5 params in it.
    """
    argv = sys.argv[1:]

    if len(argv) < 5:
        print(len(argv))
        usage()

    args,kwargs = mykwargs(argv)

    # Create the game window passing in the dictionary of command line arguments
    main(**kwargs)