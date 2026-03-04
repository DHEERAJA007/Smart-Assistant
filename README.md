# Smart-Assistant
Bunny – Smart Voice Assistant
📌 Project Description

Bunny is a Python-based smart voice assistant that listens to user voice commands and performs various tasks such as playing music, searching Wikipedia, telling jokes, opening applications, and retrieving live sports scores.

The assistant uses Speech Recognition and Text-to-Speech technologies to create a hands-free interaction experience. It can also integrate with web services and APIs to fetch real-time information such as football match results and cricket scores.

This project demonstrates the use of Python automation, API integration, natural language processing basics, and voice interaction systems.

🚀 Features

🎤 Voice Command Recognition

Uses Google Speech Recognition to capture and interpret user voice commands.

🔊 Text-to-Speech Responses

Uses pyttsx3 to convert text responses into speech.

🎵 Play Music from YouTube

Play songs directly using voice commands.

⏰ Time Information

Get the current system time instantly.

📖 Wikipedia Search

Fetch short summaries about people or topics.

😂 Jokes Generator

Tell random programming jokes.

⚽ Live Sports Scores

Fetch cricket and football scores from the web.

📊 Football Match Results

Get the latest result of a specific football team using a sports API.

💻 System Automation
Open applications using voice commands:

Google Chrome

VS Code

Spotify

WhatsApp

Steam

File Explorer

Calculator

Notepad

🛠️ Technologies Used

Python

SpeechRecognition

pyttsx3 (Text-to-Speech)

Wikipedia API

Requests

BeautifulSoup (Web Scraping)

API-Football

PyWhatKit

📂 Project Structure
smart-assistant/
│
├── assist.py        # Main voice assistant script
├── README.md        # Project documentation
└── requirements.txt # Required libraries


The assistant will start listening for commands.

Example commands:

“Play Shape of You”

“What’s the time”

“Who is Cristiano Ronaldo”

“Tell me a joke”

“Open Chrome”

“Cricket score”

“Football result”

💡 Example Workflow

The assistant listens using the microphone.

Speech is converted to text using Google Speech Recognition.

The command is processed and matched with functions.

Bunny responds using voice output.

📈 Future Improvements

Add ChatGPT or LLM integration

Add weather updates

Add email sending

Add reminder / to-do system

Add GUI dashboard

Add wake word detection (“Hey Bunny”)
