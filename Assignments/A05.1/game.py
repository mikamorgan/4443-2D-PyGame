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
    print("Usage: python basic.py title=string img_path=string width=int height=int [jsonfile=string]")
    print("Example:\n\n\t python basic.py title='Game 1' img_path=./sprite.png width=640 height=480 \n")
    sys.exit()

colors = {
    'magenta':(255, 0, 255, 100),
    'cyan':(0, 255, 255, 100),
    'background':(255,255,255,100)
}

#class Player(pygame.sprite.Sprite):
    #x = int(kwargs['width'], 10)
    #y = int(kwargs['height'], 10)

    # Used to create player
 #   def __init__(self):
   #     pygame.sprite.Sprite.__init__(self)
   #     self.image = pygame.image.load(kwargs['img_path'])
   #     self.rect  = self.image.get_rect()
        #self.rect.center = (x / 2, y / 2)

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

    BackGround = Background('bg.jpg', [0,0])

    player = pygame.image.load(kwargs['img_path'])
    player = pygame.transform.scale(player, (70, 70))

    #p_w = player.get_width()
    #p_h = player.get_height()

    p_x = x / 2 - player.get_width()
    p_y = y / 2 - player.get_height()

    # sets the window title
    pygame.display.set_caption(kwargs['title'])

    # Set up the drawing window
    screen = pygame.display.set_mode([x,y])

    # Run until the user asks to quit
    running = True
    while running:
        screen.fill(colors['background'])

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p_x -= 5
                if event.key == pygame.K_RIGHT:
                    p_x += 5
                if event.key == pygame.K_UP:
                    p_y -= 5
                if event.key == pygame.K_DOWN:
                    p_y += 5

        # Draw / render
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(player, (p_x, p_y))
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__=='__main__':
    """
    This example has 4 required parameters, so after stripping the file name out of
    the list argv, I can test the len() of argv to see if it has 4 params in it.
    """
    argv = sys.argv[1:]

    if len(argv) < 4:
        print(len(argv))
        usage()

    args,kwargs = mykwargs(argv)

    # Create the game window passing in the dictionary of command line arguments
    main(**kwargs)