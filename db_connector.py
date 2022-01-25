import time

import pyodbc
import vlc
from gtts import gTTS
from config import Configuration


def connect_db():
    # Configfile laden und daten in ein Dictionary speichern
    config = Configuration()
    database = config.getDatabaseConfig()

    # Verbindung mit Datenbank herstellen
    conn = pyodbc.connect(
        r"Driver={" + database["Driver"] + "}; DBQ=" + database["Path"] + "; PWD=" + database["Password"] + ";")
    cursor = conn.cursor()
    return cursor

class DB_Connector:
    def __init__(self, dir_path):

        self.dir_path = dir_path
        self.cursor = connect_db()





        # Alle Spiele/die Altersklasse, Spielfelder, und die Spieler in Form von einer Id raussuchen
        self.cursor.execute("select Event.name, Court.name, PlayerMatch.event, PlayerMatch.van1, PlayerMatch.van2 from (Event inner join PlayerMatch on Event.ID = PlayerMatch.event) inner join Court on Court.playermatch=PlayerMatch.id ")
        match = self.cursor.fetchall()
        self.match = match



        for row in match:
            self.row = row
            disziplin = row[0][:2]
            print(disziplin)
            if disziplin[1] == "D":
                self.Doppel()

            if disziplin[1] == "E":
                self.Einzel()



    def Einzel(self):

        row = self.row

        # Spieler Identifizieren
        player1 = self.getPlayersNames(row[3], row[2])
        player2 = self.getPlayersNames(row[4], row[2])

        # Disziplin ermitteln
        Disziplin = self.getDisciplineName(row[0][:2]) + row[0][2:]

        # Zu sprechenden Text ermitteln
        game = self.getSpeechSingle(player1, player2, str(int(row[1])), Disziplin)
        #print(game)

        # Sprachausgabe
        self.Speaking(game, self.dir_path)

        time.sleep(10)


    def Doppel(self):

        row = self.row

        players = self.getPlayersNames(row[3], row[2])
        players1 = self.getPlayersNames(row[4], row[2])

        player1 = players[0]
        player2 = players[1]
        player3 = players1[0]
        player4 = players1[1]

        # Disziplin ermitteln
        Disziplin = self.getDisciplineName(row[0][:2]) + row[0][2:]

        game = self.getSpeechDouble(player1, player2, player3, player4, str(int(row[1])), Disziplin)

        # Sprachausgabe
        self.Speaking(game, self.dir_path)

        time.sleep(10)

    def getSpeechSingle(self, Player1, Player2, Feld, Disziplin):

        fullplayer1 = (Player1[0][0][1] + " " + Player1[0][0][0])
        fullplayer2 = (Player2[0][0][1] + " " + Player2[0][0][0])
        Spielfeld = str(" auf Spielfeld " + Feld)
        text = (Disziplin + Spielfeld + " " + fullplayer1 + " gegen " + fullplayer2)
        return text

    def getSpeechDouble(self, Player1, Player2, Player3, Player4, Feld, Disziplin):

        fullplayers1 = (Player1[0][1] + " " + Player1[0][0] + " mit " + Player2[0][1] + " " + Player2[0][0])
        fullplayers2 = (Player3[0][1] + " " + Player3[0][0] + " mit " + Player4[0][1] + " " + Player4[0][0] + " ")
        Spielfeld = str(" auf Spielfeld " + Feld)
        text = (Disziplin + Spielfeld + " " + fullplayers1 + " gegen " + fullplayers2)
        return text


    def getPlayerName(self, MatchID, Altersklasse):
        # Aus der Spieler-Id den Spieler namen suchen
        self.cursor.execute("select Player.name, Player.firstname from (Entry inner join Player on Entry.player1 = Player.id) inner join PlayerMatch on Entry.ID = PlayerMatch.entry where PlayerMatch.planning =" + str(MatchID) + "and PlayerMatch.event = " + str(Altersklasse) + "")
        player = self.cursor.fetchall()
        print(player)
        return player

    def getPlayersNames(self, MatchID, Altersklasse):
        liste = [0, 0]
        self.cursor.execute("select Player.name, Player.firstname from (Entry inner join Player on Entry.player1 = Player.id) inner join PlayerMatch on Entry.ID = PlayerMatch.entry where PlayerMatch.planning =" + str(MatchID) + "and PlayerMatch.event = " + str(Altersklasse) + "")
        player1 = self.cursor.fetchall()
        self.cursor.execute("select Player.name, Player.firstname from (Entry inner join Player on Entry.player2 = Player.id) inner join PlayerMatch on Entry.ID = PlayerMatch.entry where PlayerMatch.planning =" + str(MatchID) + "and PlayerMatch.event = " + str(Altersklasse) + "")
        player2 = self.cursor.fetchall()

        liste = [player1, player2]

        return liste

    def Speaking(self, game, dir_path):
        # Sprache der Sprachausgabe
        language = "de"

        speech = gTTS(text=game, lang=language, slow=False)
        speech.save("test.mp3")

        player = vlc.MediaPlayer(dir_path + "/test.mp3")
        player.play()


    def getDisciplineName(self, disciplineShortcut:str) -> str:
        disciplineNames = {
            "JE": "Jungeneinzel",
            "ME": "Mädcheneinzel",
            "JD": "Jungendoppel",
            "MD": "Mädchendoppel",
            "GD": "Gemischtesdoppel",
        }

        return disciplineNames[disciplineShortcut]
