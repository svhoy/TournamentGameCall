import os
import time

import pyodbc
import vlc
from gtts import gTTS

from .config import Configuration


class DB_Connector:
    def __init__(self, dir_path):
        language = "de"
        print(dir_path)
        config = Configuration()
        database = config.getDatabaseConfig()

        conn = pyodbc.connect(
            r"Driver={"
            + database["Driver"]
            + "}; DBQ="
            + database["Path"]
            + "; PWD="
            + database["Password"]
            + ";"
        )
        cursor = conn.cursor()
        cursor.execute(
            "select Event.name, Court.name, PlayerMatch.event, PlayerMatch.van1, PlayerMatch.van2 from (Event inner join PlayerMatch on Event.ID = PlayerMatch.event) inner join Court on Court.playermatch=PlayerMatch.id "
        )

        match = cursor.fetchall()

        for row in match:
            print(row)
            cursor.execute(
                "select Player.name, Player.firstname from (Entry inner join Player on Entry.player1 = Player.id) inner join PlayerMatch on Entry.ID = PlayerMatch.entry where PlayerMatch.planning ="
                + str(row[3])
                + "and PlayerMatch.event = "
                + str(row[2])
                + ""
            )
            player1 = cursor.fetchall()
            cursor.execute(
                "select Player.name, Player.firstname from (Entry inner join Player on Entry.player1 = Player.id) inner join PlayerMatch on Entry.ID = PlayerMatch.entry where PlayerMatch.planning ="
                + str(row[4])
                + "and PlayerMatch.event = "
                + str(row[2])
                + ""
            )
            player2 = cursor.fetchall()
            if row[0][:2] == "JE":
                game = (
                    self.getDisciplineName(row[0][:2])
                    + row[0][2:]
                    + " auf Spielfeld "
                    + str(int(row[1]))
                    + ": "
                    + player1[0][1]
                    + " "
                    + player1[0][0]
                    + " gegen "
                    + player2[0][1]
                    + " "
                    + player2[0][0]
                )
                print(game)
                speech = gTTS(text=game, lang=language, slow=False)
                speech.save("audio/test.mp3")

                player = vlc.MediaPlayer(dir_path + "/audio/test.mp3")
                player.play()
                time.sleep(10)

    def getDisciplineName(self, disciplinShortcut):
        disciplinNames = {
            "JE": "Jungeneinzel",
            "ME": "Mädcheneinzel",
            "JD": "Jungendoppel",
            "MD": "Mädchendoppel",
            "GD": "Gemischtesdoppel",
        }

        return disciplinNames[disciplinShortcut]
