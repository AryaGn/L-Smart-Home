
from audio.wakeword import WakeWordListener
from audio.listener import listen_once
from ai.conversation import Conversation

conversation = Conversation()
wake_listener = WakeWordListener()

print("======================")
print("     L SMART HOME")
print("======================")
print("Assistant: Rotty")
print("Wake phrase: Hey Jarvis")
print("Example: Hey Jarvis... turn on the light.")
print("Press Ctrl+C to exit.")
print("======================")

try:
    while True:

        # Wait until the wake phrase is detected
        wake_listener.wait_for_wake_word()

        # Record the user's command using Whisper
        text = listen_once()

        if not text:
            print("No command detected. Waiting for wake phrase...")
            continue

        print("\nYou said:", text)

        # Send the command to the existing AI pipeline
        conversation.process(text)

except KeyboardInterrupt:
    print("\nL Smart Home stopped.")
