import re
import csv

with open("OTRSiteScrape.txt","r") as data:
        
    shows = {}
        
    for row in data.readlines():
        series_title = re.compile('Series\:\s\"(.+?)\"', re.IGNORECASE)
        all_titles = series_title.findall(row)
        print(all_titles)
        announcer_name = re.compile(r'Announcer\:\s(.+?\s.+?)[\s\\]',re.IGNORECASE)
        all_announcers = announcer_name.findall(row)
        show_stars = re.compile(r'stars:\s(.+?\s.+?)\\',re.IGNORECASE)
        all_stars = show_stars.findall(row)
        
#        for a_title in all_titles:
#            shows['title'] = a_title
#        for an_announcer in all_announcers:
#            shows['announcer'] = an_announcer
#        for a_star in all_stars:
#            shows['stars']= a_star
        
        shows['title'] = all_titles
        shows['announcer'] = all_announcers
        shows['stars'] = all_stars

#        print(all_titles)
#        
#        for title in all_titles:
#            try:
#                title=title
#            except:
#                title = False
#                
#            for announcer in all_announcers:
#                try:
#                    announcer = announcer
#                except:
#                    announcer = False
#        try:
#            stars = shows['stars']
#        except:
#            stars = False
         
        with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

#            for show in shows['titles']:
##                writer.writerow([show])
#                for announcer in shows['announcer']:
#                    writer.writerow([show,announcer])
##                    for star in shows['stars']:
###                        writer.writerow([show,announcer,star])
            
                
#        with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
##            fieldnames = ['titles','announcer','stars']
##            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#            writer = csv.writer(csvfile, delimiter=' ')
#            
            writer.writerows([title,announcer,stars]) 


