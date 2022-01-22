import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
# convert this text to speech
engine.setProperty("rate", 120)
engine.setProperty("voice", voices[0].id)
text = "U 15 Jungeneinzel auf Feld 2: Sven Hoyer gegen Stefan Lindauer"
engine.say(text)
# play the speech
engine.runAndWait()


from gtts import gTTS
import vlc
import time

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

language = 'de'

speech = gTTS(text = text, lang = language, slow = False)

speech.save('audio/test.mp3')

player = vlc.MediaPlayer(dir_path + "/audio/test.mp3")
player.play()

time.sleep(20)