from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re

import csv

url = "http://www.otrsite.com/logs/logb1155.htm"
object_page = requests.get(url)
html = object_page.text
soup = BeautifulSoup(html, "html.parser")


only_font_tags = SoupStrainer("font")    

font_3 = soup.find_all("font", attrs={"size":"3"})
font_5 = soup.find_all("font", attrs={"size":"5"})
show_data = str(font_5) + str(font_3)

def has_size_attribute_but_no_color(tag):
    return tag.has_attr('size') and not tag.has_attr('color')

def only_3_and_5(size):
    return size and not re.compile("1").search(size) 
    return size and not re.compile("2").search(size)
    return size and not re.compile("4").search(size)


#print(soup.find_all(has_size_attribute_but_no_color, size=only_3_and_5))

for a_show in soup.find_all(has_size_attribute_but_no_color, size=only_3_and_5):
    print(a_show.text)
        
