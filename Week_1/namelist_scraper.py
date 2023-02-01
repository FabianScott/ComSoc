
# ALEXANDER WITTRUP
# 2019 POSTER NAMES SCRAPER

from bs4 import BeautifulSoup ##A package to work with HTML data
import requests #A package to make HTTP requests
import re
import numpy as np

LINK = "https://2019.ic2s2.org/posters/"
r = requests.get(LINK) 
soup = BeautifulSoup(r.content)

div = soup.find("div",{"class":"col-md-8 page-content-wrap"})
rawstring_list = str(div).split("\n")[5:-2]

name_list = []
for line in rawstring_list:
    if line.startswith("<li>"):
        line = line[4:]
    
    if line.startswith("<"):
        continue
    
    idx = line.find("<")
    if idx:
        line = line[:idx]
    
    line_list = re.split(", | and ", line)
    
    for name in line_list:
        name_list.append(name)

len(np.unique(name_list))