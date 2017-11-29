from bs4 import BeautifulSoup
import urllib2, urllib
from libs.colors import *

# IP Reverse Lookup
def ipReverse(url_input):
    url = urllib.urlopen('http://api.hackertarget.com/reverseiplookup/?q='+url_input).read()
   
   
    soup = BeautifulSoup(url, "lxml")
    sites = soup.find('p')
    
    print P+"\n---------------------------------"
    print P+"-I P  R E V E R S E  L O O K U P-"
    print P+"---------------------------------\n"
    print B+"\n[!] Scann in Process..."
    print sites.text