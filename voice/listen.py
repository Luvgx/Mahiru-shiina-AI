import speech_recognition as sr
from config import USER_NAME

def initialize_recognizer():
    recognizer = sr.Recognizer()
    return recognizer

def initialize_microphone():
    microphone = sr.Microphone()
    return microphone

def capture_audio(recognizer, microphone):
    with microphone as source: #it will automaticaly close progamme!
        print("Listening...") 
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        return audio

def speech_to_text(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError as e:
        print(f"Speech Recognition Error: {e}")
        return None

def listen():
    try:
        recognizer = initialize_recognizer()
        microphone = initialize_microphone()
        audio = capture_audio(
            recognizer,
            microphone
        )
        text = speech_to_text(
            recognizer,
            audio
        )
        return text

    except Exception as e:
        print(f"Error in listen(): {e}")
        return None
