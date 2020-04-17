# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:47:54 2018

@author: RICHKINWE
"""

import time
from datetime import datetime as dt


hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
blocked_website = ["www.udemy.com", "nairaland.com", "udemy.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("...Working hours")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in blocked_website:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " +website+"\n")
    else:
         with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_website):
                    file.write(line)
            file.truncate()
            print("...Relax hours")
            
        
    time.sleep(5)