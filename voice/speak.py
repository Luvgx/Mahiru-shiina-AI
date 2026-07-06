import asyncio
import edge_tts
import os
import pygame

from config import (
    VOICE,
    VOICE_RATE,
    VOICE_VOLUME,
    TEMP_AUDIO_FILE
)

async def generate_audio(text):
    communicate = edge_tts.Communicate(
        text = text,
        voice = VOICE,
        rate = VOICE_RATE,
        volume = VOICE_VOLUME
    )
    await communicate.save(TEMP_AUDIO_FILE)

def play_audio():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(TEMP_AUDIO_FILE)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    finally:
        pygame.mixer.quit()


def delete_audio():
    try:
        if os.path.exists(TEMP_AUDIO_FILE):
            os.remove(TEMP_AUDIO_FILE)
    except Exception as e:
        print(f"Error deleting audio file: {e}")

def speak(text):
    try:
        asyncio.run(generate_audio(text))
        play_audio()
    
    except Exception as e:
        print(f"Error in speak(): {e}")
    finally:
        delete_audio()

