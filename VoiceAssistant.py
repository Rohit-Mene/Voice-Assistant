import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine= pyttsx3.init('sapi5') #sapi5->to take inbuiltvoive
voices=engine.getProperty('voices')
#print(voices)

engine.setProperty('voice',voices[1].id)
#print(voices[1].id) #tells whose voice we are using
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #wishes you according to time of the day
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour<=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("Hello! Rohit,How can i help you")

def takeCommand():# it  takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1 #seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)

    try:
        print("Recognizing")
        Query=r.recognize_google(audio, language='en-in')
        print("user said: "+Query)
    except Exception as e:
      #  print(e)
        print("Say that again please")
        return "None"
    return Query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("rohitmene@gmail.com","")
    server.sendmail("rohitmene@gmail.com",to,content)
    server.close()


if __name__=="__main__":


    wishMe()
    while True:

       Query = takeCommand().lower()
       if 'wikipedia' in Query:
           speak("Searching Wikipedia....")
           Query=Query.replace("wikipedia","")
           results=wikipedia.summary(Query,sentences=2)
           speak("According to wikipedia")
           speak(results)
       elif'open youtube' in Query: #using webbroweser module
           webbrowser.open("youtube.com")
       elif 'play music' in Query:
             music='C:\\Users\\lenovo\\Downloads\\Music'
             songs=os.listdir(music)
             print(songs)
             os.startfile(os.path.join(music,songs[random.randint(0,5)]))
       elif'the time' in Query:
           strtime=datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
           speak("Rohit the time is"+strtime)

       elif 'email to rohit' in Query:
           try:
               speak("What should I say")
               content=takeCommand()
               to='rohitmene@gmail.com'
               sendEmail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("Sorry e-mail couldn't be sent")
       elif 'who are you' in Query:
           speak('Huh! why do you care')


       elif 'stop' in Query:
           speak('succesfully exited')
           exit()



    tk.mainloop()
   # speak("ROHIT is awesome")