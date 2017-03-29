
class Event(object):

    def __init__(self, name, date, races=[]):
        self.name = name
        self.date = date
        self.races = races

    def __repr__(self):
        return "%s (%s). No of races: %s" \
            % (self.name, self.date, len(self.races))


class Race(object):

    def __init__(self, race_number,
                 distance, stake,
                 track_condition, weather, bets,
                 winning_margins, winner_owners,
                 winner_trainer, winner_breeding,
                 sub, winner_time, competitors=[]):
        self.race_number = race_number
        self.distance = distance
        self.stake = stake
        self.track_condition = track_condition
        self.weather = weather
        self.bets = bets
        self.winning_margins = winning_margins
        self.winner_owners = winner_owners
        self.winner_trainer = winner_trainer
        self.winner_breeding = winner_breeding
        self.sub = sub
        self.winner_time = winner_time,
        self.competitors = competitors


class Bet(object):

    def __init__(self, bet_type, runners, dividend):
        self.bet_type = bet_type
        self.runners = runners
        self.dividend = dividend


class Competitor(object):

    def __init__(self, number, name, jockey, place,
                 win=None, lengths_behind_leader=None):
        self.number = number
        self.name = name
        self.jockey = jockey
        self.place = place
        self.win = win
        self.lengths_behind_leader = lengths_behind_leader

    def __repr__(self):
        return "Competitor. number: '%s' name: '%s'" \
            % (self.number, self.name)
