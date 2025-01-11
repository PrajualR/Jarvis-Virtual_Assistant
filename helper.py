import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment
API_KEY = os.getenv('API_KEY')


def google_ai(prompt):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def application_launch(app_name):
    apps = {
    "notepad": "notepad.exe",
    "camera": "start microsoft.windows.camera:",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "wordpad": "write.exe",
    "explorer": "explorer.exe"
    }
    app_command = apps.get(app_name.lower())
    if app_command:
        os.system(app_command)
    else:
        return f"App '{app_name}' not found."

if __name__ == '__main__':
    prompt = "what is the time now"
    app_name = ""
    application_launch(app_name)
    google_ai(prompt)