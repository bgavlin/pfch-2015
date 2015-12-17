from bs4 import BeautifulSoup
import requests
import csv

#with open("Log_Links.csv","r") as links:
#    for a_link in links:
#        url = a_link
#        object_page = requests.get(url)
#        html = object_page.text
#        
#        soup = BeautifulSoup(html, "html.parser")
#            
#        all_data = soup.find("td", attrs={"class":"line-content"})
#        print (all_data)

url ="http://www.otrsite.com/otrsite/logs/logs1003.htm"
object_page = requests.get(url)
html = object_page.text

soup = BeautifulSoup(html, "html.parser")

all_data = soup.find_all("font", attrs={"size":"2"})
print (all_data)