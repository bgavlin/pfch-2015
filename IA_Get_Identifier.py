import requests, json   

r = requests.get ("https://archive.org/advancedsearch.php?q=creator:(Old+Time+Radio+Researchers)+AND+mediatype:(audio)&fl[]&rows=500&output=json") 

response_value = json.loads(r.text)

with open('Identifiers.txt','w') as outfile:
    metadata={}
    
    for a_doc in response_value['response']['docs']:
        try: 
            metadata['identifier'] = a_doc['identifier']
        except:
            continue
        #print (metadata['identifier'])
        
        json.dump(metadata['identifier'], outfile)  
        outfile.write('\n')
