from bs4 import BeautifulSoup
import urllib2,urllib
from libs.colors import *

# WHOIS Lookup
def whois(url_input):
    print P+"\n-------------------------"
    print P+"-W H O  I S  L O O K U P-"
    print P+"-------------------------\n"
    print B+"[!] Scann in Process...\n"

    url = urllib2.urlopen('http://api.hackertarget.com/whois/?q='+url_input).read()
    soup = BeautifulSoup(url, 'lxml')

    print G+soup.p.string
