import requests, json
import csv    

r = requests.get ("https://archive.org/advancedsearch.php?q=creator:(Old+Time+Radio+Researchers)+AND+mediatype:(audio)&fl[]&rows=900&output=json") 

response_value = json.loads(r.text)

#print(response_value['response']['docs'])
#print(response_value['response']['docs'][0]['title'])

with open('RadioShows.txt','w') as outfile:
    metadata={}
    
    for a_doc in response_value['response']['docs']:
        try: 
            metadata['title'] = a_doc['title']
            metadata['description'] = a_doc['description']
        except:
            continue
        #print (description)
        json.dump(metadata, outfile, indent = 4, ensure_ascii=False)  


        
#with open('IA_Radio_Shows2.csv', 'w', newline='') as csvfile:   
#    writer = csv.writer(csvfile, delimiter = "}")
#        try:
#            title = metadata['title']
#        except:
#            title = False
#        try:
#            description = metadata['description']
#        except:
#            description = False
#        writer.writerow([title,description])
