import time

import vlc
from gtts import gTTS

language = "de"


def single_caller(discipline, age_class, court, players):
    print(players)
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
    text_to_speech(game)


def double_caller(discipline, age_class, court, players):
    print(players)
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
        + players[2][1]
        + " "
        + players[2][0]
        + " gegen "
        + players[1][1]
        + " "
        + players[1][0]
        + " und "
        + players[3][1]
        + " "
        + players[3][0]
        + "     ."
    )
    print(game)
    text_to_speech(game)


def text_to_speech(game_text):
    speech = gTTS(text=game_text, lang=language, slow=False)
    speech.save("audio/game.mp3")
    caller("audio/game.mp3")


def caller(audio):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(audio)
    player.set_media(media)
    player.play()

    time.sleep(15)
    while player.is_playing():
        print("test")
        time.sleep(5)
