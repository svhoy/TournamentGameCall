# Standard Library
import time

# Third Party
import vlc

from gtts import gTTS


LANGUAGE = "de"

special_game = {
    1001: "Im Finale",
    1003: "Spiel um Platz 3",
    2001: "Im Halbfinale ",
    2002: "Im Halbfinale ",
}


def single_caller(discipline, age_class, court, players, game_id) -> None:
    """Bring all parts of the single call together and call text_to_speech function

    Args:
        discipline (str): [description]
        age_class (str): [description]
        court (str): [description]
        players (list): [description]
    """
    game = (
        discipline
        + age_class
        + " auf Spielfeld "
        + str(int(court))
        + ": "
        + players[0][1]
        + " "
        + players[0][0]
        + " gegen "
        + players[1][1]
        + " "
        + players[1][0]
        + " "
    )

    print(game)

    if game_id in special_game:
        text_to_speech(special_game[game_id] + game)

    else:
        text_to_speech(game)


def walkover_single_caller(discipline, age_class, players, walkover_id) -> None:
    """ "function to call single games wich are walkovers"""
    player_first = players[0][1] + " " + players[0][0]
    player_second = players[1][1] + " " + players[1][0] + " "

    if walkover_id == 1:
        game = (
            "Das Spiel im "
            + discipline
            + age_class
            + player_first
            + " gegen "
            + player_second
            + " geht Kampflos an "
            + player_first
        )
    elif walkover_id == 2:
        game = (
            "Das Spiel im "
            + discipline
            + age_class
            + player_first
            + " gegen "
            + player_second
            + " geht Kampflos an "
            + player_second
        )
    else:
        print("es ist ein unerwarteter Fehler aufgetreten siehe caller.py line 94")

    text_to_speech(game)


def double_caller(discipline, age_class, court, players, game_id) -> None:
    """Bring all parts of the double call together and call text_to_speech function

    Args:
        discipline (str): [description]
        age_class (str): [description]
        court (str): [description]
        players (list): [description]
    """
    game = (
        discipline
        + age_class
        + " auf Spielfeld "
        + str(int(court))
        + ": "
        + players[0][1]
        + " "
        + players[0][0]
        + " und "
        + players[1][1]
        + " "
        + players[1][0]
        + " gegen "
        + players[2][1]
        + " "
        + players[2][0]
        + " und "
        + players[3][1]
        + " "
        + players[3][0]
    )
    print(game)

    if game_id in special_game:
        text_to_speech(special_game[game_id] + game)

    else:
        text_to_speech(game)


def walkover_double_caller(discipline, age_class, players, walkover_id) -> None:
    """functio to call all double games which are walkovers"""
    Player_first = (
        players[0][1]
        + " "
        + players[0][0]
        + " und "
        + players[1][1]
        + " "
        + players[1][0]
    )
    Player_second = (
        players[2][1]
        + " "
        + players[2][0]
        + " und "
        + players[3][1]
        + " "
        + players[3][0]
    )

    if walkover_id == 1:
        game = (
            "Das Spiel im "
            + discipline
            + age_class
            + player_first
            + " gegen "
            + player_second
            + " geht Kampflos an "
            + player_first
        )
    elif walkover_id == 2:
        game = (
            "Das Spiel im "
            + discipline
            + age_class
            + player_first
            + " gegen "
            + player_second
            + " geht Kampflos an "
            + player_second
        )
    else:
        print("es ist ein unerwarteter Fehler aufgetreten siehe caller.py line 149")

    text_to_speech(game)


def text_to_speech(game_text: str) -> None:
    """Take Text and do magic

    Args:
        game_text (str): callable text
    """
    speech = gTTS(text=game_text, lang=LANGUAGE, slow=False)
    speech.save("audio/game.mp3")
    caller("audio/game.mp3")


def caller(audio: str) -> None:
    """Call the audio from text to speech engine via vlc Player

    Args:
        audio (str): relative path to the audio file
    """
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(audio)
    player.set_media(media)
    player.play()

    time.sleep(10)
    while player.is_playing():
        time.sleep(1)
