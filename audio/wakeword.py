
import sounddevice as sd
import numpy as np
from openwakeword.model import Model


class WakeWordListener:

    def __init__(self):
        self.sample_rate = 16000
        self.chunk_size = 1280
        self.microphone_device = 0
        self.threshold = 0.35

        print("Loading wake-word model...")

        self.model = Model(
            wakeword_models=["hey_jarvis"],
            inference_framework="onnx"
        )

        print("Wake-word model loaded successfully.")

    def wait_for_wake_word(self):

        print("\nListening for: HEY JARVIS")

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self.chunk_size,
            device=self.microphone_device
        ) as stream:

            while True:

                audio, overflowed = stream.read(self.chunk_size)

                if overflowed:
                    print("Audio buffer overflow.")

                audio = np.squeeze(audio)

                prediction = self.model.predict(audio)

                score = prediction.get("hey_jarvis", 0)

                if score >= self.threshold:

                    print(f"\nWake word detected! Score: {score:.2f}")

                    self.model.reset()

                    return True
