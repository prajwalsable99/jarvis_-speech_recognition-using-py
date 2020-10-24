import pyttsx3
from datetime import date as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
import pyjokes
from pyautogui import screenshot
from selenium import webdriver


#speaking
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# print(voices)

engine.setProperty('voice',voices[1].id)

# print(voices[1].id)

def talk(words):
    engine.say(words)
    engine.runAndWait()



#intro
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
      

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query 

def  intro():
    talk("hey this is dell g3 ,how can i help you")


if __name__=="__main__":
    intro()
    
    while True:
        query=takeCommand().lower()

        #1 wikipedia
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            talk('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            talk("According to Wikipedia")
            print(results)
            talk(results)

        #2 youtube
        if 'youtube' in query :
            talk("opening youtube")
            webbrowser.open("youtube.com")
        
        #3 music offline
        if 'play music' in query:
            folder = 'D:\\pyon_tut\\jarvis\\songs'
            songs = os.listdir(folder)
            print(songs)  
            num = random.randint(0, 2)
            os.startfile(os.path.join(folder, songs[num]))     

        #4 
        if 'joke' in query:
            talk("telling u joke a wait")
            joke=pyjokes.get_joke()
            talk(joke)
            print(joke)


        #5
        if "screenshot" in query:
            sc=screenshot()
            loc="screenshots/"
            dt_string = str(dt.today())+"_"+str(random.randint(1,1000))
            print("date and time =", dt_string)
            filename=loc+"img"+dt_string+".png"
            sc.save(filename)

        #6

        if "weather" in query:
            driver=webdriver.Chrome(executable_path="chromedriver_win32\chromedriver.exe")
            city="pune"
            try:
                driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
                weat=(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
                talk(weat)
                print(weat)
            except:
                print("Something went wrong")



        # end
        if 'thank you' in query :
            talk("Thank you,bye")
            break

    
  
    