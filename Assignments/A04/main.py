#!/usr/bin/env python

import sys, json, os
import tkinter as tk
from tkinter.font import Font

# GUI window is a subclass of the basic tkinter Frame object
class PlayerInfoFrame(tk.Frame):
    def __init__(self, master,player_dictionary):
        # Choose your font
        #appfont = font.Font(family='Courier New', size=12, weight='bold')
        
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        
        # Place frame into main window
        self.grid()

        # Create text box with player information
        row = 0
        col = 1

        for key in player_dictionary:

            if type(player_dictionary[key]) is list:
                front = tk.Label(self, text=f"{key}")
                front.grid(row=row, column=0, sticky=tk.W)

                mid   = tk.Label(self, text=f":")
                mid.grid(row=row, column=1)

                for value in player_dictionary[key]:
                    col += 1
                    back = tk.Label(self, text=f"{value},")
                    back.grid(row=row, column=col, sticky=tk.W)
            else:
                front = tk.Label(self, text=f"{key}")
                mid   = tk.Label(self, text=f":")
                back  = tk.Label(self, text=f"{player_dictionary[key]}")
                
                front.grid(row=row, column=0, sticky=tk.W)
                mid.grid(row=row, column=1)
                back.grid(row=row, column=2, sticky=tk.W)

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