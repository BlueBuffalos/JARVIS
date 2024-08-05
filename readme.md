<font size="5">**JARVIS**</font>

<p>Jarvis is a personal desktop assistant for windows which works on voice commands to perform the tasks assigned to him.</p>

<font size="2">**Features**</font>
<ul>
    <li>Speech recognition</li>
    <li>Performs assigned tasks</li>
    <li>Integrated AI</li>
</ul>

<font size="2">**Want to use it?**</font>

1. Install pyaudio wheel in your system. Select according to your system. <a href="https://pypi.org/project/PyAudio/#files">Link</a>

2. Clone this repository on your system.
```
git clone https://github.com/devarsheecodess/JARVIS
```

3. Navigate to the local repository.
```
cd JARVIS
```

4. create a file config.py and add your <a href="https://huggingface.co/">Hugging Face</a> Token as shown below. Hugging face is a free alternative to Open AI.
```
HF_TOKEN = "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

5. You can also add your whatsApp desktop app path in config.py file as shown below.
```
wa_path = r"C:\Program Files\WindowsApps\xxxxxxxxxx"
```

5. Create a new file named commands.py and add songs or websites you frequently play or visit. Follow the same format including names of lists given below.
```
songs = [
    ["XXXX" , r"C:\Users\XXXX\Music\XXXX"],
    ["XXXX", r"C:\Users\XXXX\Music\Download\XXX"],
    ["XXXX", r"C:\Users\XXXX\Music\XXXX"],
    .
    .
    .
]

sites = [
    ["youtube", "https://www.youtube.com"], 
    ["spotify", "https://www.spotify.com"], 
    ["google", "https://www.google.com"], 
    .
    .
    .
]
```

6. Run the main.py file and you are good to go!

7. To stop Jarvis, say Goodbye!
