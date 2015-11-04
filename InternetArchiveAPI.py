import requests, json
import csv    

#r = requests.get ("https://archive.org/advancedsearch.php?q=old+time+radio&fl[]=creator,coverage,date,description,title,type,subject,identifier&rows=50&page=1&output=json")   

r = requests.get ("https://archive.org/advancedsearch.php?q=creator:(Old+Time+Radio+Researchers)+AND+mediatype:(audio)&fl[]&rows=50&page=1&output=json") 

response_value = json.loads(r.text)

#print(response_value['response']['docs'])
#print(response_value['response']['docs'][0]['title'])

#with open('RadioShows.txt','w') as outfile:
with open('IA_Radio_Shows.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    metadata={}
    
    for a_doc in response_value['response']['docs']:
        try: 
            metadata['title'] = a_doc['title']
            metadata['description'] = a_doc['description']
        except:
            continue
        try:
            title = metadata['title']
        except:
            title = False
        try:
            description = metadata['description']
        except:
            description = False
        #print (metadata)
        #json.dump(metadata, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
        writer.writerow([title,description])
