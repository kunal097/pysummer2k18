#!/usr/bin/python3                

import webbrowser
import time
import requests
from bs4 import BeautifulSoup


choice = '''
1. to search data on web
2. to search images related to data
3. find url on the first page of the given data
4. show current date and time
5. search data on default browser
6. show all the IPs on the current network
7. search detail (owner , email , contact) if avaliable , of the given domain.

Enter choice >>
'''


ch = int(input(choice))


if ch==1:
    data = input("Enter data : ").split()
    for i in data:
        webbrowser.open_new_tab('https://www.google.co.in/search?q={}'.format(i))
        time.sleep(1)

elif ch==2:
    data = input("Enter data : ").split()
    for i in data:
        webbrowser.open_new_tab('https://www.google.co.in/search?q={}&source=lnms&tbm=isch'.format(i))
        time.sleep(1)

elif ch==3:
    data = input("Enter data : ").split()
    for i in data:
        url = 'https://www.google.co.in/search?q={}'.format(i)
        html_source = requests.get(url).content
        soup = BeautifulSoup(html_source)



