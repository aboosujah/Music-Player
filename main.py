import tkinter as tk
from tkinter import filedialog
from pygame import mixer
from tkinter import ttk



class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.music_file = None
        self.paused = False

        self.create_widgets()
        
    def select_music(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3",
        filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])

        if self.music_file:
            self.song_label.config(text=f"Playing: {self.music_file}")

    def play_music(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause_music(self):
        if self.music_file:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
            else:
                mixer.music.pause()
                self.paused = True