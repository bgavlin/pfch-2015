# pfch-2015
This code is intended to explore the Radio Logs from OTRSite.com and create a combined dataset of the Show Titles and Stars catalogued within.  The code is broken down per the below:

1.	OTRSite_Log_Scrape - scrapes the individual show URL’s from www.otrsite.com/radiolog/index.html and saves to a CSV file (Log_Links_2)
2.	Log_Links_4  - cleaned up version of Log_Links_2 (extraneous or duplicate URL’s removed)
3.	OTRSite_Log_Scrape_Pt_2 - loops through Log_Links_4, opens each link, and scrapes any text preceded by font size 3 tag or a font size 4 tag, writing it to a txt file (OTRSiteScrape.txt)
4.	OTRSite_Parse_Log3 - loops through the text file, pulling out the show titles, stars, announcers, and hosts with RegEx and writes each to a separate CSV file. 
5.	Bio_Links.csv – CSV file containing the names of the top 72 personalities from the data set (aka those with the highest numbers of shows) along with links to their DBPedia pages.
6.	bio_scrape -  loop through each link from the Bio_Links CSV, connects to the JSON file of the dbpedia page, and writes the biographies to a new CSV file (Bios.csv).

The Extras folder contains extra code/previous versions of the final code and were not used in the final product.
The Parsed Files folder contains resulting files that are not needed to run the code itself as well as any files needed to create the visualizations available at http://bgavlin.wix.com/pythonradio
