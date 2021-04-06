#!/usr/bin/env python

import re, os

def getPwd():
    path_pattern = re.compile(r"\/?\w\:?(\\|\/)Users(\\|\/)[a-zA-Z0-9]+")
    path = path_pattern.match(os.getcwd())
    return path.group()

def termPwd():
    path_pattern = re.compile(r"\/?\w\:?(\\|\/)Users(\\|\/)[a-zA-Z0-9-_]+([a-zA-Z0-9-_\/\\]+)")
    path = path_pattern.match(os.getcwd())
    path.group(3)
    termPromt = "{0}@{1} ~{2}\n$ ".format(
        os.environ["USERNAME"],
        os.environ['COMPUTERNAME'],
        str(path.group(3)).replace("\\", "/")
    )
    return termPromt
