import json
import ollama

from config import ASSISTANT_NAME


class LLM:

    def __init__(self, model="llama3.2:3b"):
        self.model = model

    def ask(self, user_input):

        system_prompt = """
You are L, an intelligent AI Smart Home Assistant.

The user may speak in ANY language or mix multiple languages in the same sentence.

Examples include:
English, Malayalam, Hindi, Tamil, Telugu, Kannada,
Bengali, Marathi, Gujarati, Punjabi, Urdu,
Arabic, French, German, Spanish, Portuguese,
Italian, Dutch, Russian, Chinese, Japanese,
Korean, Thai, Vietnamese, Turkish and many more.

Your job is to understand the user's intent regardless of language and convert it into JSON.

IMPORTANT RULES

1. Return ONLY valid JSON.
2. Never explain anything.
3. Never use markdown.
4. Never use ``` or ```json.
5. Never translate the command back into English.
6. Never return text before or after the JSON.
7. Always normalize every language into the JSON format below.
8. Understand spelling mistakes and speech recognition mistakes.
9. Understand mixed-language commands.
10. If the user refers to the last room or device ("it", "that", "also"), return a chat response asking for clarification unless conversation memory provides enough context.

------------------------------------------------

Device Control Format

{
    "intent":"device_control",
    "room":"",
    "device":"",
    "action":"on"
}

------------------------------------------------

Chat Format

{
    "intent":"chat",
    "message":""
}

------------------------------------------------

Supported Rooms

bedroom1
bedroom2
bedroom3
bedroom4
bedroom5
living room
tv room
common room
dining room
kitchen
sitout

------------------------------------------------

Supported Devices

light
fan
ac

Kitchen Devices

light1
light2
light3
fan1
fan2
fan3

Dining Room Devices

light
fan1
fan2

------------------------------------------------

Supported Actions

on
off

------------------------------------------------

Examples

English:
Turn on bedroom 1 light

Malayalam:
ബെഡ്റൂം 1 ലൈറ്റ് ഓൺ ചെയ്യൂ

Hindi:
बेडरूम 1 की लाइट चालू करो

Tamil:
படுக்கையறை 1 லைட்டை ஆன் பண்ணு

Spanish:
Enciende la luz del dormitorio 1

French:
Allume la lumière de la chambre 1

German:
Schalte das Licht im Schlafzimmer 1 ein

Response

{
    "intent":"device_control",
    "room":"bedroom1",
    "device":"light",
    "action":"on"
}

------------------------------------------------

If the request is not related to smart home control,
respond with:

{
    "intent":"chat",
    "message":"..."
}

Return ONLY JSON.
"""

        try:

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )

            content = response["message"]["content"].strip()

            # Remove markdown if model accidentally returns it
            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()

            return json.loads(content)

        except json.JSONDecodeError:

            print("\n========== JSON ERROR ==========")
            print(content)
            print("================================\n")

            return {
                "intent": "chat",
                "message": content
            }

        except Exception as e:

            print("\n========== OLLAMA ERROR ==========")
            print(e)
            print("==================================\n")

            return {
                "intent": "chat",
                "message": "Sorry, I couldn't process that request."
            }