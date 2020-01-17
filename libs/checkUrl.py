import urllib3
import re
from libs.colors import *
from bs4 import BeautifulSoup


def check_url(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    url_fixed = url + '\''
    http = urllib3.PoolManager()
    request = http.request('GET', url_fixed, headers=hdr)
    soup = BeautifulSoup(request.data, 'lxml')
    find_error = soup.findAll(text=re.compile("MySQL"))

    if find_error:
        return str("true")