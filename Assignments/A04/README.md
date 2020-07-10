## A04 - Simple Python Program
### Mika Morgan
### Description:

This is a small Python program that reads and displays player information from a JSON file. The file name is passed in as a command line parameter, then the data is stored in a dictionary, and each key-value pair is displayed in a small GUI window using tKinter.

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [main.py](main.py)         | Main driver of my project that launches game.      |
|   2   | [player.json](player.json)         | JSON file that holds player information.      |
|   3   | [example.png](example.png)         | Sample screenshot of the code's  output.      |


### Instructions

- Make sure you install Python on your device. Instructions and download can be found [here](https://www.python.org/downloads/). I used version Python 3.7.2, but there are updated versions available.
- The program expects one parameter in the command line when ran, the name of the JSON file with the player information stored.

- Example Command:
    - `python <code_name> <input_JSON_file>`
    - `python main.py player.json`