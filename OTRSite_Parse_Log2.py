import re
import csv

with open("OTRSiteScrape.txt","r") as data:
    
    shows = {}
        
    for row in data.readlines():
        series_title = re.compile('Series\:\s\"(.+?)\"', re.IGNORECASE)
        all_titles = series_title.findall(row)
        announcer_name = re.compile(r'Announcer\:\s(.+?\s.+?)[\s\\]',re.IGNORECASE)
        all_announcers = announcer_name.findall(row)
        show_stars = re.compile(r'stars:\s(.+?\s.+?)\\',re.IGNORECASE)
        all_stars = show_stars.findall(row)
            
        shows['titles'] = all_titles
        shows['announcer'] = all_announcers
        shows['stars'] = all_stars
        
    with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        
        for show in shows:
            
            for a_title in all_titles:
                writer.writerow([a_title])
            
            for an_announcer in all_announcers:
                writer.writerow([an_announcer])
        
            for a_star in all_stars:
                writer.writerow([a_star])
        
#            writer.writerow([a_title, an_announcer,a_star])
    
    
#        try:
#            title = shows['titles']            
#        except:
#            title = False
#        try:
#            announcer = shows['announcer']
#        except:
#            announcer = False
#        try:
#            stars = shows['stars']
#        except:
#            stars = False
            
#        with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
#            writer = csv.writer(csvfile)      
#            writer.writerow([a_title,an_announcer,a_star])