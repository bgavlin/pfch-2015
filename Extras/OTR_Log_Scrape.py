from bs4 import BeautifulSoup

import requests
import csv

url = "http://old-time.com/otrlogs2/index.html"
object_page = requests.get(url)
html = object_page.text

soup = BeautifulSoup(html, "html.parser")

all_links = soup.find_all("a")

with open('Log_Links.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=" ", skipinitialspace = True)

    for a_link in all_links:
        link = a_link.get('href')
    
        if link:
            if "txt" in link:
                html="http://www.old-time.com/otrlogs2/" + link
                writer.writerow([html])
            else:
                continue
