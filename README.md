# Sim Sim: AI Assistant

Sim-Sim is a Python-based AI assistant that can perform various tasks such as responding to voice commands, fetching the latest news, playing games, setting alarms, providing weather updates, and much more.

For the main functionality of the project, please refer to the [Sim_main.py](Sim_main.py) file.


## Features

- Voice recognition and response: Sim-Sim can recognize voice commands using the SpeechRecognition library and respond to them using text-to-speech technology.
- Graphical user interface: Sim-Sim comes with a simple GUI built using the PySide6 library, allowing users to interact with the assistant in a user-friendly manner.
- Task automation: Sim-Sim can perform various tasks such as opening applications, searching the web, fetching weather updates, setting alarms, and more.
- Speedtest integration: Sim-Sim can measure internet speed using the Speedtest library and provide users with download and upload speed information.
- News updates: Sim-Sim can fetch the latest news headlines from the web and display them to the user.
- Games: Sim-Sim can play simple games like Rock, Paper, Scissors with the user.

- For in detail look of the features, please refer to the [commands.txt](commands.txt) file.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/aryannaik225/Virtual-Assistant.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python Sim_main.py
```

## Usage

- Upon running the application, the Sim-Sim GUI will appear on the screen.
- Say "Khul ja Sim Sim" or "Open Sim Sim" and Sim-Sim boots up ready to listen to your commands.
- Sim-Sim will process your command and respond accordingly.
- Once done, say "Go to sleep" or "Soja Sim Sim" to temporarily sleep Sim-Sim.
- Or say "Band Hoja Sim Sim" or "Close Sim Sim" to exit the application completely.

## Dependencies

- Python 3.x
- PySide6
- SpeechRecognition
- pyttsx3
- requests
- BeautifulSoup
- pyautogui
- pygame
- speedtest-cli
- plyer
- pyjokes

## Acknowledgements

- Thanks to the developers of the various Python libraries used in this project.

---
