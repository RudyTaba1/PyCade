
import os
from tkinter import *
import subprocess
import sys
from PIL import Image, ImageTk

root = Tk()
root.title("Pycade")
root.geometry('400x400')



# Function to launch Pong
def pButton():
    subprocess.Popen(["python3", "Pong/pong.py"])
    sys.exit()
       
# Function to launch Hangman
def hmButton():
    os.system("python3 HangMan/Hangman.py")
    sys.exit()
   
# Function to launch Tetris
def Tbutton():
    os.system("python3 Tetris/tetris.py")
    sys.exit()
    
    
def resize(e):
    print(e)
    
root.bind("<Configure>", resize)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# Load and display image
img = Image.open("MenuIntegration/arcade.gif")
img = img.resize((400, 400))
photo = ImageTk.PhotoImage(img)

# Load and display the title image
title_img = Image.open("MenuIntegration/arcade2.png")  
title_img = title_img.resize((150, 100))
title_photo = ImageTk.PhotoImage(title_img)

title_label = Label(root, image=title_photo)
title_label.image = title_photo


#Canvas stuff
canvas = Canvas(root, width=400, height=400)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, anchor=NW, image=photo)
    
title_label_window = canvas.create_window(200, 50, anchor='n', window=title_label)
# Create buttons with fixed size
pgButton = Button(root, text="Pong", command=pButton, padx=10, pady=10, width=10)
pgButton_window = canvas.create_window(200, 150, anchor='n', window=pgButton)

hangButton = Button(root, text="Hangman", command=hmButton, padx=10, pady=10, width=10)
#hangButton.grid(row=2, column=0,padx = 10, pady = 5, sticky="nsew")
hmButton_window = canvas.create_window(200, 200, anchor='n', window=hangButton)

tetButton = Button(root, text="Tetris", command=Tbutton, padx=10, pady=10, width=10)
#tetButton.grid(row=3, column=0, padx = 10, pady = 5, sticky="nsew")
tetButton_window = canvas.create_window(200, 250, anchor='n', window=tetButton)

exitButton = Button(root, text="Exit", command=root.quit, padx=10, pady=10, width=10)
#exitButton.grid(row=4, column=0, padx = 10, pady = 5 ,sticky="nsew")
exitButton_window = canvas.create_window(200, 300, anchor='n', window=exitButton)

root.mainloop()


