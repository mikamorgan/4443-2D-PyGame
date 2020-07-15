## A05 - CovidZAR.EIEIO
### Mika Morgan
### Description:

This is a Python game similar to agar.io. This first part sets up the game window based on user input passed in as command line arguments. The user can designate the window title, screen size, and sprite image for the player. A GUI window will spawn to the specified size and a galaxy background image will fill the screen (scaled to fit). A single player will spawn on the window, that can be moved using the up, down, left, and right arrow keys on the keyboard. The player will appear as the image passed in during execution.

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [game.py](game.py)         | Main driver of my project that launches game.      |
|   2   | [bg.jpg](bg.jpg)           | Galaxy image used as the background for all builds.      |
|   3   | [sprite.png](sprite.png)         | Possible player image (but user can pass in a different file).      |


### Instructions

- Make sure you install Python on your device. Instructions and download can be found [here](https://www.python.org/downloads/). I used version Python 3.7.2, but there are updated versions available.
- The program expects one parameter in the command line when ran, the name of the JSON file with the player information stored.

- Example Command:
    - `python <code_name> <input_JSON_file>`
    - `python main.py player.json`