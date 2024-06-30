import pyttsx3 # pip install pyttsx3
import speech_recognition as sr #pip install speech_recognition
import pyaudio # pip install pyaudio
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait() # without the ths command, speech will not be audible to us.


def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour > 0 and hour < 12:
      speak("Good Morning")
   elif hour > 12 and hour < 18:
      speak("Good Afternoon")
   else:
      speak("Good Evening")
   speak("Hello I am Zavis. Tell me how i could help you.")

def takeCommand():
   # '''it take microphone input from user and return string output'''
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 2
      audio = r.listen(source)

   try:
      print("Recognizing...")
      quary = r.recognize_google(audio, language='en-in') # using bing for voice recognition
      print(f"User said: {quary}\n") # Query will be printed
 
   except Exception as e:
      print(e)
      print("Say that Again please...") # say that agaun will be printed in case of improper voice
      return "None" # None string will be returned
   return quary

def sendEmail(to, content):
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login('sg608251@gmail.com','Sourav7749@gho')
   server.sendmail('sg608251@gmail.com', to, content)
   server.close()



if __name__ == "__main__":
   # speak("Sourav is a tallented guy.")
   wishMe()
   while True:
   # if 1:
      quary = takeCommand().lower()

      # Logic for executing task based on query
      if 'wikipedia' in quary:
         speak ('searching wikipedia....')
         quary = quary.replace("wikipedia", "")
         results = wikipedia.summary(quary, sentences=2)
         speak("According to wikipedia ")
         print(results)
         speak(results)
      elif 'open youtube' in quary:
         webbrowser.open("youtube.com")
      elif 'open google' in quary:
         webbrowser.open("google.com")
      elif 'open stackoverflow' in quary:
         webbrowser.open("stackoverflow.com")
      elif 'play music' in quary:
         music_dir = "C:\\Music"
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[2]))
      elif 'the time' in quary:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
      elif 'open code' in quary:
         code_dir = "C:\\Users\\sourav ghosh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(code_dir)
      elif 'email to soumya' in quary:
         try:
            speak("What should i do now")
            content = takeCommand()
            to = "gSoumya670@gmail.com"
            sendEmail(to, content)
            speak("email has been send successfully!")
         except Exception as e:
            print(e)
            speak("Email can't be send my friend. I am not able to send the email")
      elif 'open hacker rank' in query:
         webbrowser.open('www.hackerrank.com')
      elif 'exit' in quary:
         exit()