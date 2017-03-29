from datetime import date, timedelta
from day_scraper import ScrapeDay


def IterateDateRange(start_date, end_date):
    day_count = (end_date - start_date).days + 1
    for race_date in (start_date + timedelta(n) for n in range(day_count)):
        # get the links to events for this day
        links = ScrapeDay(race_date.day, race_date.month, race_date.year)
        print(links)


start = date(2017, 3, 10)
end = date(2017, 3, 27)

IterateDateRange(start, end)
