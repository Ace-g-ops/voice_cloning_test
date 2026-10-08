import os
from dotenv import load_dotenv
from cartesia import Cartesia

load_dotenv()

api_key = os.getenv("CARTESIA_API_KEY")

if not api_key:
    raise RuntimeError("CARTESIA_API_KEY is missing from .env")

client = Cartesia(
    api_key=api_key,
    max_retries=2
)

with open("Cartesia_reference", "wb") as audio:
    voice = client.voices.clone(
        clip=audio,
        language="en-us",
        name="Podcast Voice",
    )

print("Voice Created")
print(f"Voice ID: {voice.id}")

with open("cartesia_voice_id.txt", "w", encoding="utf-8") as file:
    file.write(voice.id)

