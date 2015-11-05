from bs4 import BeautifulSoup
import requests
import csv

with open("Log_Links_2.csv","r") as links:
    for a_link in links:
        url = a_link
        object_page = requests.get(url)
        html = object_page.text
        
        soup = BeautifulSoup(html, "html.parser")
            
        font_3 = soup.find_all("font", attrs={"size":"3"})
        font_5 = soup.find_all("font", attrs={"size":"5"})
        
        if font_5:
            print (font_3)
            print (font_5)