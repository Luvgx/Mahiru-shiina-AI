import os
import pygame
import asyncio
from dotenv import load_dotenv
from elevenlabs import save
from elevenlabs.client import ElevenLabs
from config import (TTS_MODEL, VOICE_ID, TEMP_AUDIO_FILE)

def load_api_key():
    load_dotenv()
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY not found in .env file.")
    return api_key

def initialize_client():
    api_key = load_api_key()
    client = ElevenLabs(api_key=api_key)
    return client

def generate_audio(text):
    client = initialize_client()

    print("Generating audio...")

    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id=TTS_MODEL,
        text=text,
        output_format="mp3_44100_128"
    )

    save(audio, TEMP_AUDIO_FILE)

    print("Audio saved!")
    print("File exists:", os.path.exists(TEMP_AUDIO_FILE))
    print("File size:", os.path.getsize(TEMP_AUDIO_FILE))

    # client = initialize_client()
    # audio = client.text_to_speech.convert(
    #     text=text,
    #     voice_id=VOICE_ID,
    #     model_id=TTS_MODEL,
    #     output_format="mp3_44100_128"
    # )

#  print("Audio object:", audio)

#     with open(TEMP_AUDIO_FILE, "wb") as f:
#         count = 0
#         for chunk in audio:
#             count += 1
#             print(f"Chunk {count}: {type(chunk)}")

#             if chunk:
#                 f.write(chunk)

#         print("Total chunks:", count)

#         if os.path.exists(TEMP_AUDIO_FILE):
#             print("File size:", os.path.getsize(TEMP_AUDIO_FILE))  

    # with open(TEMP_AUDIO_FILE, "wb") as f:
    #     for chunk in audio:
    #         if chunk:
    #             f.write(chunk)


def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load(TEMP_AUDIO_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

def delete_audio():
    try:
        if os.path.exists(TEMP_AUDIO_FILE):
            os.remove(TEMP_AUDIO_FILE)

    except Exception as e:
        print(f"Error deleting audio: {e}")

def speak(text):
    try:
        generate_audio(text)
        play_audio()
        delete_audio()

    except Exception as e:
        print(f"Error in speak(): {e}")

    # try:
    #     generate_audio(text)
    #     play_audio()
    #     delete_audio()

    # except Exception as e:
    #     print(f"Error in speak(): {e}")