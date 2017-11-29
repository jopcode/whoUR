import sys, os
import argparse
import urllib2, urllib
import re

# Modules
from libs.ipReverse import ipReverse
from libs.whois import whois
from libs.dnsLookup import dnsLookup
from libs.adminFinder import adminFinder
from libs.colors import *

Parser = argparse.ArgumentParser(prog='whoUR.py', description="Tool for information gathering")

Parser.add_argument("-d", "--dic-path", help="Dictonaries Path, Example: -d /root/", action="store", default="dics/", dest="dicPath")
Parser.add_argument("-a", "--dic-adminspage", help="Admin Page dictonary, Example: -a adminspage.txt", action="store", default="adminspage.txt", dest="dicAdminsPage")

Args = Parser.parse_args()

# Dictonaries
dic_adminsPage = Args.dicPath +'/'+ Args.dicAdminsPage

# Validation of url
def validateUrl():
    url_input = str(raw_input(P+"[+] Please Enter a Site:: "+B))
    pattern = re.compile(r'\bwww.\b')
    
    if pattern.match(url_input) is None :
        url_input = 'www.'+url_input    
    
    url = urllib2.Request('http://'+url_input)
    
    try:
        request = urllib2.urlopen(url)
    except urllib2.URLError:
        print lR+"Please Enter a Valid URL(www.example.com)"
        validateUrl()
    else:
        return url_input

# Select a Choice
def selectChoice(url_input):
    print G+"\n[-] 1) Whois Lookup"
    print G+"[-] 2) DNS Lookup"
    print G+"[-] 3) IP Reverse Lookup"
    print G+"[-] 4) Admin Panel Finder\n"

    option_input = raw_input(P+"[+] Please Enter a Choice Separated With Comma(1,2,3) or 0 for all:: "+B)
    options_selected = []
    option_input = option_input.split(',')

    for option in option_input:
        option = int(option)
        if option not in (0,1,2,3,4):
            print lR+"[!] Option "+str(option)+" is Wrong."
            selectChoice(url_input)
        options_selected.append(option)

    if len(options_selected) == 1 and options_selected[0] == 0:
        whois(url_input)
        dnsLookup(url_input)
        ipReverse(url_input)
        adminFinder(url_input)
    else:
        for option in options_selected:
            if option == 1:
                whois(url_input)
            elif option == 2:
                dnsLookup(url_input)
            elif option == 3:
                ipReverse(url_input)
            elif option == 4:
                adminFinder(url_input, dic_adminsPage)

def main():
    print '\n'
    print B+"             _                                ___  "
    print B+" __      __ | |__     ___      _   _   _ __  |__ \ "
    print B+" \ \ /\ / / | '_ \   / _ \    | | | | | '__|   / / "
    print B+"  \ V  V /  | | | | | (_) |   | |_| | | |     |_|  "
    print B+"   \_/\_/   |_| |_|  \___/     \__,_| |_|     (_)  "
    print '\n'
    print lC+"Beta 1.0                                       JopCode"
    print '\n'

    url_input = validateUrl()

    selectChoice(url_input)

    print lG+"\n---------"
    print lG+"- C Y A -"
    print lG+"---------\n"
    print lR+"[+] Script by JopCode\n"

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print lG+"\n---------"
        print lG+"- C Y A -"
        print lG+"---------\n"
        print lR+"[+] Script by JopCode\n"
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
