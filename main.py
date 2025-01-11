from helper import google_ai, application_launch
import pyttsx3
import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def google_assist(prompt):
    speak(prompt)
    result = google_ai(prompt)
    return speak(result)
def launch_app(app):
    speak(f"Opening {app}")
    result = application_launch(app)
    return speak(result)

def processing_command(cmd):
    apps = ['notepad', 'camera', 'calculator', 'paint', 'wordpad', 'explorer']

    if "open google" in cmd.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in cmd.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif cmd in apps:
        launch_app(cmd)
    else:
        google_assist(cmd.lower())


if __name__ == '__main__':
    speak("Initializing the Jarvis")
    while True:
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = recognizer.listen(source,timeout=2, phrase_time_limit=3)
            init_command = recognizer.recognize_google(audio)
            # print(init_command)
            if "jarvis" in init_command.lower():
                speak("Hi Prajual")
                #
                with sr.Microphone() as source:
                    print("You are here")
                    audio = recognizer.listen(source,timeout=2, phrase_time_limit=4)
                    command = recognizer.recognize_google(audio)

                    processing_command(command)

        except Exception as e:
            print(e)