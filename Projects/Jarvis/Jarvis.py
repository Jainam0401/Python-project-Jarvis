
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:    
        speak("Good Afternoon!")

    elif hour>=18 and hour<24:    
        speak("Good Evening!")

    speak("I am Jarvis Sir. Plaese tell ``````` 1Qme how may I help you?")

def takecommand():
    #  it takes microphone input from the user and returns a string 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    sever = smtplib.SMTP("smtp.gmail.com",587)
    sever.ehlo()
    sever.starttls()
    sever.login("jainammithalaljain@gamil.com","9833785895")
    sever.sendmail('jainammithalaljain@gamil.com',to,content)
    sever.close() 



if __name__ == "__main__":
    # speak("Hello! I belong to India")
    wishme()
    while True:
        query = str(takecommand().lower())
    # logic for executing tasks based on query 
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Accordind to Wikipedia")
            print(results)
            speak(results)
            quit()

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
            
        elif "play music" in query:
            music_dir = 'D:'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}") 

        elif "quit" in query:
            speak("Thanks you so much for saving your Time ")
            quit()

        elif "open code" in query:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "jainammithalaljain@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry my friend Jainam I am failed to sent the mail. ")