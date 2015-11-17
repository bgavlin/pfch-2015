import nltk.data
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
from nameparser.parser import HumanName
import csv

#http://stackoverflow.com/questions/20290870/improving-the-extraction-of-human-names-with-nltk

with open('OTRSiteScrape.txt','r') as text:
    
    for row in text:
        def get_human_names(row):
            tokens = nltk.tokenize.word_tokenize(row.strip())
            pos = nltk.pos_tag(tokens)
            sentt = nltk.ne_chunk(pos, binary = False)
            person_list = []
            person = []
            name = ""
            for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
                for leaf in subtree.leaves():
                    person.append(leaf[0])
                if len(person) > 1: #avoid grabbing lone surnames
                    for part in person:
                        name += part + ' '
                    if name[:-1] not in person_list:
                        person_list.append(name[:-1])
                    name = ''
                person = []
        
            return (person_list)
    
        with open('OTRSiteNames.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            names = get_human_names(row)
        
            for name in names: 
#            last_first = HumanName(name).last + ', ' + HumanName(name).first
                writer.writerow([HumanName(name)])