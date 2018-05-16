#!/usr/bin/python3                


import os                                            # to find platform information
import webbrowser                                    # Browser related task
import time                                          # For sleep function
import requests                                      # To get page source of an url
from bs4 import BeautifulSoup                        # Scrap particular information from the page source
from datetime import datetime, timedelta             # Date , Time related stuff
from pytz import timezone                            # To get timezone of a particular
import nmap                                          # For scanning the network
from ipwhois import IPWhois                          # For domain lookup purpose
import socket                                        # To get host ip using domain name 


 
## These are the task to be performed 

choice = '''                                                              
1. to search data on web
2. to search images related to data
3. find url on the first page of the given data
4. show current date and time
5. search data on default browser also detect paltform
6. show all the IPs on the current network
7. search detail (owner , email , contact) of the given domain , if avaliable .

Enter choice >>
'''


ch = int(input(choice))                                                         # Take user input


if ch==1:                                                                       # Search each input keyword on the web
    data = input("Enter data : ").strip().split()
    for i in data:
        webbrowser.open_new_tab('https://www.google.co.in/search?q={}'.format(i))
        time.sleep(1)

elif ch==2:                                                                     # Search images related to each input keyword
    data = input("Enter data : ").strip().split()
    for i in data:
        webbrowser.open_new_tab('https://www.google.co.in/search?q={}&source=lnms&tbm=isch'.format(i))
        time.sleep(1)

elif ch==3:                                                                     # Fetch url of the each input keyword from the homepage
    data = input("Enter data : ").strip().split()
    for i in data:
        url = 'https://www.google.co.in/search?q={}'.format(i)
        html_source = requests.get(url).content
        soup = BeautifulSoup(html_source , "lxml")
       
        test =True
        for link in soup.find_all('a'):
            if test:
                print("Url related to {}".format(i))
                print("********************************")
                test = False
            print(link.get('href'))

        
        print("***********END***************")   
        time.sleep(2)



elif ch==4:                                                                     # Show current date and time with timezone
    tzone = timezone('Asia/Kolkata')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    loc_dt = tzone.localize(datetime.now())
    print(loc_dt.strftime(fmt)) 


elif ch==5:                                                                     # Search each input keyword on default platform browser
    kernel = os.sys.platform
    data = input('Enter data : ').strip().split()

    if kernel=='win32':
        for i in data:
            webbrowser.get('windows-default').open_new_tab('https://www.google.co.in/search?q={}'.format(i))
            time.sleep(1)

    if kernel=='linux':
        for i in data:
            webbrowser.get('firefox').open_new_tab('https://www.google.co.in/search?q={}'.format(i))
            time.sleep(1)

    if kernel=='darwin':
        for i in data:
            webbrowser.get('safari').open_new_tab('https://www.google.co.in/search?q={}'.format(i))
            time.sleep(1)                




elif ch==6:                                                         # Search all host on the same network
    ip_addr = input("Enter Network IP : ")                          # Take network ip

    nmap_obj = nmap.PortScanner()                                   # Create nmap object
    nmap_obj.scan(hosts=ip_addr , arguments='-n -sP')               # -n : Never do DNS resolution  and -sP : for ping scan
    for host in nmap_obj.all_hosts():                               
        print(host)                                                 # Print available host on the network



elif ch==7:                                                         # Search information of the given domain (if avaliable)
    domain = input("Enter domain name : ")
    obj = IPWhois(socket.gethostbyname(domain))
    res = obj.lookup_whois()
    info = res['nets'][0]

    for title , detail in info.items():
        print('{} : {}'.format(title,detail))

