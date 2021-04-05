#!/usr/bin/env python

import os, sys, funcs, pyperclip
from random import randint
import argparse as argp

class CLI_Tri():
    def __init__(self):
        
        sysInput = sys.argv
        
        if sysInput[1] == "tri":
        
            cliCommand = sysInput[1:3]
            
            if cliCommand[-1][0] != "-" and cliCommand[-1] != "tri":
                keyw, com = cliCommand
                command = keyw+com
            else:
                command = cliCommand[0]
            
            getattr(self, command)()
        else:
            pass
    
    def tri(self):
        parser = argp.ArgumentParser(
            description="CLI tool for generating passwords",
            usage=f"""usage: tri [-v | --version] [-h | --help]\n\t{' '*3}<command> [<args>]\n\nThese are the most common Tri commands:\n  gen\tGenerates a password\n"""
        )
        parser.add_argument("-v", "--version", action="store_true", help="Gets your instalation version of Tri")
        args = parser.parse_args(sys.argv[2:]) # it gets the rest of the optional arguments after tri
        
        if args.version:
            print("You still have to implement this\n")
        else:
            print(parser.usage)
            
    def trigen(self):
        parser = argp.ArgumentParser(
            description="Generates a password and copies it to your clipboard",
            usage="""usage: tri gen [<options>]\n\t-s, --symbols\tFile with the symbols you want to be used\n\t-l, --length\tThe length you want the password to be\n\t-v, --verbose\tShow more information"""
        )
        parser.add_argument("-s", "--symbols", type=str, default="default", help="File with the symbols you want to be used")
        parser.add_argument("-l", "--length", type=int, default=15, help="The length you want the password to be")
        parser.add_argument("-v", "--verbose", action="store_true", help="Show more information")
        args = parser.parse_args(sys.argv[3:])  # it gets the rest of the optional arguments after gen
        
        passSyms = []
        
        try:
            with open(f"{funcs.getpwd()}/.pwdgen/{args.symbols}.txt", "r") as f:
                passSyms += f.read().split()
            
            pwd = "".join(passSyms[randint(0, len(passSyms)-1)] for _ in range(args.length))
            
            if args.verbose:
                print(f"Password generated is:\t{pwd}\n")
            
            pyperclip.copy(pwd)
        except FileNotFoundError:
            print("File specified does not exist\n")

if __name__=="__main__":
    CLI_Tri()
