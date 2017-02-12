"""
Developer: 
	Name: Abdullah Al Imran
	Email: abdalimran@gmail.com
	
Required Modules to run this program:
	1. BeautifulSoup [pip install beautifulsoup4]
	2. inscriptis [pip install inscriptis]
"""

from urllib.request import urlopen
import lxml
from bs4 import BeautifulSoup
from inscriptis import get_text

def main():
    url = 'http://www.ieee.org/conferences_events/conferences/search/index.html?KEYWORDS=&CONF_SRCH_RDO=conf_date&RANGE_FROM_DATE=&RANGE_TO_DATE=&REGION=Region10-Asia+and+Pacific&COUNTRY=Bangladesh&RowsPerPage=10&PageLinkNum=10&ActivePage=1&SORTORDER=desc&SORTFIELD=start_date'
    content = urlopen(url)
    soup = BeautifulSoup(content,'lxml')
    conference_table = soup.findChildren('table',class_='nogrid-nopad')
    rows = conference_table[0].findChildren('td',class_='pad10')
    
    events = []
    
    for row in rows:
        event = row.find_all('p')
        for info in event:
             events.append(get_text(str(info)))
	    
    label = ["Event title: ", "Date of Submissions:", "Event Date:", "Event Location:"]
    
    extra_decoration = 0
    
    print("*"*60,"\n")
    
    for lab, event in zip(label*len(events), events):
        print(lab, event, end="\n")
        extra_decoration += 1
	
        if extra_decoration == 4:
            print("\n","*"*60,"\n")
            extra_decoration = 0

if __name__=="__main__":
    main()
