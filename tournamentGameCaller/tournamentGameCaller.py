from .caller import double_caller, single_caller
from .config import Configuration
from .dbConnector import DbConnector


class TournamentGameCaller:
    """Controller class for the everything"""

    def __init__(self):
        """function to init DB"""
        self._db_conn = DbConnector()

    def start(self):
        """Start function the Connection to Database and call the games"""
        courts = {
            "01": "",
            "02": "",
            "03": "",
            "04": "",
            "05": "",
            "06": "",
            "07": "",
            "08": "",
            "09": "",
            "10": "",
            "11": "",
            "12": "",
            "13": "",
            "14": "",
            "15": "",
            "16": "",
        }

        while True:
            matches = self._db_conn.get_games()

            for match in matches:
                if courts[match[1]] != match[5]:
                    courts[match[1]] = match[5]
                    print(match)
                    if match[0][1] == "E":
                        players = self._db_conn.get_single_players(
                            match[3], match[4], match[2]
                        )
                        if match[6] == 1001:
                            single_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games="final",
                            )
                        elif match[6] == 1003:
                            single_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games="3",
                            )
                        elif match[6] == 2001:
                            single_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games="halffinal",
                            )
                        else:
                            single_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games=None,
                            )

                    else:
                        players = self._db_conn.get_double_players(
                            match[3], match[4], match[2]
                        )
                        if match[6] == 1001:
                            double_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games="final",
                            )
                        elif match[6] == 1003:
                            double_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games="3",
                            )
                        elif match[6] == 2001:
                            double_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games="halffinal",
                            )
                        else:
                            double_caller(
                                Configuration().get_discipline_name(match[0][:2]),
                                match[0][2:],
                                match[1],
                                players,
                                games=None,
                            )

    def get_db_conn(self):
        """Returns the DB Connector Class

        Returns:
            class: DB Class
        """
        return self._db_conn
