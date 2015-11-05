from bs4 import BeautifulSoup

import requests
import csv

url = "http://www.otrsite.com/otrsite/radiolog/"
object_page = requests.get(url)
html = object_page.text

soup = BeautifulSoup(html, "html.parser")

all_links = soup.find_all("a")
#select_links = soup.find_all(

with open('Log_Links_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")

    for a_link in all_links:
        
        link = a_link.get('href')
        if link:
            link_text = a_link.text
            link_length = len(link)
            link_stripped = link[2:link_length]
            html = "http://www.otrsite.com/otrsite" + link_stripped
            writer.writerow([html])