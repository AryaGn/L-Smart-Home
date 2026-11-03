
from ai.llm import LLM
from ai.mapping import SmartMapper
from hardware.validator import CommandValidator
from hardware.controller import Controller


class Conversation:
    def __init__(self):
        self.llm = LLM()
        self.mapper = SmartMapper()
        self.validator = CommandValidator()
        self.controller = Controller()

    def process(self, command_text):
        try:
            response = self.llm.ask(command_text)

            if not isinstance(response, dict):
                print("Error: AI returned an invalid response.")
                return

            print("AI Response:", response)

            response = self.mapper.resolve(response)

            if not isinstance(response, dict):
                print("Error: Command mapping failed.")
                return

            print("Mapped:", response)

            if response.get("intent") == "chat":
                print("Rotty:", response.get("message", "I couldn't understand that."))
                return

            valid, message = self.validator.validate(response)
            print("Validator:", message)

            if not valid:
                print("Command rejected. Please try again.")
                return

            self.controller.execute(response)

        except Exception as error:
            print("Command processing error:", error)
