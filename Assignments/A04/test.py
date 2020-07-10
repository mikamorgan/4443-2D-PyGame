import sys
import os
import json

if __name__ == "__main__":
    # Open json file with player information
    fpath = sys.argv[0]

    f = open(fpath,"r")
    data = f.read()
    f.close()

    player = json.loads(data)

    print(data)