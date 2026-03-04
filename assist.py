import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    print("Bunny:", text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")    
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
    except sr.UnknownValueError:
        talk("Sorry mawaa, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def get_match_score(sport="cricket"):
    try:
        search_query = f"{sport} live score"
        url = f"https://www.google.com/search?q={search_query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        score_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        if score_div:
            score = score_div.text
            talk(f"Here's the latest {sport} score: {score}")
        else:
            talk(f"Sorry, I couldn’t fetch {sport} score right now.")
    except Exception as e:
        talk("An error occurred while fetching score.")

import requests

def get_latest_football_result(team_name):
    try:
        api_key = "29be49b1ed3070eb2fcd83c75f12bd0d"

        # First: search for team ID
        team_search_url = "https://v3.football.api-sports.io/teams"
        headers = {
            "x-apisports-key": api_key
        }
        search = requests.get(team_search_url, headers=headers, params={"search": team_name})
        team_data = search.json()

        if not team_data["response"]:
            talk(f"Sorry, I couldn’t find a team named {team_name}.")
            return

        team_id = team_data["response"][0]["team"]["id"]
        fixtures_url = "https://v3.football.api-sports.io/fixtures"
        match = requests.get(fixtures_url, headers=headers, params={"team": team_id, "last": 1})
        match_data = match.json()

        if not match_data["response"]:
            talk(f"Couldn't fetch match data for {team_name}.")
            return

        fixture = match_data["response"][0]
        home = fixture["teams"]["home"]["name"]
        away = fixture["teams"]["away"]["name"]
        score_home = fixture["goals"]["home"]
        score_away = fixture["goals"]["away"]
        date = fixture["fixture"]["date"][:10]
        status = fixture["fixture"]["status"]["short"]

        result = f"{home} {score_home} - {score_away} {away} on {date}, status: {status}"
        talk(f"Last match result: {result}")

    except Exception as e:
        print("Error:", e)
        talk("Something went wrong fetching the result.")



def run_bunny():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing on YouTube")
        pywhatkit.playonyt(song)

    elif "what's the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time}")

    elif "who is The owner of this laptop" in command or "who is Dheeraj" in command:
        info = (
            "Dheeraj is the owner of this laptop and he is studying in 4th year B.tech in Vellore Institute of Technology. "
            "He named me after his very own nickname BUNNY."
        )
        talk(info)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome")
            os.startfile(chrome_path)
        else:
            talk("Chrome not found")

    elif "open steam" in command:
        steam_path = "C:\\Users\\amsdh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam"
        if os.path.exists(steam_path):
            talk("Opening steam")
            os.startfile(steam_path)
        else:
            talk("Steam not found")


    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code")
        os.system("code")

    elif "open whatsapp" in command:
        talk("Opening whatsapp")
        os.system("start whatsapp:")

    elif "open spotify" in command:
        talk("Opening Spotify")
        os.system("start spotify:")
        
    elif "open pintrest" in command:
        talk("Opening pintrest")
        os.system("start Pintrest:")

    elif "open file explorer" in command or "open explorer" in command:
        talk("Opening File Explorer")
        os.system("explorer")

    elif "open calculator" in command:
        talk("Opening Calculator")
        os.system("calc")

    elif "open notepad" in command:
        talk("Opening Notepad")
        os.system("notepad")

    elif "cricket" in command and "score" in command:
        talk("Fetching live cricket score")
        get_match_score("cricket")

    elif "football" in command and "score" in command:
        talk("Fetching live football score")
        get_match_score("football")

    elif "exit" in command or "stop" in command:
        talk("Okay mawaa, see you later")
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet")

    elif "match result" in command or "football result" in command or "team result" in command:
        talk("Which football team's result do you want?")
        team_name = take_command()
        if team_name:
            get_latest_football_result(team_name)
        else:
            talk("I didn’t hear the team name.")


    

talk("Hello mawaa! I'm Bunny your personal voice assistant!! How can I help you")
while True:
    run_bunny()