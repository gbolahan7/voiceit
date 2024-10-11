import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer



# Download VADER lexicon if not already available
nltk.download('vader_lexicon')


class SentimentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Sentimen App")
        self.root.geometry("400x300")

        # Label to display instructions
        self.label = tk.Label(root, text="Press the button to start recording", font=("Arial", 14))
        self.label.pack(pady=20)
        
          # Button to start recording
        self.record_button = tk.Button(root, text="Record", command=self.record_audio, font=("Arial", 14), bg="lightblue")
        self.record_button.pack(pady=10)

        # Text area to display transcribed text
        self.text_area = tk.Text(root, height=5, width=40)
        self.text_area.pack(pady=10)
