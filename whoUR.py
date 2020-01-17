import sys, os
import argparse
import urllib3, urllib
import re

# Modules
from libs.colors import *
from libs.selectChoice import select_choice

Parser = argparse.ArgumentParser(prog='whoUR.py', description='Tool for information gathering')
'''
this has been use in the future
Parser.add_argument('-d', '--dic-path', help='Dictonaries Path, Example: -d /root/', action='store', default='dicts/', dest='dicPath')
Parser.add_argument('-a', '--dic-adminspage', help='Admin Page dictonary, Example: -a adminspage.txt', action='store', default='adminspage.txt', dest='dicAdminsPage')

Args = Parser.parse_args()

# Dictonaries
dic_adminsPage = Args.dicPath +'/'+ Args.dicAdminsPage
'''
def main():
    print('\n')
    print(B+'             _                                ___  ')
    print(B+' __      __ | |__     ___      _   _   _ __  |__ \ ')
    print(B+' \ \ /\ / / | \_ \   / _ \    | | | | | |__|   / / ')
    print(B+'  \ V  V /  | | | | | (_) |   | |_| | | |     |_|  ')
    print(B+'   \_/\_/   |_| |_|  \___/     \__,_| |_|     (_)  ')
    print('\n')
    print(lC+'Beta 1.6                                       JopCode')
    print('\n')

    select_choice()

    print(lG+'\n---------')
    print(lG+'- C Y A -')
    print(lG+'---------\n')
    print(lR+'[+] Script by JopCode\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(lG+'\n---------')
        print(lG+'- C Y A -')
        print(lG+'---------\n')
        print(lR+'[+] Script by JopCode\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
