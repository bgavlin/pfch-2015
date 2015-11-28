import re
import csv

with open("OTRSiteScrape.txt","r") as data:
    
#    for row in data.readlines():
    text=data.read()
    
    series_title = re.compile('Series\:\s\"(.+?)\"', re.IGNORECASE)
    all_titles = series_title.findall(text)
    announcer_name = re.compile(r'Announcer\:\s(.+?\s.+?)[\s\\]',re.IGNORECASE)
    all_announcers = announcer_name.findall(text)
    show_stars = re.compile(r'stars:\s(.+?\s.+?)\\',re.IGNORECASE)
    all_stars = show_stars.findall(text)
    
    with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for a_title in all_titles:    
            try: 
                writer.writerow([a_title])
            except:
                writer.writerow("false")        
        for an_announcer in all_announcers:
            try:
#                    announcer = an_announcer
                writer.writerow([an_announcer])
            except:
                writer.writerow("false")
                        
        for a_star in all_stars:
#                    star=a_star
            try:
                writer.writerow([a_star])            
            except:
                writer.writerow("false")
            
                
            
