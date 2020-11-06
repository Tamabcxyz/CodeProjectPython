from tkinter import *

root = Tk()
w=500
h=300
cas = Canvas(root,width=w,height=h)
cas.pack()
cas.create_polygon(50,50,0,0,50,0, fill='red')

def movecontrol(event):
    if event.keysym == 'Up':
        cas.move(1,0,-10)# x ko doi y -10
    elif event.keysym == 'Down':
        cas.move(1,0,10)
    elif event.keysym == 'Left':
        cas.move(1,-10,0)
    else:
        cas.move(1,10,0)
cas.bind_all('<KeyPress-Up>',movecontrol)
cas.bind_all('<KeyPress-Down>',movecontrol)
cas.bind_all('<KeyPress-Left>',movecontrol)
cas.bind_all('<KeyPress-Right>',movecontrol)
root.mainloop()