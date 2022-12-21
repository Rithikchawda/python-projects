import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
#import smtplib
import psutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio): # for speak command
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may i help you !")
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"        User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

def cpu():
    cpu = str(psutil.sensors_battery())
    speak (f'You have used {cpu} of battery.')
    battery = psutil.sensors_battery().percent
    speak(f'You have used{battery} of battery')


###def sendEmail(to, content)
  #  server = smtplib.SMTP('smtp.gmail.com', 587)
   # server.ehlo()
    #server.starttls()
    #server.login('sonnychawda@gmail.com', 'sonnyadichawda')
    #server.sendmail('sonnychawda@gmail.com', to, content)
    #server.close()


if __name__ == "__main__":
    speak("hey sir ")
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            n = random.randint(0,3)
            print(n)
            music_dir = 'C:\\Users\\HP\\OneDrive\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))

        #elif 'open code' in query
           # codePath =  
          #  os.startfile(codePath)

        #elif 'email to rithik' in query
            #try:
            #    speak("what should i say?")
             #   content = takecommand()
              #  to = "@gmail.com "
               # sendEmail(to, content)
                #speak("Email has been sent Sir!")
            #except Exception as e:
             #   print(e)
              #  speak("sorry my friend ved. I am not able to send this email.")
        elif 'battery' in query:
            cpu()
        elif 'quit' in query:
            exit()
                    
            
