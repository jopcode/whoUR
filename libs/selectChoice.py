# -*- coding: utf-8 -*-
from libs.googleScanner import googleScanner
from libs.getInformation import get_information
from libs.colors import *
from libs.validateUrl import validateUrl


# Select a Choice
def select_choice():
    
    print(B+'\n¿What you want do?\n')
    print(P+'[-] 1) SQLi Scanner')
    print(P+'[-] 2) Get information from a website\n')
    try:
        option_input = int(input(G+'[+] Please Enter a Choice Separated With Comma(1,2,3):: '+B))
        if option_input not in (1,2):
            print(lR+'[!] Option '+str(option_input)+' is Wrong.')
            select_choice()

        if option_input == 1:
            googleScanner()
        elif option_input == 2:
            url_input = validateUrl()
            get_information(url_input)
    except ValueError:
        print(lR+'[!] Please enter a Number')
        select_choice()
    select_choice()