from bs4 import BeautifulSoup
from bs4 import SoupStrainer

import requests

import csv

with open("Log_Links_3.csv","r") as links:
    with open('OTRSiteScrape2.txt','w') as outfile:  

        show_links = []
        
        for row in links:
            show_links.append(row)
            
        link = iter(show_links)
        num_links = len(show_links)
        
        url = show_links[0]
        print(url)
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
        # print(font_5_string)
        
        try:
            url = next(link)
            print(url)
        except:
            print ("error")
    
        