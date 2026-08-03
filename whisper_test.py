import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import whisper

SAMPLE_RATE = 16000
DURATION = 5

print("Loading Whisper model...")
model = whisper.load_model("base")

while True:

    input("\nPress ENTER to record...")

    print("🎤 Speak now...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=0  # MacBook Air Microphone
    )

    sd.wait()

    audio = np.squeeze(audio)

    print("Max audio level:", np.max(np.abs(audio)))

    filename = "test.wav"

    write(
        filename,
        SAMPLE_RATE,
        (audio * 32767).astype(np.int16)
    )

    print("🧠 Transcribing...")

    result = model.transcribe(filename)

    text = result["text"].strip()

    print("\n==========================")
    print("Detected Text:")
    print(text)
    print("==========================\n")

    if os.path.exists(filename):
        os.remove(filename)