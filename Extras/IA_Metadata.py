import requests, json   

r = requests.get ("https://archive.org/advancedsearch.php?q=creator:(Old+Time+Radio+Researchers)+AND+mediatype:(audio)&fl[]&rows=50&output=json") 

response_value = json.loads(r.text)

with open('RadioMetadata.txt','w') as outfile:
    for a_doc in response_value['response']['docs']:
        try: 
            identifier = a_doc['identifier']
        except:
            continue
        
        payload = {'identifier':identifier}
        r = requests.get ("https://archive.org/metadata/", params=payload)
        response_value = json.loads(r.text)
        
        metadata = {}
        
        for a_file in response_value['files']:
            try:
                metadata['title'] = a_doc['title']
                metadata['description'] = a_doc['description']
            except:
                continue 
            if metadata['title'] not in metadata:    
                json.dump(metadata, outfile, indent = 4)
