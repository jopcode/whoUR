# -*- coding: utf-8 -*-

from libs.colors import *

def saveSites(sites):
    wantSave = raw_input('\n[!] '+lP+str(len(sites)) + ' Sites has been founds, ¿You want save this?(Y/n):: '+B)

    if not wantSave or wantSave == "y"  or wantSave == "Y" or wantSave == "yes" or wantSave == "Yes":
        whereSave = raw_input(G+' \n[+] ¿Where you want save sites.txt?(/home/someplace) by default in this folder:: '+B)
        if not whereSave:
            whereSave = "."

        f = open(whereSave+'/sites.txt', 'a')
        
        for site in sites:
            f.write(site+'\n')
        
        f.close
        print lB+"[+] All sites has been saved!"
    
    elif wantSave == "n" or wantSave == "N" or wantSave == "no" or wantSave == "No":
        for site in sites:
            print lR+'[!] '+b+site+lR+' is vulnerable but not saved.'
    
    else:
        print lR+"[!] Please enter a valid option (yes/no)"
        saveSites()

