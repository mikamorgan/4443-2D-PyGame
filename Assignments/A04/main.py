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
        col = 0

        for key in player_dictionary:
            if type(player_dictionary[key]) is list:
                lab = tk.Label(self, text=f"{key}\t:")
                lab.grid(row=row, column=col)
                for value in player_dictionary[key]:
                    col += 1
                    lab = tk.Label(self, text=f"{value}, ")
                    lab.grid(row=row, column=col)
            else:
                lab = tk.Label(self, text=f"{key}\t:\t{player_dictionary[key]}")
                lab.grid(row=row, column=col)

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