from bs4 import BeautifulSoup
import html5lib
from bs4.diagnose import diagnose
import requests
import re

import csv

with open("Log_Links_3.csv","r") as links:
    with open('OTRSiteScrape2.txt','w') as outfile:  
        show_links = []
        
        for row in links:
            show_links.append(row)
#        print (show_links[0])
        num_links = len(show_links)
#        print (num_links)
        
        url = show_links[1]
        object_page = requests.get(url)
        html = object_page.text
        soup = BeautifulSoup(html, "html5lib")
            
        def has_size_attribute_but_no_color(tag):
            return tag.has_attr('size') and not tag.has_attr('color')
        
#
#        def only_3_and_5(size):
#            return size and not re.compile("1").search(size) 
#            return size and not re.compile("2").search(size)
#            return size and not re.compile("4").search(size)
        font_3 = soup.find_all("font", attrs={"size":"3"})
        font_5 = soup.find_all("font", attrs={"size":"5"})
        font_3_string = str(font_3)
        font_5_string = str(font_5)
        
        
#        print(soup.find_all(has_size_attribute_but_no_color))
        print(soup.find_all("font"))
#            
#        try: 