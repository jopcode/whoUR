from bs4 import BeautifulSoup
import urllib3, urllib
from libs.colors import *


# IP Reverse Lookup
def ip_reverse(url_input):
    http = urllib3.PoolManager()
    url = http.request('GET','http://api.hackertarget.com/reverseiplookup/?q='+str(url_input)).data
   
    soup = BeautifulSoup(url, 'lxml')
    sites = soup.find('p')
    
    print(P+'\n---------------------------------')
    print(P+'-I P  R E V E R S E  L O O K U P-')
    print(P+'---------------------------------\n')
    print(B+'\n[!] Scann in Process...')
    print(sites.text)