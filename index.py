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

          # Label to show conversation classification result
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def record_audio(self):
    # Capture and transcribe audio
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.config(text="Recording... Please speak")
            audio = recognizer.listen(source)

            try:
                # Transcribing the audio
                self.label.config(text="Transcribing...")
                text = recognizer.recognize_google(audio)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, text)
                self.label.config(text="Press the button to start recording")

                # Analyze the sentiment of the transcribed text
                conversation_type = self.analyze_sentiment(text)
                self.result_label.config(text=f"Conversation: {conversation_type}")

            except sr.UnknownValueError:
                messagebox.showerror("Error", "Could not understand the audio")
            except sr.RequestError as e:
                messagebox.showerror("Error", f"Could not request results; {e}")
