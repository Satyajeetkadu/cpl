from gtts import gTTS
from playsound import playsound

tts = gTTS(text='Kadiuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', lang='en')
tts.save('speech.mp3')

# play the speech using the default system player
playsound('speech.mp3')
