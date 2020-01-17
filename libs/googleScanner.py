# -*- coding: utf-8 -*-
from libs.colors import *
from libs.checkUrl import check_url
from libs.saveSites import save_sites
from libs.randomDork import random_dork

from googlesearch import search
import urllib3, urllib

def googleScanner():
    dork = input(G+'\n[+] Please enter a dork to use(inurl:"index.php?id=") leave in blank for use a random dork:: '+B)
    if not dork:
        dork = random_dork()
        print(B+'\n[!] Using '+G+dork)
    try:
        hit_limit = int(input(G+'[+] Please enter a number of hits(10):: '+B))
        if not hit_limit :
            raise ValueError('null')
    except ValueError:
            print(lR+'\n[!] Please enter a Number\n')
            hit_limit = int(input(G+'[+] Please enter a number of hits(10):: '+B))

    print(P+'\n--------------------')
    print(P+'-G O O G L E  S C A N N E R-')
    print(P+'--------------------\n')
    print(B+'[!] Scann in Process...\n')

    vulSites = []
    
    try:
        
        for url in search(dork, stop=hit_limit, start=0, pause = 2.0):
            
            print(G+'[!] Checking '+B+url+'\n')
            url, sep, tail = url.partition('&sa')
            try:
                isVul = check_url(url)
                if isVul == 'true':
                    vulSites.append(url)
            except urllib3.exceptions.MaxRetryError:
                continue
    
    except urllib3.exceptions.HTTPError:
        exit('[503] Service Unreachable')
    except urllib.error.HTTPError:
        print("HTTP Error please try later or use tor, proxy, vpn.")
        pass
    
    else:
        for vulnerable in vulSites:
            print(G+'[!] '+B+vulnerable+G+' Has been vulnerable')
        
        if len(vulSites) == 0:
            print(lR+'[!] 0 vulnerable sites has been found')
            return False

        save_sites(vulSites)