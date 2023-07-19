import pyttsx3
import webbrowser
import smtplib
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import requests
from bs4 import BeautifulSoup
import pyjokes
from playsound import playsound

engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 3 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 16:
        speak('Good Afternoon!')

    if currentH >= 16 and currentH <17:
        speak('Good Evening!')


greetMe()

speak('Hello,I am uem Ai oAssistant welcome to university of engineering and management new town kolkata campus ')
speak('How can I help you')
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumarishan1116@gmail.com', '')
    server.sendmail('kumarishan1116@gmail.com', to, content)
    server.close()


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-IN')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))


    return query
      

if __name__ == '__main__': 

    while True:

    
        query = myCommand()
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        
        elif 'open google' in query:
            webbrowser.open("google.com") 
       
        elif 'alarm' in query:
            speak('Enter the time for which you want to set the alarm')
            time=input("Enter the time: ")

            while True:
                Time_Ac=datetime.datetime.now()
                now=Time_Ac.strftime("%H:%M:%S")

                if now==time:
                    music_dir = "C:\\Users\\hp\\Desktop\\uemAi\\music"
                    songs = os.listdir(music_dir)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif now>time:
                    break

        elif 'music' in query:
            music_dir = "C:\\Users\\hp\\Desktop\\uemAi\\music"
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")  
        
        elif 'hello' in query or 'hey' in query or 'hi' in query:
            speak("Hello")      
    
        elif 'library' in query:
            speak('It is in B2 ground floor')

        elif 'medical room' in query:
            speak('It is in B1 ground floor,beside cafeteria')         

        elif 'cafeteria' in query:
            speak('It is in B1 ground floor') 
        
        elif 'financial department' in query:
            speak('It is in B1 second floor') 
            
        elif 'xerox centre' in query:
            speak('It is in B1 second floor,beside dark room') 
        
        elif 'physics lab' in query:
            speak('It is in B1 second floor')       
        
        elif 'chemistry lab' in query:
            speak('It is in B1 second floor') 

        elif 'cheap store' in query:
            speak('It is in B1 third floor')

        elif 'registrar\'s office' in query:
            speak('It is in B3 ground floor')

        elif 'atm' in query:
            speak('It is in B1 ground floor')

        elif 'buddha auditorium' in query:
            speak('It is in B1 ground floor go straight from the main entrance')             
            
        elif 'electrical lab' in query:
            speak('It is in B1 third floor room no B1 LG 3.10 right side')

        elif 'electronics lab' in query:
            speak('It is in B1 third floor room no B1 LG 3.10 left side')

        elif 'computer lab' in query:
            speak('There are two computer labs one is in B2 fourth floor and the other is in B1 first floor')

        elif 'av hall' in query:
            speak('It is in B1 fourth floor') 

        elif 'skg' in query:
            speak('It is in B3 third floor staff room')

        elif 'dean\'s office' in query:
            speak('It is in B1 ground floor opposite cafeteria') 

        elif 'ficci auditorium' in query or 'where is B3 seminar hall' in query:
            speak('It is in B3 ground floor')  

        elif 'autocad lab' in query:
            speak('It is in B3 first floor room no B3 LG 1.5') 

        elif 'language lab' in query:
           speak('There are two language labs one is in B2 first floor room no B2 LG 1.3 and the other is in B1 first floor') 

        elif 'biotech lab' in query:
            speak('It is in B3 second floor') 

        elif 'sports room' in query:
            speak('It is in the basement') 

        elif 'office' in query:
            speak('It is in B1 ground floor beside the buddha auditorium')  

        elif 'innovation cell' in query:
            speak('It is in B1 third floor room number B1 LG 3.7')

        elif 'clothing department' in query:
            speak('It is in B1 first floor') 

        elif 'examination controllers room' in query:
            speak('It is in B1 second floor')  

        elif 'vc\'s room' in query:
            speak('It is in B2 ground floor in the left')

        elif 'mechanical workshop' in query:
            speak('It is in the basement and outside B3')

        elif 'proctors room' in query:
            speak('It is in B3 corridor')  

        elif 'board room' in query:
            speak('It is in B1 ground floor') 
        
        elif 'cultural' in query:
            speak('The cultural fest of Uem is called Ecstasia. It usually takes place in the month of March. ECSTASIA is a land of celebration of talents. It is a cultural fest where artists and players gather around to share their expertise with everyone. Ecstasia is filled with a lot of activities like games and sports, music, drama, dance, literacy events, fine arts, photography and even online competitions. Many colleges participate in our fest. There are exciting gifts. The last day is marked with dj night')

        elif 'information' in query:
            speak('UEM Kolkata is an engineering and management college that was established in the year 2014 by Act No 25 of 2014 of Govt of West Bengal. Being located in New Town, the Smart City of Eastern India and very near to the Netaji Subhash International Airport, the students of the University are exposed to the top corporates. UEM Kolkata has stood one out of the top 10 institutes of India including all IITs and all NITs of the country in the NPTEL program ranked by IIT Kharagpur and IIT Chennai. University of Engineering & Management (UEM) is a fully government approved and UGC recognised University. For more details visit on the link below:')
            print('https://uem.edu.in/uem-kolkata/')

        elif 'odd' in query:
            speak('It happens in the month of November to December every year for regular students and in January for backlogs')
            
        elif 'even' in query:
            speak('It happens in the month of April to May every year for regular students and in June for backlogs')

        elif 'website' in query:
            speak('The official website of UEM is www.iemcrp.com') 

        elif 'temperature' in query:
            search="temperature in kolkata"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")    

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "kumarishan1116@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email") 

        elif 'call' in query:
            from twilio.rest import Client

            account_sid='AC6d8f9d723391e179ab9488d9094ccdd4'
            auth_token='119c133ace918e00aaa97dff52182b94'

            client=Client(account_sid,auth_token)

            message=client.calls \
                .create(
                    twiml='<Response><Say>Hi I am your Assisstant.How can I help you</Say></Response>',
                    from_='+18316535830',
                    to='+917544895001'
                ) 

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            

        elif 'nothing' in query or 'abort' in query or 'stop' or 'bye' in query:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()    
        
        
        speak('Next Command!')