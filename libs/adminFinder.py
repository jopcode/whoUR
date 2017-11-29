from libs.colors import *
import urllib2, urllib

# Admin Pages Finder
def adminFinder(url_input, dic_adminsPage):
    print P+"\n-------------------------"
    print P+"-A D M I N  F I N D E R -"
    print P+"-------------------------\n"
    print B+"[!] Scann in Process...\n"
    with open(dic_adminsPage) as f:
        adminPageFound = []
        adminPageNotFound = 0
        contents = f.readlines()
        print P+'[+] Please be Patient, This May Take a While\n'
        for content in contents:
            url_request = url_input+'/'+content
            url = urllib2.Request('http://'+url_request)
            try:
                request = urllib2.urlopen(url)
            except urllib2.HTTPError as e:
                if e.code == 401:
                    adminPageFound.append('http://'+url_request)
                else:
                    ++adminPageNotFound
            except urllib2.URLError:
                pass
            else:
                if request.url == url_request:
                    adminPageFound.append('http://'+request.url)
                else:
                    ++adminPageNotFound

        print G+'[!] Admin Pages Found: '+str(len(adminPageFound))

        for page in adminPageFound:
            print lB+'\n[+] '+ page
