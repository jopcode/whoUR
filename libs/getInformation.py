# -*- coding: utf-8 -*-
from libs.colors import *
from libs.ipReverse import ipReverse
from libs.whois import whois
from libs.dnsLookup import dnsLookup
from libs.adminFinder import adminFinder

def getInformation(url_input):
    dic_adminsPage = "dics/adminspage.txt"

    print P+"\n[-] 1) Whois Lookup"
    print P+"[-] 2) DNS Lookup"
    print P+"[-] 3) IP Reverse Lookup"
    print P+"[-] 4) Admin Panel Finder\n"

    option_input = raw_input(G+"[+] Please Enter a Choice Separated With Comma(1,2,3) or 0 for all:: "+B)
    options_selected = []
    option_input = option_input.split(',')

    for option in option_input:
        option = int(option)
        if option not in (0,1,2,3,4):
            print lR+"[!] Option "+str(option)+" is Wrong."
            getInformation(url_input)
        options_selected.append(option)

    if len(options_selected) == 1 and options_selected[0] == 0:
        whois(url_input)
        dnsLookup(url_input)
        ipReverse(url_input)
        adminFinder(url_input,dic_adminsPage)
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
        getInformation(url_input)
