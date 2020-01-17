from libs.colors import *
import urllib3, urllib


# Admin Pages Finder
def admin_finder(url_input, dic_adminsPage):
    print(P+'\n-------------------------')
    print(P+'-A D M I N  F I N D E R -')
    print(P+'-------------------------\n')
    print(B+'[!] Scann in Process...\n')

    with open(dic_adminsPage) as f:
        admin_page_found = []
        admin_page_not_found = 0
        contents = f.readlines()
        print(P+'[+] Please be Patient, This May Take a While\n')
        http = urllib3.PoolManager()
        for content in contents:
            url_request = url_input+'/'+content
            try:
                url = http.request('GET', 'http://'+url_request)
            except urllib3.exceptions.HTTPError as e:
                if e == 401:
                    admin_page_found.append('http://'+url_request)
                else:
                    ++admin_page_not_found
            except urllib3.exceptions.RequestError:
                pass
            else:
                admin_page_found.append('http://' + url_request)

        print(G+'[!] Admin Pages Found: '+str(len(admin_page_found)))

        for page in admin_page_found:
            print(lB+'\n[+] '+ page)
