from config import HOUSE


class CommandValidator:

    def validate(self, command):

        if command.get("intent") != "device_control":
            return False, "Not a device command"

        room = command.get("room")
        device = command.get("device")
        action = command.get("action")

        if room not in HOUSE:
            return False, f"Invalid room: {room}"

        if device not in HOUSE[room]:
            return False, f"Invalid device: {device}"

        if action not in ["on", "off"]:
            return False, "Invalid action"

        return True, "Command valid"