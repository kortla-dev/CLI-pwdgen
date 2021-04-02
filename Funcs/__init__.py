#!/usr/bin/env python

import re, os

def getpwd():
    path_pattern = re.compile(r"\/?\w\:?(\\|\/)Users(\\|\/)[a-zA-Z0-9]+")
    path = path_pattern.match(os.getcwd())
    return path.group()