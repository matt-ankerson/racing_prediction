import requests
import re
from datetime import date
from bs4 import BeautifulSoup
from race_event_types import Event
from race_event_types import Race
from race_event_types import Competitor
from race_event_types import Bet


def ScrapeEvent(race_result_url):
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                  'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    r = requests.get(race_result_url)

    # Create soup from web request result content
    content = r.content
    soup = BeautifulSoup(content, 'html5lib')

    # Get the event name
    event_element = \
        soup.find('div', class_='infoPanelBar navbar').find('strong')
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

        try:
            race_title = race_container.find('div',
                                             class_='raceTitle')\
                                            .contents[0].strip()
        except AttributeError:
            race_title = race_container.find('div', class_='header bold')
            race_title = race_title.text.strip().replace('index', '')

        race_det_arr = [x.rstrip() for x in race_title.split()]

        new_race = Race(race_number=race_det_arr[1],
                        distance=race_det_arr[race_det_arr.index('m') - 1],
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

        # add first 3 results (if there are any)
        try:
            placing_results = \
                race_container.find('table', class_='raceResults')\
                .find('tbody').find_all('tr')

            win_results = placing_results[0].findChildren()
            second_results = placing_results[1].findChildren()
            third_results = placing_results[2].findChildren()

            # first place
            new_race.competitors.append(Competitor(
                                        number=win_results[0].contents[0],
                                        name=win_results[1].contents[0],
                                        jockey=win_results[2].contents[0],
                                        win=win_results[3].contents[0].strip(),
                                        place=win_results[4]
                                        .contents[0].strip()))
            # second place
            new_race.competitors.append(Competitor(
                                        number=second_results[0].contents[0],
                                        name=second_results[1].contents[0],
                                        jockey=second_results[2].contents[0],
                                        win=None,
                                        place=second_results[4].contents[0]
                                        .strip()))
            # third place
            new_race.competitors.append(Competitor(
                                        number=third_results[0].contents[0],
                                        name=third_results[1].contents[0],
                                        jockey=third_results[2].contents[0],
                                        win=None,
                                        place=third_results[4]
                                        .contents[0].strip()))
        except:
            pass

        # add remaining competitors (if any are listed)
        try:
            also_ran = race_container.find('strong', text='ALSO RAN:')\
                .parent.text.strip()

            # also_ran_arr is quite a dirty array
            also_ran_arr = [x.replace('ALSO RAN:\n', '')
                            for x in also_ran.split(',')]

            for competitor in also_ran_arr:
                competitor_breakdown = competitor.split('-')
                # add other competitors to collection
                new_race.competitors.append(
                    Competitor(number=competitor_breakdown[0],
                               name=competitor_breakdown[1],
                               jockey=re.sub(r'\([^)]*\)', '',
                               competitor_breakdown[2]),
                               win=None,
                               place=None,
                               lengths_behind_leader=None))
        except:
            pass

        # scrape bet information (of which there are an arbitrary number)
        try:
            bets = race_container.find('div', text='Bet Type')\
                .parent.parent.parent.parent.find('tbody').find_all('tr')
        except:
            bets = []

        for bet_row in bets:
            clean_bet_row = [x.text.strip() for x in bet_row.findChildren()]
            runners = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]',
                               clean_bet_row[1])
            runners = [x.strip() for x in runners]

            new_race.bets.append(Bet(bet_type=clean_bet_row[0],
                                     runners=runners,
                                     dividend=clean_bet_row[2]))

        # scrape remaining race information
        try:
            race_metadata = race_container\
                .find('strong', text='Winning Margins:')\
                .parent.parent.text.split('\n')
            race_metadata = \
                [x.strip().split(':') for x in race_metadata if x != '']
            race_metadata = \
                [item for sublist in race_metadata for item in sublist]
            race_metadata = \
                [x for x in race_metadata if x != '']
        except:
            race_metadata = []

        # sometimes these attributes are missing
        try:
            new_race.winning_margins = \
                race_metadata[race_metadata.index('Winning Margins') + 1]
        except:
            pass
        try:
            new_race.winner_owners = \
                race_metadata[race_metadata.index('Owners') + 1]
        except:
            pass
        try:
            new_race.winner_trainer = \
                race_metadata[race_metadata.index('Trainer') + 1]
        except:
            pass
        try:
            new_race.winner_breeding = \
                race_metadata[race_metadata.index('Breeding') + 1]
        except:
            pass
        try:
            new_race.sub = \
                race_metadata[race_metadata.index('SUB') + 1]
        except:
            pass
        try:
            winners_time = \
                race_metadata[race_metadata.index('Winners Time') + 1:
                              race_metadata.index('Winners Time') + 3]
            new_race.winner_time = winners_time[0] + ':' + winners_time[1]
        except:
            pass

        # append this race to the event
        event.races.append(new_race)

    return event

# event = ScrapeEvent("https://ebet.tab.co.nz/results/DBAI-reslt03251700.html")
# print(str(event))
