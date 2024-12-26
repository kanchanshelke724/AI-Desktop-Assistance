import pyttsx3 #text-to-speech conversion. It allows you to convert text into spoken words 
import os #way to interact with the operating system. It can be used for tasks such as file manipulation, 
                                                         #directory operations, and executing system commands.
import wikipedia
import webbrowser
import speech_recognition as sr
import datetime
import pywhatkit #Google searches 
import pyautogui  #programmatically control the mouse and keyboard & perform other tasks related to graphical user interface automation.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am AI, please tell me how I may help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    current_song_index = 0
    songs = []
    music_dir = "E:\songs"
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Sure, what would you like to search on YouTube?")
            search_query = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

        elif 'go back' in query.lower():
            pyautogui.press('back')  # Simulate pressing the "Back" key

        elif 'close tab' in query.lower():
            pyautogui.hotkey('ctrl', 'w')  # Simulate pressing Ctrl+W to close the tab

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play song' in query:
           speak("Sure, what song would you like to play?")
           song_query = takeCommand().lower()
           webbrowser.open(f"https://www.youtube.com/results?search_query={song_query}")


        elif 'hey google' in query:
            speak("Sure, what would you like to search on Google?")
            search_query = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'play music' in query:
            speak("Sure, what song would you like to play?")
            song_query = takeCommand().lower()
            pywhatkit.playonyt(song_query)  # Search and play the song on YouTube

        elif 'play next song' in query:
            current_song_index += 1
            current_song_index %= len(songs)
            os.startfile(os.path.join(music_dir, songs[current_song_index]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'cooking' in query:
            speak("Sure, what would you like to cook?")
            recipe_query = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={recipe_query} recipe")

        elif 'education' in query:
            speak("Sure, what would you like to learn?")
            topic_query = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={topic_query} education")

        elif 'stop' in query:
            speak("Bye!See u again")
            break  
