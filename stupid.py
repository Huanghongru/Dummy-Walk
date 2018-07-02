import os
import sys
import time

class dummy(object):
    """
    A dummy walking matchsticking man
    """
    def __init__(self):
        self.frame = [
                "                   ____                     ",
                "                  / 0 0\ Watching Football..",
                "                  \__v_/                    ",
                "                   |> |--                   ",
                "                  _\__\                     ",
                "                                            ",
                "                   ____                     ",
                "                  / - -\ Watching Football..",
                "                  \__v_/                    ",
                "                   |> |--                   ",
                "                  _\__\                     ",
                "                                            "]

    def run(self):
        while True:
            for f in self.frame:
                if not f.strip():
                    time.sleep(1.5)
                    os.system('clear')
                sys.stdout.write(f+'\n')
                sys.stdout.flush()




d = dummy()
d.run()

