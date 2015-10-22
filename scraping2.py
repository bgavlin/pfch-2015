from bs4 import BeautifulSoup

import requests
import re 

url = "http://www.otrplotspot.com/suspense.html"
object_page = requests.get(url)
html = object_page.text

soup = BeautifulSoup(html, "html.parser")

all_titles = soup.find_all("h3", attrs={"class":"title titleSuspense"})
all_divs = soup.find_all("div", attrs={"class":"review"})
container = soup.find("div", attrs={"class":"container"})
high_ratings = soup.find_all(string=re.compile("\[[^1-7]\/10\]"))

#prints titles + reviews of any shows rated 8/10 or higher
for a_rating in high_ratings:
    print(a_rating.find_previous("h3", attrs={"class":"title titleSuspense"}).text)
    print(a_rating)

#for a_title in all_titles:
#    print ("Title: " + a_title.text)
#    print (a_title.find_next_sibling("div", attrs={"class":"review"}))

    

                          
    