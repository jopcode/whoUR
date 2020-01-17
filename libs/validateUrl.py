from libs.colors import *
import urllib3
import re

# Validation of url
def validateUrl():
    url_input = str(input(P+"\n[+] Please Enter a Site:: "+B))
    pattern = re.compile(r'\bwww.\b')
    
    if pattern.match(url_input) is None :
        url_input = 'www.'+url_input    
    http = urllib3.PoolManager()
    
    try:
        url = http.request('GET', 'http://'+url_input)
    except urllib3.exceptions.HTTPError:
        print(lR+'Please Enter a Valid URL(www.example.com)')
        validateUrl()
    else:
        return url_input
