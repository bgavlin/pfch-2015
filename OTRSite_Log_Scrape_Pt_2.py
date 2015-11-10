from bs4 import BeautifulSoup
from bs4 import SoupStrainer

import requests

import csv

with open("Log_Links_4.csv","r") as links:
    with open('OTRSiteScrape.txt','w') as outfile:  

        for a_link in links:
            url = a_link.strip()
            object_page = requests.get(url)
            html = object_page.text
        
            soup = BeautifulSoup(html, "html5lib")
            only_font_tags = SoupStrainer("font")  
            
            font_3 = soup.find_all("font", attrs={"size":"3"})
            font_5 = soup.find_all("font", attrs={"size":"5"})
            font_3_string = str(font_3)
            font_5_string = str(font_5)
            
            
        if font_5:
            outfile.write(font_5_string)
            outfile.write(font_3_string)
                
            