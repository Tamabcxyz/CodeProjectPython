'''import speech_recognition
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening...")
    audio = robot_ear.listen(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you="..."
print("You: " + you)
'''
import speech_recognition as sr
filename=""
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)