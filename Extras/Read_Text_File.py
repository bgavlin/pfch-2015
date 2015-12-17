import csv
import re

with open("RadioShows.txt","r") as radio_shows:
    with open('Proper_Nouns.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for an_episode in radio_shows:  
            title = re.compile('"title":\s"(.+?)"')
            title_match = title.search(an_episode)
            names = re.compile('([A-Z][a-z]+\s[A-Z]\w+)')
            name_match = names.search(an_episode)
        
            if title_match:
                
                try:
                    title_tuple= title_match.groups()
                    show_titles = title_tuple[0]
                except:
                    show_titles = False
                
                writer.writerow([show_titles])
                
            if name_match:
                try:
                    name_tense = name_match.group(0)
                except:
                    name_tense = False
            
                writer.writerow([name_tense])
        
        
            
    