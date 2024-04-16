# Necessary packages

import tkinter as tk
import os

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("Game Menu")

        self.label = tk.Label(master, text="Choose a game to play")
        self.label.pack()

        self.tetris_button = tk.Button(master, text="Tetris", command=self.tetButton)
        self.tetris_button.pack()

        self.pong_button = tk.Button(master, text="Pong", command=self.pButton)
        self.pong_button.pack()

        self.hangman_button = tk.Button(master, text="Hangman", command=self.hmButton)
        self.hangman_button.pack()

    def tetButton(self):
        # Button for tetris
        # It will pull up a CLI and run "python3 tetris.py"
        # Then play tetris
        os.system("python3 tetris.py")
        print("Tetris")

    def pButton(self):
        # Button for pong
        pass

    def hmButton(self):
        # Button for hangman
        # It will pull up a CLI and run "python3 hangman.py"
        # Then play hangman
        os.system("python3 hangman.py")

    def easterEgg(self):
        pass
