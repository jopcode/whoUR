# -*- coding: utf-8 -*-
from libs.colors import *
from libs.ipReverse import ip_reverse
from libs.whois import whois
from libs.dnsLookup import dns_lookup
from libs.adminFinder import admin_finder


def get_information(url_input):
    dicts_admins_page = 'dicts/adminspage.txt'

    print(P+'\n[-] 1) Whois Lookup')
    print(P+'[-] 2) DNS Lookup')
    print(P+'[-] 3) IP Reverse Lookup')
    print(P+'[-] 4) Admin Panel Finder\n')

    option_input = input(G+'[+] Please Enter a Choice Separated With Comma(1,2,3) or 0 for all:: '+B)
    options_selected = []
    option_input = option_input.split(',')

    for option in option_input:
        option = int(option)
        if option not in (0,1,2,3,4):
            print(lR+'[!] Option '+str(option)+' is Wrong.')
            get_information(url_input)
        options_selected.append(option)

    if len(options_selected) == 1 and options_selected[0] == 0:
        whois(url_input)
        dns_lookup(url_input)
        ip_reverse(url_input)
        admin_finder(url_input, dicts_admins_page)
    else:
        for option in options_selected:
            if option == 1:
                whois(url_input)
            elif option == 2:
                dns_lookup(url_input)
            elif option == 3:
                ip_reverse(url_input)
            elif option == 4:
                admin_finder(url_input, dicts_admins_page)
        get_information(url_input)
