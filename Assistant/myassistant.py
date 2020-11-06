import speech_recognition
import pyttsx3
#get date
from datetime import date
from datetime import datetime
#robot is listening
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening...")
        audio = robot_ear.listen(mic)
    print("Robot:...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you="..."
    print("You: " + you)
    #robot understanding and reply
    if "hello" in you:
        robot_brain="Hello Tam"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        current_time = now.strftime("%H Hours %M minutes %S seconds")
        robot_brain = current_time
    elif "president" in you:
        robot_brain = "Donald Trump"
    elif "bye" in you:
        break 
    else:
        robot_brain="I can't hear you, try it again"
    print("Robot: "+robot_brain)
    #robot speech to user
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
