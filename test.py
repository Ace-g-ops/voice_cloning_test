from google.cloud import texttospeech
from pathlib import Path

client = texttospeech.TextToSpeechClient()

##this code reads the text from a file named "script.txt", splits it into chunks based on double newlines, and then synthesizes speech for each chunk using Google Cloud's Text-to-Speech API. The synthesized audio is saved as WAV files in a directory named "chunks".
script = Path("script.txt").read_text(encoding="utf-8")
chunks = [chunk.strip() for chunk in script.split("\n\n") if chunk.strip()]

output_dir = Path("chunks")
output_dir.mkdir(exist_ok=True)

for index, chunk in enumerate(chunks, start=1):
    response = client.synthesize_speech(
        ##the synthesis input is the textto be converted to speech
        input=texttospeech.SynthesisInput(text=chunk),
        #the voice parameters for the speech synthesis
        voice=texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Chirp3-HD-Charon",
        ),
        #the audio configuration for the speech synthesis
        audio_config=texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            speaking_rate=1.0,
        ),
    )

    output_file = output_dir / f"{index:03d}.wav"
    output_file.write_bytes(response.audio_content)


print(f"Created {output_file}")