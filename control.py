import speech_recognition as sr
import os
# obtain audio from the microphone                                              
r = sr.Recognizer()
with sr.Microphone() as source:
    os.system("say please speak what you would like to be writen")
    audio = r.listen(source)
text = r.recognize_sphinx(audio)
os.system(text)







