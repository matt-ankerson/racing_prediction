import requests
import json


def SaveEvent(event):
    event_payload = {
        'name': event.name,
        'date': str(event.date),
        'races': []
    }

    for race in event.races:
        event_payload['races'].append({
            'race_number': race.race_number,
            'distance': race.distance,
            'stake': race.stake,
            'track_condition': race.track_condition,
            'weather': race.weather,
            'winning_margins': race.winning_margins,
            'winner_owners': race.winner_owners,
            'winner_trainer': race.winner_trainer,
            'winner_breeding': race.winner_breeding,
            'sub': race.sub,
            'winner_time': race.winner_time,
            'bets': [{'bet_type': x.bet_type,
                      'runners': x.runners,
                      'dividend': x.dividend} for x in race.bets],
            'competitors': [{'number': x.number,
                             'name': x.name,
                             'jockey': x.jockey,
                             'place': x.place,
                             'place_in_race': x.place_in_race,
                             'win': x.win} for x in race.competitors]
        })

    r = requests.post(
        url='http://localhost:58180/api/event',
        data=json.dumps(event_payload),
        headers={'content-type': 'application/json'})
    return r.status_code
