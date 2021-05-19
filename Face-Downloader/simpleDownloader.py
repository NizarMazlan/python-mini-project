import speech_recognition as sr
from simple_image_download import simple_image_download as simp

r = sr.Recognizer()
response = simp.simple_image_download

with sr.Microphone() as source:
    print("Who's face do you want to download")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        print("You said : " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition")

response().download(text + ' face' ,100)

#used 2 different python libraries
#pyaudio and simple downloader
