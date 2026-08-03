from audio.listener import listen_once
from ai.conversation import Conversation

conversation = Conversation()

WAKE_WORD = "l"

print("======================")
print("     L IS READY")
print("======================")

while True:

    text = listen_once()

    if not text:
        continue

    print("\nYou said:", text)

    text_lower = text.lower().strip()

    # Wake word detection
    if not (
        text_lower.startswith("l ")
        or text_lower.startswith("l,")
        or text_lower == "l"
    ):
        print("No wake word detected")
        continue

    # Remove wake word
    command_text = text_lower[1:].strip(" ,")

    print("Command:", command_text)

    conversation.process(command_text)