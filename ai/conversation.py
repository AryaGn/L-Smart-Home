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

        response = self.llm.ask(command_text)
        print("AI Response:", response)

        response = self.mapper.resolve(response)
        print("Mapped:", response)

        valid, msg = self.validator.validate(response)
        print("Validator:", msg)

        if valid:
            self.controller.execute(response)