# Standard Library
import time

# Third Party
import vlc

from gtts import gTTS


LANGUAGE = "de"


def single_caller(discipline, age_class, court, players, games="") -> None:
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

    if games is None:
        text_to_speech(game)

    if games == "final":
        text_to_speech("Im Finale " + game)

    if games == "3":
        text_to_speech("Spiel um Platz 3" + game)

    if games == "halffinal":
        text_to_speech("Im Halbfinale " + game)


def double_caller(discipline, age_class, court, players, games="") -> None:
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

    if games is None:
        text_to_speech(game)

    if games == "final":
        text_to_speech("Im Finale " + game)

    if games == "3":
        text_to_speech("Spiel um Platz 3" + game)

    if games == "halffinal":
        text_to_speech("Im Halbfinale " + game)


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
