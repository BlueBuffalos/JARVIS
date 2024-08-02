import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import openai
from config import apikey
from config import wa_path
speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak("Hello sir! I am Jarvis")

chatStr = ""



# Under Process 

# def chat(text):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Harry: {text}\nJarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     speaker.Speak(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]

# def AI(prompt):
#     try:
#         openai.api_key = apikey
#         text = f"OpenAI response for Prompt: {prompt}\n"
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0.7,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )

#         print(response["choices"][0]["text"])
#         text += response["choices"][0]["text"]
#         if not os.path.exists("OpenAI"):
#             os.mkdir("OpenAI")

#         with open(f"OpenAI/{prompt[0:30]}.txt", "w") as file:
#             file.write(text)
#     except:
#         print("An error occurred")



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:
    text = listen()
    sites = [
        ["youtube", "https://www.youtube.com"], 
        ["spotify", "https://www.spotify.com"], 
        ["google", "https://www.google.com"], 
        ["facebook", "https://www.facebook.com"], 
        ["twitter", "https://www.twitter.com"], 
        ["instagram", "https://www.instagram.com"], 
        ["linkedin", "https://www.linkedin.com"], 
        ["github", "https://www.github.com"], 
        ["stackoverflow", "https://www.stackoverflow.com"]
    ]

    for site in sites:
        if site[0] in text.lower():
            speaker.Speak(f"Opening {site[0]} sir")
            webbrowser.open(site[1])
            break;

    if "music" in text.lower():
        speaker.Speak("Opening Music sir")
        music = r"C:\Users\devar\Music\Musify\Download\Dil_Chori.mp3"
        os.startfile(music)

    elif "your name" in text.lower():
        speaker.Speak("I am Jarvis, your personal assistant")

    elif "the time" in text.lower():
        now = datetime.datetime.now()
        time = now.strftime("%I:%M %p")
        speaker.Speak(f"The time is {time}")

    elif "browser" in text.lower():
        speaker.Speak("Opening browser sir")
        browser = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
        webbrowser.open(browser)

    # elif "using ai" in text.lower():
    #     AI(prompt=text)

    elif "WhatsApp" in text:
        speaker.Speak("Opening WhatsApp sir")
        os.startfile(wa_path)

    elif "exit" in text.lower():
        speaker.Speak("Goodbye sir")
        break;
    
    elif "reset" in text.lower():
        chatStr = ""
        speaker.Speak("Chat history resetted sucessfully sir")

    else:
        # print("Chatting...")
        # chat(text)
        print("Pardon sir")