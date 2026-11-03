
import json
import ollama

from config import ASSISTANT_NAME


class LLM:

    def __init__(self, model="llama3.2:3b"):
        self.model = model

    def ask(self, user_input):

        system_prompt = f"""
You are {ASSISTANT_NAME}, an AI-powered smart home assistant.

You interpret natural-language voice commands and return
structured JSON responses.

The user may speak English or another language.
Understand multilingual commands when possible.

CURRENT HARDWARE

This prototype currently controls ONE physical LED
connected to ESP32 GPIO pin 18.

It does not currently have independently connected
lights, fans, air conditioners, or multiple rooms.

SUPPORTED COMMANDS

Turn the demo LED ON:
{{
    "intent": "device_control",
    "room": "demo",
    "device": "light",
    "action": "on"
}}

Turn the demo LED OFF:
{{
    "intent": "device_control",
    "room": "demo",
    "device": "light",
    "action": "off"
}}

IMPORTANT RULES

1. Return ONLY valid JSON.
2. Never use Markdown or code fences.
3. Never include explanations outside JSON.
4. For a clear request to turn the light on or off,
   use the device_control format above.
5. Always use room "demo" and device "light"
   for the connected demonstration LED.
6. If the user requests a specific room, fan, AC,
   or another device that is not connected, do not
   pretend it is operational. Return a chat response
   explaining that only the demo LED is currently connected.
7. If the request is unclear, ask for clarification
   using the chat format.
8. For unrelated questions, use the chat format.

CHAT FORMAT

{{
    "intent": "chat",
    "message": "Your response here"
}}

Return ONLY valid JSON.
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

            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()

            result = json.loads(content)

            if not isinstance(result, dict):
                raise ValueError("AI response must be a JSON object.")

            return result

        except json.JSONDecodeError:

            print("\n========== JSON ERROR ==========")
            print(content)
            print("================================\n")

            return {
                "intent": "chat",
                "message": "Sorry, I couldn't understand that command."
            }

        except Exception as error:

            print("\n========== OLLAMA ERROR ==========")
            print(error)
            print("==================================\n")

            return {
                "intent": "chat",
                "message": "Sorry, I couldn't process that request."
            }
