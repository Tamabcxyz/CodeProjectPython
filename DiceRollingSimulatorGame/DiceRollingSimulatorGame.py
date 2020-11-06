
import tkinter
from PIL import Image, ImageTk
import random
'''
root=tkinter.Tk()
root.geometry('400x400')
root.title("DataFlair roll the dice")
BlankLine=tkinter.Label(root,text="")
BlankLine.pack()
HeadingLabel = tkinter.Label(root, text="Hello from DataFlair!",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
HeadingLabel.pack()
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
DiceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
ImageLabel=tkinter.Label(root,image=DiceImage)
ImageLabel.image=DiceImage
ImageLabel.pack(expand=True)

def roll_dice():
    DiceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    
button=tkinter.Button(root,text="Click to dice", fg='blue', command=roll_dice)
button.pack(expand=True)
root.mainloop();
'''
# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('DataFlair Roll the Dice')
# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello from DataFlair!",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget 
ImageLabel.pack( expand=True)




# images
dice1 = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage1 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))

# construct a label widget for image
ImageLabel1 = tkinter.Label(root, image=DiceImage1)
ImageLabel1.image = DiceImage1

# packing a widget in the parent widget 
ImageLabel1.pack( expand=True)





# function activated by button
def rolling_dice():
    DiceImage1 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
    # update image
    ImageLabel1.configure(image=DiceImage1)
    # keep a reference
    ImageLabel1.image = DiceImage1

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()