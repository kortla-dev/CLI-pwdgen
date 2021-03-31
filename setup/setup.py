#!/usr/bin/env python

import os, re

def getpwd():
    path_pattern = re.compile(r"\/?\w\:?(\\|\/)Users(\\|\/)[a-zA-Z0-9]+(\\|\/)?")
    path = path_pattern.match(os.getcwd())
    return path.group()

def create_default(path):
    with open(f"{path}/default.txt", "w") as f:
        print(*[
            "a", "b", "c", "d",
              "e", "f", "g", "h",
              "i", "j", "k", "l",
              "m", "n", "o", "p",
              "q", "r", "s", "t",
              "u", "v", "w", "x",
              "y", "z"
              ], file=f)
        f.close()

def setup():
    path = f"{getpwd()}.pwdgen"

    if os.path.exists(path):
        if os.path.exists(f"{path}/default.txt"):
            pass
        else:
            create_default(path)
    else:
        os.mkdir(path)
        create_default(path)

if __name__=="__main__":
    setup()
