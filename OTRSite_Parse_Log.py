import re
import csv

Data = [line.strip() for line in open('OTRSiteScrape.txt')]
with open('Shows_Parsed.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for a_show in Data:

        series_title = re.compile('Series\: \".+?\"')
        title_match = series_title.search(a_show)
        
        try:
            SeriesTitle = title_match.group(0)
        except:
            SeriesTitle = False
            
        writer.writerow([SeriesTitle])