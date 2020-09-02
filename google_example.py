#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:53:20 2020

@author: Dylan
"""

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

# print(result.status_code)
# print(result.headers)

src = result.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
# print(links)
# print('\n')

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
        


