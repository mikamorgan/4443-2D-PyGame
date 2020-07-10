#!/usr/bin/env python

import sys, json, os
import tkinter as tk

# GUI window is a subclass of the basic tkinter Frame object
class PlayerInfoFrame(tk.Frame):
    def __init__(self, master,player_dictionary):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()

        # Create text box with player information
        row = 0

        for info in player_dictionary:
            lab = tk.Label(self, text=f"{info} \t: {info}")
            lab.grid(row=row, column=0)

            row += 1

# Spawn window
if __name__ == "__main__":
    # Open json file with player information (get file name as command line paramater)
    with open(sys.argv[1], 'r') as f:
        data = f.read()
        f.close()

        player_dictionary = json.loads(data)

    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("Player: ")
    # Instantiate PlayerInfoFrame object, pass data dictionary
    player_frame = PlayerInfoFrame(root, player_dictionary)
    # Start GUI 
    player_frame.mainloop()