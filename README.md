# Voice Assistant in Python 🎙️🤖

🎯 Objective

The goal of this project is to develop a Voice Assistant in Python that listens to voice commands, processes them, and performs useful tasks. The assistant is implemented in two stages:

Basic Version: Handles simple commands such as greeting the user, telling the time/date, and searching the web.

Advanced Version: Adds extended features like opening applications, answering general knowledge questions via Wikipedia, and providing Google search results as fallback.

🛠️ Steps Performed
🔹 Basic Features

Voice Input – Captures audio via microphone using speech_recognition.

Speech Output – Converts text responses to speech using pyttsx3.

Simple Commands – Responds to:

"hello" / "how are you"

"time" → tells current time

"date" → tells today’s date

"search <query>" → opens Google search

🔹 Advanced Features

Open Applications

Open Notepad, Calculator, or Chrome directly via command.

Wikipedia Integration

Answers general questions like "Who is Elon Musk?" or "Tell me about Python" using the wikipedia library.

Handles disambiguation errors and page errors gracefully.

Fallback to Google Search

If Wikipedia cannot provide an answer, the assistant automatically opens a Google search for the query.

Exit Command

Ends the assistant on commands like "stop" or "exit".

⚙️ Tools & Technologies Used

Python

Libraries:

speech_recognition – Speech-to-text

pyttsx3 – Text-to-speech

datetime – Time & date functions

webbrowser – Web searches

os, subprocess – Open desktop apps

wikipedia – Fetch information summaries

✅ Outcome

Built a working interactive assistant capable of:

Greeting and small talk

Telling the date & time

Performing Google searches

Opening system applications

Answering knowledge-based queries from Wikipedia

🚀 Future Enhancements

Add NLP (Natural Language Processing) for better understanding of free-form queries.

Integrate with weather API for real-time weather updates.

Enable email sending, reminders, and task management.

Add customizable commands for personalization.

Demonstrates practical use of speech recognition, automation, and information retrieval.

