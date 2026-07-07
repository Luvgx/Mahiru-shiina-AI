from voice.speak import speak
# def main():
#     speak("Hello Siddhant! Kya haal hai? Aaj hum kya build karne wale hain?")
from voice.listen import listen
def main():
    text = listen()
    print(text)
if __name__ == "__main__":
    main()
