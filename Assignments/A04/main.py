import tkinter as tk
import sys
import os
import json

# GUI window is a subclass of the basic tkinter Frame object
class PlayerInfoFrame(tk.Frame):
    def __init__(self, master,data):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()

        # Create text box with player information
        fName = tk.Label(self, text=f"Hello ")
        fName.grid(row=0, column=0)

        lName = tk.Label(self, text=f"Hello ")
        lName.grid(row=1, column=0)

        rank = tk.Label(self, text=f"Hello")
        rank.grid(row=2, column=0)

        speed = tk.Label(self, text=f"Hello ")
        speed.grid(row=3, column=0)

        power = tk.Label(self, text=f"Hello")
        power.grid(row=2, column=0)

        health = tk.Label(self, text=f"Hello ")
        health.grid(row=3, column=0)

# Spawn window
if __name__ == "__main__":
    # Open json file with player information
    fpath = sys.argv[0]

    f = open(fpath,"r")
    data = f.read()
    f.close()

    player = json.loads(data)

    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("Player: ")
    # Instantiate HelloWorldFrame object
    player_frame = PlayerInfoFrame(root, data)
    # Start GUI
    player_frame.mainloop()