# -*- coding: utf-8 -*-

from libs.colors import *


def save_sites(sites):
    want_save = input('\n[!] '+lP+str(len(sites)) + ' Sites has been founds, ¿You want save this?(Y/n):: '+B)

    if not want_save or want_save == 'y'  or want_save == 'Y' or want_save == 'yes' or want_save == 'Yes':
        where_save = input(G+' \n[+] ¿Where you want save sites.txt?(/home/someplace) by default in this folder:: '+B)
        if not where_save:
            where_save = '.'

        f = open(where_save+'/sites.txt', 'a')
        
        for site in sites:
            f.write(site+'\n')
        
        f.close
        print(lB+'[+] All sites has been saved!')
    
    elif want_save == 'n' or want_save == 'N' or want_save == 'no' or want_save == 'No':
        for site in sites:
            print(lR+'[!] '+b+site+lR+' is vulnerable but not saved.')
    
    else:
        print(lR+'[!] Please enter a valid option (yes/no)')
        save_sites()

