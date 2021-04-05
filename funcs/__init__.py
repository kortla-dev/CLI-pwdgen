#!/usr/bin/env python

import re, os

def getPwd():
    path_pattern = re.compile(r"\/?\w\:?(\\|\/)Users(\\|\/)[a-zA-Z0-9]+")
    path = path_pattern.match(os.getcwd())
    return path.group()

def getCurUserPwd():
    path_pattern = re.compile(r"\/?\w\:?(\\|\/)Users(\\|\/)[a-zA-Z0-9-_]+([a-zA-Z0-9-_\/\\]+)")
    path = path_pattern.match(os.getcwd())
    return path.group(3)
