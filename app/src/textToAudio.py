from gtts import gTTS
import os


def covert_to_audio(text, url, fname):
    audio = gTTS(text, lang='en')
    audio.save(os.path.join(url, f"{fname}.mp3"))
