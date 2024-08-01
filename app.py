import speech_recognition as sr
import pyttsx3
import requests
from transformers import pipeline
import datetime
import os

# Initialize recognizer, TTS engine, and NLP pipeline
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = pipeline("zero-shot-classification")

# Define some global variables
WAKE_WORD = ""

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Error with the speech recognition service.")
        return ""

def respond(text):
    engine.say(text)
    engine.runAndWait()


def process_command(command):
    if WAKE_WORD in command:
        command = command.replace(WAKE_WORD, '').strip()

        # Simplified command recognition
        if 'open browser' in command:
            os.system('start chrome')  # Adjust for your browser and OS
            return "Opening the browser."
        elif 'reminder' in command:
            return "Reminder feature is under development."
        elif 'joke' in command:
            return "Why did the scarecrow win an award? Because he was outstanding in his field!"
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."
        else:
            return "Sorry, I didn't understand the command."

    return "Say the wake word followed by your command."

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            response = process_command(command)
            print(f"Assistant: {response}")
            respond(response)
            if "goodbye" in command:
                break

