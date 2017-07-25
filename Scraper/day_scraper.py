import requests
from bs4 import BeautifulSoup


def ScrapeDay(day, month, year):
    r = requests.get('https://ebet.tab.co.nz/ebet/ResultsArchive?day=' +
                     str(day) + '&month=' + str(month) + '&year=' + str(year))

    if r.status_code == 200:
        # find the links to the events for this day.
        soup = BeautifulSoup(r.content, 'html5lib')

        raw_links = soup.find('h3', text='SEARCH RESULTS')\
            .parent.parent.find_all('a')

        links = [x['href'] for x in raw_links
                 if x.has_attr('href') and not x.has_attr('nofollow')]
        return links
    else:
        return []


# ScrapeDay(27, 3, 2002)
