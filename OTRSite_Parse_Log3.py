import re
import csv

with open("OTRSiteScrape.txt","r") as data:
    
    text=data.read()

    search_string = re.compile(r'\[[^\[\]]+Series\:\s\"([\w\s]+)[^\[\]]+\]\[[^\[\]][\w\s="<>\\:./,\'-]+stars\:\s([^\[\]]+?)\\', re.IGNORECASE)
    
    host_search = re.compile(r'\[[^\[\]]+Series\:\s\"([\w\s]+)[^\[\]]+\]\[[^\[\]]*?host\:\s([^\[\]]+?)\\', re.IGNORECASE)
    
    announcer_search = re.compile(r'\[[^\[\]]+Series\:\s\"([\w\s]+)[^\[\]]+\]\[[^\[\]]*?announcer\:\s([^\[\]]+?)\\', re.IGNORECASE)
    
    with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
             
        for match in search_string.finditer(text):    
            try:
                title=match.group(1)
            except:
                title= False       
            try:
                stars=match.group(2)
            except:
                stars=False
            
            writer.writerow([title,stars])
                
    with open('Hosts_Parsed.csv','w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        
        for match in host_search.finditer(text):
            try:
                show=match.group(1)
            except:
                show=False
            try:
                host=match.group(2)
            except:
                host=False
                
            writer.writerow([show, host])
            
    with open('Announcers_Parsed.csv','w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        
        for match in announcer_search.finditer(text):
            try:
                show_title=match.group(1)
            except:
                show_title=False
            try:
                announcer=match.group(2)
            except:
                announcer=False
                    
            writer.writerow([show_title, announcer])
