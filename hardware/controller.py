
import requests

ESP32_IP = "192.168.1.112"
ESP32_BASE_URL = f"http://{ESP32_IP}"


class Controller:

    def execute(self, command):

        action = command.get("action")

        if action not in ["on", "off"]:
            print("Invalid hardware action.")
            return

        endpoint = "/on" if action == "on" else "/off"

        print("\n====================")
        print(" SMART HOME ACTION ")
        print("====================")
        print("Device : ESP32 GPIO 18 LED")
        print("Action :", action.upper())

        try:
            response = requests.get(
                f"{ESP32_BASE_URL}{endpoint}",
                timeout=5
            )

            response.raise_for_status()

            print("ESP32 Response:", response.text)
            print("Hardware command completed.")

        except requests.RequestException as error:
            print("ESP32 connection failed:", error)

        print("====================")
