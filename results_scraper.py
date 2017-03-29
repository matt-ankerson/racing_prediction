import requests
import re
from datetime import date
from bs4 import BeautifulSoup
from race_event_types import Event
from race_event_types import Race
from race_event_types import Competitor

month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

race_result_url = "https://ebet.tab.co.nz/results/NSWC-reslt03271700.html"
r = requests.get(race_result_url)

# Create soup from web request result content
content = r.content
soup = BeautifulSoup(content, 'html5lib')

# Get the event name
event_element = soup.find('div', class_='infoPanelBar navbar').find('strong')
event_name = event_element.contents[0].strip()

# Get the event date
event_date_arr = event_name.split(' ')[-3:]
event_date = date(int(event_date_arr[2]), month_dict[event_date_arr[1]],
                  int(event_date_arr[0]))

# Create the event
event = Event(name=event_name, date=event_date, races=[])

# Take the race containers from the soup
# - This collection of elements contains info
#   about the races at this event.
race_containers = soup.find_all('div', class_='content')

for race_container in race_containers:
    # race_container is a tag
    race_title = race_container.find('div', class_='raceTitle')\
        .contents[0].strip()
    race_det_arr = [x.rstrip() for x in race_title.split()]

    new_race = Race(race_number=race_det_arr[1],
                    time=race_det_arr[3],
                    distance=race_det_arr[10],
                    stake=race_container.find('th', text='Stake:')
                    .fetchNextSiblings()[0].contents[0],
                    track_condition=race_container.find('th', text='Track:')
                    .fetchNextSiblings()[0].contents[0],
                    weather=race_container.find('th', text='Weather:')
                    .fetchNextSiblings()[0].contents[0],
                    bets=[],
                    winning_margins=[],
                    winner_owners=[],
                    winner_trainer=None,
                    winner_breeding=None,
                    sub=None,
                    winner_time=None,
                    competitors=[])

    # results info
    placing_results = race_container.find('table', class_='raceResults')\
        .find('tbody').find_all('tr')

    win_results = placing_results[0].findChildren()
    second_results = placing_results[1].findChildren()
    third_results = placing_results[2].findChildren()

    # first place
    new_race.competitors.append(Competitor(number=win_results[0].contents[0],
                                name=win_results[1].contents[0],
                                jockey=win_results[2].contents[0],
                                win=win_results[3].contents[0].strip(),
                                place=win_results[4].contents[0].strip()))
    # second place
    new_race.competitors.append(Competitor(number=second_results[0].contents[0],
                                name=second_results[1].contents[0],
                                jockey=second_results[2].contents[0],
                                win=None,
                                place=second_results[4].contents[0].strip()))
    # third place
    new_race.competitors.append(Competitor(number=third_results[0].contents[0],
                                name=third_results[1].contents[0],
                                jockey=third_results[2].contents[0],
                                win=None,
                                place=third_results[4].contents[0].strip()))
    # add remaining competitors
    also_ran = race_container.find('strong', text='ALSO RAN:')\
        .parent.text.strip()
    # also_ran_arr is quite a dirty array
    also_ran_arr = [x.replace('ALSO RAN:\n', '') for x in also_ran.split(',')]

    for competitor in also_ran_arr:
        competitor_breakdown = competitor.split('-')
        # add other competitors to collection
        new_race.competitors.append(
            Competitor(number=competitor_breakdown[0],
                       name=competitor_breakdown[1],
                       jockey=re.sub(r'\([^)]*\)', '', competitor_breakdown[2]),
                       win=None,
                       place=None,
                       lengths_behind_leader=None))  # lengths is too dirty

    # scrape bet information

    # scrape remaining race information

    event.races.append(new_race)
