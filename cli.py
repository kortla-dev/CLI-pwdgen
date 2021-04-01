#!/usr/bin/env python

import os, sys, Funcs, pyperclip
from random import randint
import argparse as argp

class CLI_Prog():
    def __init__(self):
        parser = argp.ArgumentParser(
            description="CLI tool for generating passwords",
            usage="""cli.py <command> [<args>]\n\nThese are common Gen commands:\n  gen\tGenerates password"""
        )
        parser.add_argument("command", help="The command to run")
        
        # it gets the first argument after cli.py
        args = parser.parse_args(sys.argv[1:2])  # PS. would also be sys.argv[1]

        # gets the name of the func specified in command and calls it
        getattr(self, args.command)()
    
    def gen(self):
        parser = argp.ArgumentParser(
            description="Generates password",
            usage="cli.py gen [<args>]"
        )
        parser.add_argument("-s", "--symbols", type=str, default="default", help="File with the symbols you want to be used")
        parser.add_argument("-l", "--length", type=int, default=15, help="The length you want the password to be")
        parser.add_argument("-v", "--verbose", action="store_true", help="Gives more information")
        args = parser.parse_args(sys.argv[2:])  # it gets the rest of the optional arguments after gen
        
        passSyms = []
        
        with open(f"{Funcs.getpwd()}.pwdgen/{args.symbols}.txt") as f:
            passSyms += f.read().split()
        
        pwd = "".join(passSyms[randint(0, len(passSyms)-1)] for _ in range(args.length))
        
        if args.verbose:
            print(f"password generated is:\t{pwd}")
        
        pyperclip.copy(pwd)

if __name__=="__main__":
    CLI_Prog()
