from sqlite3 import Cursor

import pyodbc

from .config import Configuration


class DbConnector:
    def __init__(self) -> None:
        db_config = self.get_config()
        self._cursor = self.connect_db(db_config)

    def get_config(self) -> dict:
        return Configuration().get_database_config()

    def connect_db(self, db_config) -> Cursor:
        # Verbindung mit Datenbank herstellen
        self._conn = pyodbc.connect(
            r"Driver={"
            + db_config["Driver"]
            + "}; DBQ="
            + db_config["Path"]
            + "; PWD="
            + db_config["Password"]
            + ";"
        )
        return self._conn.cursor()

    def disconnect_db(self) -> None:
        self._conn.close()

    def get_games(self) -> list:
        self._cursor.execute(
            "select Event.name, Court.name, PlayerMatch.event, PlayerMatch.van1, "
            + "PlayerMatch.van2 from (Event inner join PlayerMatch on "
            + "Event.ID = PlayerMatch.event) inner join "
            + "Court on Court.playermatch=PlayerMatch.id "
        )
        return self._cursor.fetchall()

    def get_single_players(self, planning_id1, planning_id2, event_id) -> list:
        player1 = self.get_player(planning_id1, event_id)
        player2 = self.get_player(planning_id2, event_id)
        return [player1[0], player2[0]]

    def get_double_players(self, planning_id1, planning_id2, event_id) -> list:
        player1 = self.get_player(planning_id1, event_id)
        player2 = self.get_double_partner(planning_id1, event_id)

        player3 = self.get_player(planning_id2, event_id)
        player4 = self.get_double_partner(planning_id2, event_id)

        return [player1[0], player3[0], player2[0], player4[0]]

    def get_player(self, planning_id, event_id) -> list:
        self._cursor.execute(
            "select Player.name, Player.firstname "
            + "from (Entry inner join Player on Entry.player1 = Player.id) "
            + "inner join PlayerMatch "
            + "on Entry.ID = PlayerMatch.entry where PlayerMatch.planning ="
            + str(planning_id)
            + "and PlayerMatch.event = "
            + str(event_id)
            + ""
        )
        return self._cursor.fetchall()

    def get_double_partner(self, planning_id, event_id) -> list:
        self._cursor.execute(
            "select Player.name, Player.firstname "
            + "from (Entry inner join Player on Entry.player2 = Player.id) "
            + "inner join PlayerMatch "
            + "on Entry.ID = PlayerMatch.entry where PlayerMatch.planning ="
            + str(planning_id)
            + "and PlayerMatch.event = "
            + str(event_id)
            + ""
        )
        return self._cursor.fetchall()
