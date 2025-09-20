import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess
import wikipedia   # NEW: Wikipedia library

recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that. Please say again.")
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable right now.")
            return ""

def open_app(app_name):
    if "notepad" in app_name:
        os.system("notepad")
        speak("Opening Notepad")
    elif "calculator" in app_name:
        os.system("calc")
        speak("Opening Calculator")
    elif "chrome" in app_name:
        path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        if os.path.exists(path):
            subprocess.Popen([path])
            speak("Opening Chrome")
        else:
            speak("Chrome is not installed in the default location.")
    else:
        speak("Sorry, I don't know how to open that app yet.")

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "how are you" in command:
        speak("I'm doing great, thank you for asking!")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
        else:
            speak("What would you like me to search for?")

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_app(app_name)

    # NEW FEATURE: Wikipedia Q&A with Google fallback
    elif "who is" in command or "tell me about" in command or "what is" in command or "where is" in command:
        try:
            query = command.replace("who is", "").replace("tell me about", "")
            query = query.replace("what is", "").replace("where is", "").strip()
            
            if query:
                try:
                    summary = wikipedia.summary(query, sentences=2)
                    speak(summary)
                except wikipedia.DisambiguationError as e:
                    speak(f"Your query is too broad. Here’s the first option: {e.options[0]}")
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                except wikipedia.PageError:
                    speak("I couldn’t find anything on Wikipedia. Let me check Google.")
                    webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("Please tell me what you want to know about.")

        except Exception:
            speak("I had trouble getting information. Let me check Google instead.")
            webbrowser.open(f"https://www.google.com/search?q={command}")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I can only respond to greetings, time, date, search, open apps, or general questions.")
    return True

# Main loop
speak("Advanced Voice Assistant activated. You can say hello, time, date, search, open apps, or ask me about anything.")
running = True
while running:
    command = listen()
    if command:
        running = process_command(command)

