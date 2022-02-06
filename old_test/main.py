import os
import time

import pyttsx3
import vlc
from gtts import gTTS

# initialize Text-to-speech engine
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
for voice in voices:
    print("Voice: {}".format(voice.name))
    print(" - ID: {}".format(voice.id))
    print(" - Languages: {}".format(voice.languages))
    print(" - Gender: {}".format(voice.gender))
    print(" - Age: {}".format(voice.age))
    print("\n")
# convert this text to speech
engine.setProperty("rate", 120)
engine.setProperty("voice", voices[0].id)
text = "U 15 Jungeneinzel auf Feld 2: Sven Hoyer gegen Stefan Lindauer"
engine.say(text)
# play the speech
engine.runAndWait()


dir_path = os.path.dirname(os.path.realpath(__file__))

language = "de"

speech = gTTS(text=text, lang=language, slow=False)

speech.save("audio/test.mp3")

player = vlc.MediaPlayer(dir_path + "/audio/test.mp3")
player.play()

time.sleep(20)
