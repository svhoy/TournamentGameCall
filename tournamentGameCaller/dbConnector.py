# Third Party
import pyodbc

from .config import Configuration


class DbConnector:
    """Conntector Class to manage Connection and getting Data from Database"""

    def __init__(self) -> None:
        db_config = Configuration().get_database_config()
        self._cursor = self.connect_db(db_config)

    def connect_db(self, db_config) -> pyodbc.Cursor:
        """Function that initzialsed the conntection to the Datebase

        Args:
            db_config (dict): Configuration dict with Driver, Path and Password

        Returns:
            Cursor: Returns the pyodbc Courser to the Database
        """
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
        """Disconnect from Database"""
        self._conn.close()

    def get_games(self) -> list:
        """Function to return all Games thats on a field

        Returns:
            list: Returns a list with all games that currently on a field
        """
        self._cursor.execute(
            "select Event.name, Court.name, PlayerMatch.event, PlayerMatch.van1, "
            + "PlayerMatch.van2, court.playermatch, PlayerMatch.planning from"
            + "(Event inner join PlayerMatch on "
            + "Event.ID = PlayerMatch.event) inner join "
            + "Court on Court.playermatch=PlayerMatch.id "
        )
        return self._cursor.fetchall()

    def get_single_players(self, planning_id1, planning_id2, event_id) -> list:
        """[summary]

        Args:
            planning_id1 (int): Games Planning ID Player 1
            planning_id2 (int): Games Planning ID Player 2
            event_id (int): Event ID to the Planning IDs

        Returns:
            list: Returns a list with all Players for a Single Match
        """
        player1 = self.get_player(planning_id1, event_id)
        player2 = self.get_player(planning_id2, event_id)
        return [player1[0], player2[0]]

    def get_double_players(self, planning_id1, planning_id2, event_id) -> list:
        """[summary]

        Args:
            planning_id1 (int): Games Planning ID Double 1
            planning_id2 (int): Games Planning ID Double 2
            event_id (int): Event ID to the Planning IDs

        Returns:
            list: Returns a list with all Players for a Double Match
        """
        player1 = self.get_player(planning_id1, event_id)
        player2 = self.get_double_partner(planning_id1, event_id)

        player3 = self.get_player(planning_id2, event_id)
        player4 = self.get_double_partner(planning_id2, event_id)

        return [player1[0], player2[0], player3[0], player4[0]]

    def get_player(self, planning_id, event_id) -> list:
        """Getting one Player from Database first Player in Double and Single Player

        Args:
            planning_id (int): Current Player Planning ID
            event_id (int): Current Event ID

        Returns:
            list: With one Entry Player Name
        """
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
        """Getting the Double Partner from Database

        Args:
            planning_id (int): Current Double Planning ID
            event_id (int): Current Event ID

        Returns:
            list: With one Entry Player Name
        """
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
