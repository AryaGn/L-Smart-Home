import requests

ESP32_IP = "192.168.1.80"


class Controller:

    def execute(self, command):

        action = command["action"]

        print("\n====================")
        print(" SMART HOME ACTION ")
        print("====================")
        print("Room   :", command["room"])
        print("Device :", command["device"])
        print("Action :", action)

        try:

            if action == "on":
                response = requests.get(
                    f"http://{ESP32_IP}/on",
                    timeout=3
                )

            else:
                response = requests.get(
                    f"http://{ESP32_IP}/off",
                    timeout=3
                )

            print("ESP32:", response.text)

        except Exception as e:

            print("ESP32 Error:", e)

        print("====================")