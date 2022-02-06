import os
import time
from pydoc import TextRepr

import pyttsx3
import vlc
from gtts import gTTS

# initialize Text-to-speech engine
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
for voice in voices:
    print(f"Voice: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender}")
    print(f" - Age: {voice.age}")
    print("\n")
# convert this text to speech
engine.setProperty("rate", 120)
engine.setProperty("voice", voices[0].id)
TEXT = "U 15 Jungeneinzel auf Feld 2: Sven Hoyer gegen Stefan Lindauer"
engine.say(TEXT)
# play the speech
engine.runAndWait()


dir_path = os.path.dirname(os.path.realpath(__file__))

LANGUAGE = "de"

speech = gTTS(text=TEXT, lang=LANGUAGE, slow=False)

speech.save("audio/test.mp3")

player = vlc.MediaPlayer(dir_path + "/audio/test.mp3")
player.play()

time.sleep(20)
