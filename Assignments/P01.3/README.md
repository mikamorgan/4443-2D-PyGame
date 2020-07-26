## P01.3 - CovidZAR.EIEIO cont.
### Mika Morgan
### Description:

This is a Python game similar to agar.io. This third part expands on the first two program portions, found [here](./../P01.2/README.md). The updated game code does the same as before, with the addition of a player animation. The planet player (used as an example sprite) now has an animated comet tail that follows behind the player. The tail grows as the player grows and fades as the player moves. The sample planet sprite provided will also turn to face the direction of movement, based on keyboard input. The player sprite spins when it hits a world border, in addition to displaying the red border wall.

### One important note
The player sprite changed in this third part of the project from a single image, to an animated image. The program now expects a folder of images in succession to create the animation. That changes the way the program is called, and accepted user input. The program player sprite will work best with the provided sample file, or a folder of sprites with 8 images, one for each direction.


The sample background and player image used in the example commands should display a scene as shown below. You can see the comet tail in various stages of the animation, plus the planet rotating based on the direction of movement:

<img src="comet_tail_1.png" width="400">
<img src="comet_tail_2.png" width="400">


When the player hits a world border, the sprite spins continuously as the wall is pressed. This, in addition to the red border line, help show the user they have reached a boundary and cannot continue in this direction.  


Example of boundary wall spin animation:

<img src="spin_animation_1.png" width="400">
<img src="spin_animation_2.png" width="400">

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [game_pt3.py](game_pt3.py)         | Main driver of my project that launches game.      |
|   2   | [bg.jpg](bg.jpg)           | Galaxy image used as possible background (but user can pass in a different file).     |
|   3   | [planet_sprite](./planet_sprite)         | Folder of planet images used as possible player (but user can pass in a different file).      |
|   4   | [comet_tail](./comet_tail)         | Folder of comet tail images used with sample player.      |
|   5   | [comet_tail_1.png](comet_tail_1.png)         | Example screenshots of game play.      |
|   6   | [comet_tail_2.png](comet_tail_2.png)         | Example screenshots of game play.      |
|   7   | [spin_animation_1.png](spin_animation_1.png)         | Example screenshots of game play.      |
|   8   | [spin_animation_2.png](spin_animation_2.png)         | Example screenshots of game play.      |
|   9   | [bg.mp3](bg.mp3)         | Background music: Deep Blue, courtesy of [bensound](https://www.bensound.com)     |


### Instructions

- Make sure you install Python on your device. Instructions and download can be found [here](https://www.python.org/downloads/). I used version Python 3.7.2, but there are updated versions available.
  
- The program expects seven parameters in the command line when ran:
  - the window title that will display at the top of the game screen
  - the file path for the background image that will fill the screen
  - the file path for the folder of images to be used as the main player
  - the width of the game screen
  - the height of the game screen
  - the starting player width
  - the starting player height

- Some things to note:
  - Parameters do not have to be in order, but you must use the = symbol in between the key and value
  - Argument key names must be entered exactly as the examples below
  - Be sure the file path is accessible from where you are calling (might have to include full path name)
  - PNG files work best for players, to preserve the transparent layer around your character

- Example Command:
    - `python <code_name> <window_title> <bg_image_filepath> <player_image_folder_filepath> <screen_width> <screen_height> <player_start_x> <player_start_y>`
    - `python game.py title="Move Player" bg_path=bg.jpg img_path=planet_sprite width=640 height=480 player_start_x=70 player_start_y=70`