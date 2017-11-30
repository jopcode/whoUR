# -*- coding: utf-8 -*-
from libs.colors import *
from libs.checkUrl import checkUrl
from libs.saveSites import saveSites
from libs.randomDork import randomDork

from google import search
from urllib2 import HTTPError, URLError

def googleScanner():
    dork = raw_input(G+'\n[+] Please enter a dork to use(inurl:"index.php?id=") leave in blank for use a random dork:: '+B)
    if not dork:
        dork = randomDork()
        print B+'\n[!] Using '+G+dork
    try:
        hitLimit = int(raw_input(G+"[+] Please enter a number of hits(10):: "+B))
        if not hitLimit :
            raise ValueError('null')
    except ValueError:
            print lR+"\n[!] Please enter a Number\n"
            hitLimit = int(raw_input(G+"[+] Please enter a number of hits(10):: "+B))

    print P+"\n--------------------"
    print P+"-G O O G L E  S C A N N E R-"
    print P+"--------------------\n"
    print B+"[!] Scann in Process...\n"

    vulSites = []
    
    try:
        
        for url in search(dork, stop=hitLimit, start=0):
            
            print G+"[!] Checking "+B+url+"\n"
            
            try:
                isVul = checkUrl(url)
                if isVul == "true":
                    vulSites.append(url)
            except:
                continue
    
    except HTTPError:
        exit("[503] Service Unreachable")
    
    except URLError:
       exit("[504] Gateway Timeout")
    
    else:
        for vulnerable in vulSites:
            print G+'[!] '+B+vulnerable+G+' Has been vulnerable'
        
        if len(vulSites) == 0:
            print lR+'[!] 0 vulnerable sites has been found'
            return False

        saveSites(vulSites)