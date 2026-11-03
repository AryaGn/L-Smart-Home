# L-Smart-Home 

### AI-Powered Voice-Controlled Smart Home Automation

L-Smart-Home is an AI-powered smart home automation prototype that allows users to control a physical device using natural voice commands.

The system listens for the wake phrase **"Hey Jarvis"**, captures the user's voice command, interprets it using a locally running Large Language Model (LLM), validates the command, and communicates with an ESP32 over Wi-Fi to control an LED.

The voice assistant is named **Rotty**.

## ✨ Features

- **Wake-word detection:** Activates when the user says "Hey Jarvis".
- **Speech recognition:** Uses OpenAI Whisper to convert speech into text.
- **AI command interpretation:** Uses Ollama with Llama 3.2 to understand natural-language commands.
- **Command mapping:** Converts interpreted commands into structured device actions.
- **Command validation:** Checks commands before sending them to the hardware.
- **Wi-Fi communication:** Sends HTTP requests to an ESP32.
- **Physical device control:** Turns an LED ON or OFF using ESP32 GPIO 18.

## 🏗️ System Architecture

```text
User Voice
    |
    v
Microphone
    |
    v
OpenWakeWord
(Wake phrase detection)
    |
    v
OpenAI Whisper
(Speech-to-text)
    |
    v
Ollama + Llama 3.2
(Natural-language understanding)
    |
    v
Command Mapping
    |
    v
Command Validation
    |
    v
HTTP Request over Wi-Fi
    |
    v
ESP32
    |
    v
LED ON / OFF
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main application |
| OpenWakeWord | Wake-word detection |
| OpenAI Whisper | Speech recognition |
| Ollama | Local LLM execution |
| Llama 3.2 (3B) | Voice-command interpretation |
| NumPy | Audio processing |
| SoundDevice | Microphone input |
| Requests | HTTP communication |
| ESP32 | Hardware controller |

## 🔌 Hardware Requirements

- ESP32 development board
- LED
- 220Ω resistor
- Breadboard
- Jumper wires
- Laptop or computer with a microphone
- Wi-Fi network

**Current prototype:** One LED connected to ESP32 GPIO 18.

## ⚙️ Software Requirements

- Python 3.12
- Ollama
- Llama 3.2 (3B) model
- Arduino IDE with ESP32 board support
- Git

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AryaGn/L-Smart-Home.git
cd L-Smart-Home
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and configure Ollama

Install Ollama from:

https://ollama.com/

Download the model:

```bash
ollama pull llama3.2:3b
```

Ensure Ollama is running before starting the application.

### 5. Configure the ESP32

Upload the ESP32 firmware that provides an HTTP server with `/on` and `/off` endpoints.

Configure the ESP32 to connect to your Wi-Fi network.

Update the ESP32 IP address in:

```text
hardware/controller.py
```

Make sure the laptop and ESP32 are connected to the same local Wi-Fi network.

### 6. Run the application

```bash
python main.py
```

## 🎤 How to Use

1. Start the Python application.
2. Wait for the assistant to listen for the wake phrase.
3. Say **"Hey Jarvis"**.
4. Pause briefly, then speak your command.

Example commands:

```text
Hey Jarvis... turn on the lights.
Hey Jarvis... turn off the lights.
```

The application processes the command and sends the corresponding HTTP request to the ESP32.

## Current Prototype Capabilities

| Capability | Status |
|---|---|
| Wake-word detection | Implemented |
| Speech-to-text | Implemented |
| Local AI command interpretation | Implemented |
| Command validation | Implemented |
| ESP32 Wi-Fi communication | Implemented |
| LED ON/OFF control | Working |
| Multiple room automation | Future enhancement |
| Fan and AC control | Future enhancement |
| Standalone operation without laptop | Future enhancement |

## Safety and Limitations

- The laptop must remain powered on with the application running.
- The ESP32 and laptop must share the same local Wi-Fi network.
- The current working demonstration controls one LED only.
- The prototype does not directly control mains-powered appliances.
- Do not connect household electrical appliances without properly rated isolated relay hardware and qualified supervision.
- Keep Wi-Fi credentials and other secrets out of the public repository.

## Future Enhancements

- Multiple device and room support
- Relay-based appliance control with appropriate electrical isolation
- Improved continuous voice interaction
- Configurable hardware network settings
- Standalone embedded voice-control architecture
- Expanded wake-word customization

## Author

**Arya Gopakumar**

GitHub: https://github.com/AryaGn

---

*L-Smart-Home is a prototype developed to explore the integration of artificial intelligence, speech recognition, natural-language processing, and embedded hardware for smart home automation.*