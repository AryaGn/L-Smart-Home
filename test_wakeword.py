import sounddevice as sd
import numpy as np
from openwakeword.model import Model

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
MICROPHONE_DEVICE = 0
THRESHOLD = 0.35

print("Loading wake-word model...")

model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)

print("Wake-word model loaded.")
print("Listening for: HEY JARVIS")
print("Press Ctrl+C to stop.\n")

try:
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        blocksize=CHUNK_SIZE,
        device=MICROPHONE_DEVICE
    ) as stream:

        while True:
            audio, overflowed = stream.read(CHUNK_SIZE)

            if overflowed:
                print("Audio buffer overflow.")

            audio = np.squeeze(audio)

            prediction = model.predict(audio)

            for wakeword, score in prediction.items():
                if score >= THRESHOLD:
                    print(f"\nWAKE WORD DETECTED! Score: {score:.2f}")
                    model.reset()

except KeyboardInterrupt:
    print("\nWake-word test stopped.")