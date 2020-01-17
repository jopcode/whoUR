from bs4 import BeautifulSoup
import urllib3,urllib
from libs.colors import *


# WHOIS Lookup
def whois(url_input):
    print(P+'\n-------------------------')
    print(P+'-W H O  I S  L O O K U P-')
    print(P+'-------------------------\n')
    print(B+'[!] Scann in Process...\n')
    http = urllib3.PoolManager()
    url = http.request('GET','http://api.hackertarget.com/whois/?q='+str(url_input)).data
    soup = BeautifulSoup(url, 'lxml')

    print(G+str(soup.p.string))
