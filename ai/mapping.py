from config import HOUSE


class SmartMapper:

    def resolve(self, command):

        if command.get("intent") != "device_control":
            return command

        room_input = command.get("room", "").lower()
        device_input = command.get("device", "").lower()

        matched_room = None

        for room in HOUSE.keys():
            if room_input in room:
                matched_room = room
                break

        if not matched_room:
            return command

        matched_device = None

        for device in HOUSE[matched_room].keys():
            if device_input in device:
                matched_device = device
                break

        if not matched_device:
            matched_device = device_input

        command["room"] = matched_room
        command["device"] = matched_device

        return command