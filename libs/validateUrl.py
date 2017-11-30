from libs.colors import *
import urllib2
import re

# Validation of url
def validateUrl():
    url_input = str(raw_input(P+"\n[+] Please Enter a Site:: "+B))
    pattern = re.compile(r'\bwww.\b')
    
    if pattern.match(url_input) is None :
        url_input = 'www.'+url_input    
    
    url = urllib2.Request('http://'+url_input)
    
    try:
        request = urllib2.urlopen(url)
    except urllib2.URLError:
        print lR+"Please Enter a Valid URL(www.example.com)"
        validateUrl()
    else:
        return url_input
