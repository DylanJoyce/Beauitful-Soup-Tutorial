#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:18:03 2020

@author: Dylan
"""

import requests
from bs4 import BeautifulSoup

results = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = results.content
soup = BeautifulSoup(src, 'lxml')

urls = []

for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])
    
print(urls)s