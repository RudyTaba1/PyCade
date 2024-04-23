# Necessary packages
import os
from tkinter import *
import subprocess
import sys

root = Tk()
root.title("Pycade")



def pButton():
    try:
        subprocess.Popen(["python3", "Pong/pong.py"])
        sys.exit()
    except Exception as e:
        print("Error:", e)
   
def hmButton():
    os.system("python3 HangMan/Hangman.py")
    sys.exit() 
    
def Tbutton():
    os.system("python3 Tetris/tetris.py")
    sys.exit()
    
    
pgButton = Button(root, text="Pong", command=pButton)
pgButton.pack()

hangButton = Button(root, text="Hangman", command=hmButton)
hangButton.pack()

tetButton = Button(root, text="Tetris", command=Tbutton)
tetButton.pack()

root.mainloop()