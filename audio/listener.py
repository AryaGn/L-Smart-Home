import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import os

# You can change "base" to "medium" later for better multilingual accuracy
model = whisper.load_model("base")

SAMPLE_RATE = 16000


def listen_once():
    duration = 6

    print("🎤 Listening... Speak now!")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=0
    )

    sd.wait()

    audio = np.squeeze(audio)

    print("Max audio level:", np.max(np.abs(audio)))

    # Save audio
    wav_path = "temp.wav"
    write(wav_path, SAMPLE_RATE, (audio * 32767).astype(np.int16))

    print("🧠 Processing speech...")

    result = model.transcribe(
        wav_path,
        language=None,
        task="transcribe",
        fp16=False
    )

    print("Detected Language:", result["language"])

    os.remove(wav_path)

    return result["text"].strip()