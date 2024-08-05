import speech_recognition as sr
import os
import win32com.client
import webbrowser
import wikipedia
import datetime
import requests
from huggingface_hub import InferenceClient
from config import wa_path, HF_TOKEN
from commands import songs, sites

# Initialize Text-to-Speech engine
try:
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("At your service sir! What can I do for you?")
except Exception as e:
    print(f"Error initializing TTS engine: {e}")


# Hugging Face AI Assistant

client = InferenceClient(
    "microsoft/Phi-3-mini-4k-instruct",
    token=HF_TOKEN,
)

def get_ai_response(prompt):
        answer = ""
        for message in client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            stream=True,
            ):
                answer += message.choices[0].delta.content
            
        return answer

def getWeather(city):
    try:
        key = "c726c328b68da1dd57231b76a50eaf12"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        response = requests.get(api)
        data = response.json()
        if data['cod'] != 200:
            raise ValueError("Invalid city name")
        temp = round(data['main']['temp'] - 273.15, 2)
        print(f"Name of the city: {data['name']}")
        print(f"Temperature: {temp} °C")
        speaker.Speak(f"The temperature in {city} is {temp} degree celsius")
    except Exception as e:
        print(f"Error fetching weather: {e}")
        speaker.Speak("Cannot find the city sir")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 500 
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

while True:
    text = listen()
    if text is None:
        continue

    try:
        # Check and open websites
        for site in sites:
            if site[0].lower() in text.lower():
                speaker.Speak(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
                break

        # Check and play songs
        for music in songs:
            if music[0].lower() in text.lower():
                speaker.Speak(f"Playing {music[0]} sir")
                os.startfile(music[1])
                break

        if "music" in text.lower():
            speaker.Speak("Playing Music sir")
            music = r"C:\Users\devar\Music\Musify\Download\Dil_Chori.mp3"
            os.startfile(music)

        elif "code" in text.lower():
            speaker.Speak("Opening Visual Studio Code sir")
            vscode = r"C:\Users\devar\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(vscode)


        elif "your name" in text.lower():
            speaker.Speak("I am Jarvis, your personal assistant")

        elif "time" in text.lower():
            now = datetime.datetime.now()
            time = now.strftime("%I:%M %p")
            speaker.Speak(f"The time is {time}")

        elif "weather" in text.lower():
            speaker.Speak("Can you please tell me the city name sir?")
            city_name = listen()
            if city_name:
                getWeather(city_name)

        elif "browser" in text.lower():
            speaker.Speak("Opening browser sir")
            browser = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
            webbrowser.open(browser)

        elif "whatsapp" in text.lower():
            speaker.Speak("Opening WhatsApp sir")
            os.startfile(wa_path)

        elif "goodbye" in text.lower() or "exit" in text.lower() or "quit" in text.lower():
            speaker.Speak("Goodbye sir! Have a nice day")
            break

        elif "reset the chat" in text.lower():
            chatStr = ""
            speaker.Speak("Chat history reset successfully sir")

        elif "wikipedia" in text.lower():
            result = wikipedia.summary(text, sentences=2)
            print(result)
            speaker.Speak(result)

        else:
            response = get_ai_response(text)
            print(f"Jarvis: {response}")
            speaker.Speak(response)

    except Exception as e:
        print(f"An error occurred: {e}")
        speaker.Speak("I cannot process your request at the moment")
        continue