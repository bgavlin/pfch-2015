import json
import requests
import re
import csv

with open("Bio_Links.csv","r") as csvfile:
    links = csv.reader(csvfile)
    
    with open("Bios.csv","w", newline='') as newcsv:
        writer = csv.writer(newcsv, quoting=csv.QUOTE_MINIMAL)
        
        for a_link in links:

            name=a_link[0]
            url=a_link[1]

            jsonurl = re.sub('/resource/', '/data/', url)
        
            try:
                t = requests.get(jsonurl + ".json")
                person_info = json.loads(t.text)
            except:
                pass
        
            try:
                for data in person_info[url]["http://dbpedia.org/ontology/birthYear"]:
                    try:
                        birth_year=data['value']
                    except:
                        birth_year=False
            except:
                pass
            
            try:
                for data in person_info[url]["http://dbpedia.org/ontology/deathYear"]:
                    try:
                        death_year = data['value']
                    except:
                        death_year = False
            except:
                pass
            
            try:
                for data in person_info[url]['http://www.w3.org/2000/01/rdf-schema#comment']:
                
                    if data['lang']=='en':
                        bio = data['value']
            except:
                pass
            
            
            writer.writerow([name, birth_year,death_year, bio])

                        