
from config import HOUSE


class SmartMapper:

    def resolve(self, command):
        if not isinstance(command, dict):
            return command

        if command.get("intent") != "device_control":
            return command

        room_input = command.get("room")
        device_input = command.get("device")

        if not isinstance(room_input, str) or not isinstance(device_input, str):
            return command

        room_input = room_input.strip().lower()
        device_input = device_input.strip().lower()

        matched_room = None

        for room in HOUSE:
            if room_input == room.lower():
                matched_room = room
                break

        if not matched_room:
            return command

        matched_device = None

        for device in HOUSE[matched_room]:
            if device_input == device.lower():
                matched_device = device
                break

        if not matched_device:
            return command

        mapped_command = command.copy()
        mapped_command["room"] = matched_room
        mapped_command["device"] = matched_device

        return mapped_command
