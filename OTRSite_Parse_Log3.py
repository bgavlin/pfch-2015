import re
import csv

with open("OTRSiteScrape.txt","r") as data:
    
#    for row in data.readlines():
    text=data.read()
    
#    series_title = re.compile('Series\:\s\"(.+?)\"', re.IGNORECASE)
#    all_titles = series_title.finditer(text)
#    announcer_name = re.compile(r'Announcer\:\s(.+?\s.+?)[\s\\]',re.IGNORECASE)
#    all_announcers = announcer_name.findall(text)
#    show_stars = re.compile(r'stars:\s(.+?\s.+?)\\',re.IGNORECASE)
#    all_stars = show_stars.findall(text)
    
    search_string = re.compile(r'Series\:\s\"(.+?)\".*?Announcer\:\s(.+?\s.+?)[\s\\].*?stars:\s(.+?\s.+?)\\', re.IGNORECASE)


    
    with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
             
        for match in search_string.finditer(text):    
            try:
                title=match.group(1)
            except:
                title= False       
            try: 
                announcer=match.group(2)
            except:
                announcer=False
            try:
                stars=match.group(3)
            except:
                stars=False
            
        writer.writerow([title,announcer,stars])
                

#         for match in series_title.finditer(text):    
#            try:
#                title=match.group(1)
#            except:
#                title= "False"
#        
#        for match in announcer_name.finditer(text):    
#            try:
#                announcer=match.group(1)
#            except:
#                announcer= "False"
#                
#        for match in show_stars.finditer(text):    
#            try:
#                stars=match.group(1)
#            except:
#                stars= "False"              
                
            
