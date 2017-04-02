from datetime import date, timedelta
from day_scraper import ScrapeDay
from event_scraper import ScrapeEvent
from storage_service import SaveEvent
import time
import sys


def IterateDateRange(start_date, end_date):
    day_count = (end_date - start_date).days + 1

    for race_date in (start_date + timedelta(n) for n in range(day_count)):
        # delay request by half a second
        time.sleep(0.5)

        # get the links to events for this day
        try:
            links = ScrapeDay(race_date.day, race_date.month, race_date.year)
            print('Found %s events for %s:' % (len(links), race_date))
        except:
            links = []
            e = sys.exc_info()[0]
            print('Failed to get events for %s. Error: %s' % (race_date, e))

        for link in links:
            # delay request by half a second
            time.sleep(0.5)
            try:
                event = ScrapeEvent('https://ebet.tab.co.nz' + link)
                print(str(event))
                # push the event off to a database
                SaveEvent(event)
            except:
                e = sys.exc_info()[0]
                print('Failed to collect event information at %s. Error: %s'
                      % (link, e))


start = date(2017, 3, 31)
end = date(2017, 4, 2)

IterateDateRange(start, end)
