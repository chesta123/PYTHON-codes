from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'en'
sp = gTTS(text="i am chesta gupta", lang=language,slow=False)
sp.save(audio)
playsound(audio)

# print("\U0001F923")
# print("\U0001F922")
# print("\U0001F924")
# print("\U0001F618")
# print("\U0001F917")
# print("\U0001F62A")
# print("\U0001F600")
# print("\U0001F606")
# print("\U0001F607")