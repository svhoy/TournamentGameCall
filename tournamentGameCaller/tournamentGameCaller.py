from .caller import double_caller, single_caller
from .config import Configuration
from .dbConnector import DbConnector


class TournamentGameCaller:
    """Controller class for the everything"""

    def __init__(self):
        self.db_conn = DbConnector()

    def start(self):
        """Start the Connection to Database and call the games"""
        matches = self.db_conn.get_games()

        for match in matches:
            print(match)
            if match[0][1] == "E":
                players = self.db_conn.get_single_players(match[3], match[4], match[2])
                single_caller(
                    Configuration().get_discipline_name(match[0][:2]),
                    match[0][2:],
                    match[1],
                    players,
                )
            else:
                players = self.db_conn.get_double_players(match[3], match[4], match[2])
                double_caller(
                    Configuration().get_discipline_name(match[0][:2]),
                    match[0][2:],
                    match[1],
                    players,
                )
