from .caller import single_caller, double_caller, walkover_double_caller, walkover_single_caller
from .config import Configuration
from .dbConnector import DbConnector


class TournamentGameCaller:
    """Controller class for the everything"""

    def __init__(self):
        """function to init DB"""
        self._db_conn = DbConnector()

    def start(self):
        """Start function the Connection to Database and call the games"""

        walkovers_list = []
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
            walkovers = self._db_conn.get_walkover()
            for walkover in walkovers:
                if walkover[0] in walkovers_list:
                    pass
                else:
                    if walkover[1][1] == "E":
                        players = self._db_conn.get_single_players(
                            walkover[3], walkover[4], walkover[2]
                        )
                        walkover_single_caller(
                            Configuration().get_discipline_name(walkover[1][:2]),
                            walkover[1][2:],
                            players,
                            walkover[6],
                        )
                        walkovers_list.append(walkover[0])
                    else:
                        players = self._db_conn.get_double_players(
                            walkover[3], walkover[4], walkover[2]
                        )
                        walkover_double_caller(
                            Configuration().get_discipline_name(walkover[1][:2]),
                            walkover[1][2:],
                            players,
                            walkover[6],
                        )
                        walkovers_list.append(walkover[0])

            matches = self._db_conn.get_games()

            for match in matches:
                if courts[match[1]] != match[5]:
                    courts[match[1]] = match[5]
                    print(match)
                    if match[0][1] == "E":
                        players = self._db_conn.get_single_players(
                            match[3], match[4], match[2]
                        )
                        single_caller(
                            Configuration().get_discipline_name(match[0][:2]),
                            match[0][2:],
                            match[1],
                            players,
                            match[6],
                        )

                    else:
                        players = self._db_conn.get_double_players(
                            match[3], match[4], match[2]
                        )
                        double_caller(
                            Configuration().get_discipline_name(match[0][:2]),
                            match[0][2:],
                            match[1],
                            players,
                            match[6],
                        )

    def get_db_conn(self):
        """Returns the DB Connector Class

        Returns:
            class: DB Class
        """
        return self._db_conn
