Jarvis Virtual Assistant

A simple voice-activated virtual assistant built in Python, designed to perform a variety of tasks like opening applications, browsing the web, and responding to queries using Google's AI.

Features
Voice Commands: Initiate the assistant using the keyword "Jarvis".
Open Applications: Open commonly used applications like Notepad, Calculator, Paint, and more.
Google Search: Send voice prompts to Google’s AI and get responses.
Web Browsing: Open websites like Google, YouTube, etc., via voice command.
Custom Commands: Extendable to add more voice commands and functionalities.

Requirements
Python 3.x
pyttsx3 for text-to-speech (TTS) functionality
speech_recognition for speech-to-text functionality
webbrowser for opening websites in the default browser
Google AI integration (through google_ai function in helper.py)

Installation
Clone the repository to your local machine:

git clone https://github.com/yourusername/Jarvis-Virtual_Assistant.git
Install the required Python libraries:

pip install pyttsx3 speechrecognition webbrowser

Set up Google API integration by adding your API key to the helper.py file.

Usage
Ensure your microphone is properly connected to your system.

Run the script:
python jarvis_assistant.py

The assistant will initialize and wait for the keyword "Jarvis". Once "Jarvis" is detected, you can issue commands like:

Open applications: "Open Notepad", "Open Calculator"
Web search: "Search for Python tutorials"
Open websites: "Open Google", "Open YouTube"

Code Structure
jarvis_assistant.py: Main script that listens for voice commands and processes them.
helper.py: Contains functions for Google AI interaction and launching applications.
.env: A file to store sensitive information like your API keys. Make sure this file is added to .gitignore to prevent it from being pushed to GitHub.