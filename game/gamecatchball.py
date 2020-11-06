from tkinter import *
import time
import random
w=820
h=500
class Ball:
    def __init__(self,Canvas,color,coordinate_bar):#need a Canvas and color
        self.Canvas=Canvas# receive Canvas input
        self.id=Canvas.create_oval(10,10,25,25,fill=color)#when create Canvas will return values id
        self.Canvas.move(self.id,100,10)
        self.status = False
        #random coordinate x
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)
        #save coordinate x,y of ball
        self.x=start[0]
        self.y=1
        # receive coordinate of bar
        self.coordinatebar=coordinate_bar
        self.core=0
        self.idtext=Canvas.create_text(400,10,text="Your core is:0",font=('Arial',20,'bold'))
    #process event impact receive into coordinate of ball
    def bothimpact(self,pos):
        pos_bar=self.Canvas.coords(self.coordinatebar.id)
        if pos[2]>=pos_bar[0] and pos[2]<=pos_bar[2]:#impact here
            if pos[3]>=pos_bar[1] and pos[3]<=pos_bar[3]:
                return True
    def draw(self):
        self.Canvas.move(self.id,self.x,self.y)
        # receive position currently of ball when ball move
        pos=self.Canvas.coords(self.id)
        if pos[1]<=0:
            self.y=2 # stop move with value 0, with values 3 mean increase 3
        elif self.bothimpact(pos)==True:
            self.y=-2
            self.core+=1
            self.Canvas.delete(self.idtext)
            self.idtext=self.Canvas.create_text(400,10,text=f"Your core is:{self.core}",font=('Arial',20,'bold'))
            if self.core==5:
                self.status=True
                self.Canvas.create_text(300,200,text="You Win", font=('Arial',50,'bold'), fill='red')
        elif pos[3]>=h:
            self.status=True
            self.Canvas.create_text(300,200,text="Game over", font=('Arial',50,'bold'), fill='red')
        elif pos[0]<=0:
            self.x=2
        elif pos[2]>=w:
            self.x=-2
class Bar:
    def __init__(self,Canvas,color):#need a Canvas and color
        self.Canvas=Canvas# receive Canvas input
        self.id=Canvas.create_rectangle(0,0,100,20,fill=color)#when create Canvas will return values id
        self.Canvas.move(self.id,360,400)
        self.x=0 #coordinate of bar
        self.y=0
        can.bind_all('<KeyPress-Left>',self.turnleft)
        can.bind_all('<KeyPress-Right>',self.turnright)
    def draw(self):
        self.Canvas.move(self.id,self.x,self.y)
    def turnleft(self,event):
        #self.x=self.x-1
        self.Canvas.move(1,-40,0)
    def turnright(self,event):
        #self.x=self.x+1
        self.Canvas.move(1,40,0)
root=Tk()
root.title('Game catch ball')
root.resizable(0,0)
can = Canvas(root,width=w,height=h)
can.pack()
thanhtruoc=Bar(can,"black")
bong=Ball(can,"red",thanhtruoc)
# interator
while True:
    if bong.status!=True:
        bong.draw()
        thanhtruoc.draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.01)
    else:
        break
print('End game')
root.mainloop()
