from libs.colors import *
from bs4 import BeautifulSoup
import urllib3


# DNS Lookup
def dns_lookup(url_input):
    print(P+'\n--------------------')
    print(P+'-D N S  L O O K U P-')
    print(P+'--------------------\n')
    print(B+'[!] Scann in Process...\n')

    http = urllib3.PoolManager()
    url = http.request('GET','https://api.hackertarget.com/dnslookup/?q='+url_input).data
    soup = BeautifulSoup(url, 'lxml')
    print(G+soup.p.string)
