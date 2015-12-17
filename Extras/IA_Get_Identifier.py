import requests, json
import csv
import re

with open('All_Shows_for_API.csv', 'r') as csvfile:

    for row in csvfile:
        query=row   
        r = requests.get ("https://archive.org/advancedsearch.php?q="+ query +"+AND+creator:(Old+Time+Radio+Researchers)+AND+mediatype:(audio)&fl[]&rows=500&output=json")
        print (query)
        
        try:
            response_value = json.loads(r.text)
        except:
            continue

        with open('Identifiers.csv','a') as outfile:
            writer = csv.writer(outfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
           
            metadata={}
    
            for a_doc in response_value['response']['docs']:
                try: 
                    metadata['identifier'] = a_doc['identifier']
                    identifier=metadata['identifier']
                except:
                    identifier= False
                try:
                    metadata['title'] = a_doc['title']
                    title=metadata['title']
                except:
                    title= False
                    
            writer.writerow([identifier, title])
                        
    