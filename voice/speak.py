from config import TTS_ENGINE

if TTS_ENGINE == "elevenlabs":
    from voice.eleven_engine import speak
elif TTS_ENGINE == "edge":
    from voice.edge_engine import speak
else:
    raise ValueError(f"Unknown voice engine: {TTS_ENGINE}")

