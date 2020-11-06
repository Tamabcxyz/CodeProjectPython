from tkinter import *
from datetime import datetime
import time
import winsound
import playsound

def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        current_date=now.strftime("%d/%m/%Y")
        print("The set time is ", set_alarm_time)
        print("Current time is ", current_time)
        print("You want to get up at ", set_alarm_time)
        if current_time == set_alarm_time:
            print("This time for wake up get up...")
            #winsound.PlaySound("D://bird.wav", winsound.SND_ASYNC)
            playsound('bird.mp3')
            break
        
def actualy_time():
    set_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_timer)
    
clock =Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text="Enter time in 24h", fg="red", bg="black", font="Arial").place(x=60, y=120)
add_time=Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

hour=StringVar()
min=StringVar()
sec=StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actualy_time).place(x =110,y=70)

clock.mainloop()