import os
from pathlib import Path

from dotenv import load_dotenv
from cartesia import Cartesia

load_dotenv()

api_key = os.getenv("CARTESIA_API_KEY")

if not api_key:
    raise RuntimeError("CARTESIA_API_KEY is missing.")

audio_path = Path("reference.wav")

if not audio_path.exists():
    raise FileNotFoundError(f"Missing audio file: {audio_path}")

if audio_path.stat().st_size == 0:
    raise ValueError(f"Audio file is empty: {audio_path}")

client = Cartesia(api_key=api_key)

with audio_path.open("rb") as audio:
    voice = client.voices.clone(
        clip=audio,
        language="en",
        name="Podcast Test Voice",
    )

voice_id = voice.id

## Save the voice ID to a text file
Path("cartesia_voice_id.txt").write_text(
    voice_id,
    encoding="utf-8",
)

print("Voice created successfully")
print("Voice ID saved to cartesia_voice_id.txt")