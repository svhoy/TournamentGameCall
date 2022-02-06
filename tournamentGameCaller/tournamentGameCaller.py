from .caller import double_caller, single_caller
from .dbConnector import DbConnector
from .donfig import Configuration


class TournamentGameCaller:
    def __init__(self):
        pass

    @staticmethod
    def start():
        db_conn = DbConnector()

        matches = db_conn.get_games()

        for match in matches:
            print(match)
            if match[0][1] == "E":
                players = db_conn.get_single_players(match[3], match[4], match[2])
                single_caller(
                    Configuration().get_discipline_name(match[0][:2]),
                    match[0][2:],
                    match[1],
                    players,
                )
            else:
                players = db_conn.get_double_players(match[3], match[4], match[2])
                double_caller(
                    Configuration().get_discipline_name(match[0][:2]),
                    match[0][2:],
                    match[1],
                    players,
                )
