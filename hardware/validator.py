
from config import HOUSE, VALID_ACTIONS


class CommandValidator:

    def validate(self, command):

        if not isinstance(command, dict):
            return False, "Invalid command format."

        if command.get("intent") != "device_control":
            return False, "Not a device-control command."

        room = command.get("room")
        device = command.get("device")
        action = command.get("action")

        if not isinstance(room, str) or not room:
            return False, "Room is missing or invalid."

        if not isinstance(device, str) or not device:
            return False, "Device is missing or invalid."

        if room not in HOUSE:
            return False, f"Unsupported room: {room}"

        if device not in HOUSE[room]:
            return False, f"Unsupported device: {device}"

        if action not in VALID_ACTIONS:
            return False, "Action must be 'on' or 'off'."

        return True, "Command validated successfully."
