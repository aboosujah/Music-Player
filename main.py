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
    
    def create_widgets(self):
        self.select_button = ttk.Button(self.root, text="Select Music", command=self.select_music,)
        self.select_button.pack(pady=10)

        self.song_label = ttk.Label(self.root, text="no music", font=("Helvetica", 12),justify='center',background= "#adb8c2")
        self.song_label.pack(pady=10)

        self.controls_frame = ttk.Frame(self.root)
        self.controls_frame.pack(pady=140)

        self.play_button = ttk.Button(self.controls_frame, text="Play", command=self.play_music)
        self.play_button.grid(row=0, column=0, padx=10)

        self.pause_button = ttk.Button(self.controls_frame, text="Pause", command=self.pause_music)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.stop_button = ttk.Button(self.controls_frame, text="Stop", command=self.stop_music,)
        self.stop_button.grid(row=0, column=2, padx=10)
        
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

    def stop_music(self):
        if self.music_file:
            mixer.music.stop()


if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TButton", padding=0, font=("Helvetica", 12),Background="blue")
    music_player = MusicPlayer(root)
    root.mainloop()

