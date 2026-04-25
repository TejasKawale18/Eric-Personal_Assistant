print("Initializing The Program...")
import os
import sys
import random
import pyttsx3
import smtplib
import datetime
import requests
import geocoder
import pywhatkit
import wikipedia
import webbrowser
import speech_recognition as sr
print("Wait Few Seconds...")
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Eric_GUI import Ui_MainWindow
from keyboard import press_and_release,write
from pyautogui import *
from os import startfile
from bs4 import BeautifulSoup as BS
from Features import *
from Bot import ChatBot
from DataBase.Config import *
from datetime import datetime
from googletrans import Translator
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty("rate",200)

def Speak(audio):
    ui.Print_T(" ")
    ui.Updated_GUI("Visualizing")
    ui.Print_T(f"Eric : {audio}")
    engine.say(audio)
    engine.runAndWait()
    ui.Print_T(" ")

class MainThread(QThread):
    
    def __init__(self): 
        super(MainThread,self).__init__()
        print("Starting...")

    def run(self):
        self.Exe()

    def TakeCommand(self, Hold = 6):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.Print_T(": Listening...")
            ui.Updated_GUI("Listening")
            r.adjust_for_ambient_noise(source,duration = 0.5)
            # r.pause_threshold = 1
            audio = r.listen(source,0,Hold)
        try:
            ui.Print_T(": Recognizing...")
            ui.Updated_GUI("Recognizing")
            query = r.recognize_google(audio,language='hi')
        except:
            return self.TakeCommand()
        query = str(query)
        query = query.lower()
        Translation = Translator()
        Result = Translation.translate(query)
        query = Result.text
        ui.Print_T(f": You : {query.title()}")
        return query.lower()
    
    def StartUpCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.Updated_GUI("Sleeping")
            print("Listening...")
            r.adjust_for_ambient_noise(source,duration = 0.5)
            # r.pause_threshold = 1
            audio = r.listen(source,0,4)
        try:
            print("Recognizing...")
            ui.Updated_GUI("Sleeping")
            query = r.recognize_google(audio,language='hi')
        except:
            return self.StartUpCommand()
        query = str(query)
        query = query.lower()
        Translation = Translator()
        Result = Translation.translate(query)
        query = Result.text
        print(f": You : {query.title()}")
        return query.lower()

    def SendingEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('personal.assistant.eric@gmail.com', 'rkorygmdkslqmfhv')
        server.sendmail('personal.assistant.eric@gmail.com', to, content)
        server.close()
    
    def Exe(self):
        MailData = {'self':'personal.assistant.eric@gmail.com',
        'lokesh':'sutarlokesh82@gmail.com',
        'prasad':'zadeprasad246@gmail.com',
        'tejas':'tejaskawale18@gmail.com',
        'Manish':'manisht8454@gmail.com',
        'Vedant':'vedantshigwan11@gmail.com'}
        ui.Print_T("Sleeping...")
        while True:
            query = self.StartUpCommand()
            if "wake up" in query or "activate" in query or "ready" in query or "hey" in query or "hi" in query or "hello" in query or "online" in query or "get up" in query or "eric" in query or "are you there" in query:
                Reply = ("Hey, Nice To Meet You Again.","Hello Sir","Hey, How Are You ?","Hello Sir, Nice To Meet You Again.")
                Speak(random.choice(Reply))
                while True:
                    query = self.TakeCommand()
                    if query == "":
                        continue
                    query = query.replace("eric","")
                    query = query.replace("please","")
                    query = query.replace("well","")
                    query = query.strip()
                    if 'home screen' in query: press_and_release('windows + m')
                    elif 'minimize' in query or 'minimise' in query: press_and_release('windows + m')
                    elif 'show start' in query or 'show the start' in query: press('super')
                    elif 'open setting' in query: press_and_release('windows + i')
                    elif 'open search' in query: press_and_release('windows + s')
                    elif 'show me the screen' in query or 'display the screen' in query or 'last screen' in query:
                        try:
                            os.startfile(path_2)
                            Speak("Here it is sir")
                        except:
                            os.startfile("DataBase\\Screenshots")
                    elif 'screen shot' in query or 'screenshot' in query or "capture the screen" in query:
                        Speak("Alright Sir, Taking The Screenshot")
                        Img = screenshot()
                        Speak("By What Name Do You Want To Save This Screenshot?")
                        Name = self.TakeCommand()
                        Name = f"{Name}.png"
                        Img.save(Name)
                        path_1 = Name
                        path_2 = "DataBase\\Screenshots\\" + str(Name)
                        os.rename(path_1,path_2)
                        Speak("The Screenshot Has Been Captured Successfully")
                    elif (('increase' in query and 'volume' in query) or ('volume' in query and 'up' in query)): press("volumeup")
                    elif (('decrease' in query and 'volume' in query) or ('decree' in query and 'vol' in query) or ('volume' in query and 'down' in query)): press("volumedown")
                    elif (('unmute' in query and 'volume' in query) or ('volume unmute' in query or 'volumeupmute' in query)): press("volumemute")
                    elif (('mute' in query and 'volume' in query) or ('volume mute' in query or 'volumemute' in query)): press("volumemute")
                    elif (('close' in query and ('window' in query or 'app' in query)) or ('close it' in query)): press_and_release('alt + f4')
                    elif 'restore window' in  query or 'restore the window' in query: press_and_release('Windows + Shift + m')
                    elif 'switch the window' in query or 'switch window' in query:
                        Speak("Okay sir, Switching the window")
                        keyDown("alt")
                        press("tab")
                        sleep(1)
                        keyUp("alt")
                    elif 'type' == query or 'write' == query or "right" == query:
                        Speak("To Stop Writing, Please Speak Stop Or Exit")
                        Speak("Please Tell Me What Should I Write...")
                        while True:
                            Content = self.TakeCommand()
                            Content = Content.strip()
                            if (("stop" == Content) or ("exit" == Content)):
                                Speak("Typing is Stopped !")
                                break
                            elif 'save this file' == Content:
                                hotkey('ctrl','s')
                                press('enter')
                                Speak("Done, Sir !")
                                break
                            else:
                                write(Content)
                    elif 'enter' in query and 'press' in query: press('enter')
                    elif 'new tab' in query: press_and_release('ctrl + t')
                    elif 'close' in query and 'tab' in query: press_and_release('ctrl + w')
                    elif 'new window' in query: press_and_release('ctrl + n')
                    elif 'history' in query and 'show' in query: press_and_release('ctrl + h')
                    elif 'open downloads' == query: press_and_release('ctrl + j')
                    elif 'bookmark' in query: 
                        press_and_release('ctrl + d')
                        press('enter')
                    elif 'incognito' in query: press_and_release('Ctrl + Shift + n')
                    elif 'switch tab' in query: press_and_release('ctrl + tab')
                    elif 'pause' in query: press('space bar')
                    elif 'resume' in query: press('space bar')
                    elif 'full screen' in query or 'fullscreen' in query: press('f')
                    elif 'film screen' in query or 'filmscreen' in query: press('t')
                    elif 'skip' in query: press('l')
                    elif 'back' in query or 'rewind' in query: press('j')
                    elif 'increase' in query and 'speed' in query: press_and_release('SHIFT + .')
                    elif 'decrease' in query and 'speed' in query: press_and_release('SHIFT + ,')
                    elif 'previous' in query: press_and_release('SHIFT + p')
                    elif 'next' in query: press_and_release('SHIFT + n')
                    elif 'search' == query:
                        click(x=884, y=100)
                        Speak("What To Search Sir ?")
                        search = self.TakeCommand()
                        write(search)
                        sleep(1)
                        press('enter')
                    elif 'close' in query or 'dismiss' in query or 'exit' in query: 
                        try:
                            if "chrome" in query:
                                query = "chrome"
                            elif "edge" in query:
                                query = "msedge"
                            elif "youtube" in query:
                                query = "chrome"
                            elif "google" in query:
                                query = "chrome"
                            elif "setting" in query:
                                query = "systemsettings"
                            query = query.replace("close ","")
                            query = query.replace("exit ","")
                            query = query.replace("form ","")
                            query = query.replace("the ","")
                            query = query.replace("okay ","")
                            query = query.replace("ok ","")
                            query = query.replace("let's ","")
                            query = query.replace("lets ","")
                            query = query.replace("end ","")
                            query = query.replace("dismiss ","")
                            if os.system(f"TASKKILL /F /im {query}.exe")==0:
                                Speak(f"Closing {query}")
                            else:
                                Speak("Sorry, I am Unable To Find This Application")    
                        except:
                            Speak("Sorry, I am Unable To Find This Application")
                    elif 'who are you' in query or 'what is your name' in query or "what's your name" in query:
                        Reply = ("I am Eric","I am Eric, How Can I Assist You ?","My Name Is Eric","My Name Is Eric, And I am Your Personal Assistant")
                        Speak(random.choice(Reply))
                    elif 'mail in data' in query or 'mail in our data' in query or 'add mail' in query or 'add email' in query:
                        Speak("Please Write The Name Of That Person Which You Want To Add")
                        Name = input("Write The Name And Press Enter: ")
                        Speak(f"Please Write The Email ID Of {Name}")
                        ID = input(f"Write The Email Of {Name} And Press Enter: ")
                        try:
                            MailData.update({Name:ID})
                            Speak("Updating Database...")
                            Speak("Database Is Updated Successfully")
                        except:
                            Speak("Sorry Sir, Something Happends Wrong. Please Try Again Later...")
                    elif 'mail' in query:
                            query = query.replace("email", "")
                            query = query.replace("mail", "")
                            query = query.replace("send ", "")
                            query = query.replace("an", "")
                            query = query.replace("to", "")
                            query = query.replace("can", "")
                            query = query.replace("you", "")
                            query = query.replace("please", "")
                            query = query.replace("hey","")
                            query = query.replace("bro","")
                            query = query.replace("eric","")
                            query = query.strip()
                            to = query
                            if to in MailData:
                                for Name,Id in MailData.items():
                                    if Name == to:
                                        to = Id
                            elif to == "":
                                Speak("Please Try Speaking Name With Command...")
                                to = input("Enter The Email Id:- ")
                            else:
                                Speak(f"{to} is Not Found In Our DataBase, Please Enter The Mail Id Of {to} Manually...")
                                to = input("Enter The Email Id:- ")
                            try:
                                Speak('What Should I Write In This Email ?')
                                content = self.TakeCommand(Hold = 20)
                                while True:
                                    Speak(f"Confirm Your Content, {content}")
                                    confirmation = self.TakeCommand(Hold = 3)
                                    if 'yes' in confirmation or 'yep' in confirmation or 'okay' in confirmation or 'ok' in confirmation:
                                        Speak (f"Sending Email to {query}")
                                        self.SendingEmail(to, content)
                                        Speak("Email has been sent!")
                                        break
                                    elif 'no' in confirmation or 'nope' in confirmation:
                                        Speak('What Should I Write In Updated Mail ?')
                                        content = self.TakeCommand(Hold = 20)
                                    elif 'cancel' in confirmation:
                                        Speak("This Email Has Been Canceled!")
                                        break 
                            except Exception as e:
                                ui.Print_T(e)
                                Speak("Sorry. I Am Not Able To Send This Email Right Now")
                    elif (('google' in query) and ('map' not in query)):
                        query = query.replace("please","")
                        query = query.replace("from ","")
                        query = query.replace("okay ","")
                        query = query.replace("ok ","")
                        query = query.replace("of ","")
                        query = query.strip()
                        if 'and' in query or 'search' in query or 'find' in query or 'on ' in query:
                            query = query.replace("search","")
                            query = query.replace(" on","")
                            query = query.replace("google","")
                            query = query.replace("find","")
                            query = query.replace("and","")
                            query = query.replace("open","")
                            query = query.strip()
                            try:
                                if query != "":
                                    Speak("This Is What I Found On Google!")
                                    webbrowser.open(f"https://www.google.com/search?q={query}")
                                    try:
                                        results = wikipedia.summary(query, sentences=3)
                                        Speak(results)
                                    except:
                                        Speak(f"Sorry, I Cannot Tell Anything About {query}")
                                elif query == "":
                                    Speak("What Should I Search On Google...")
                                    query = self.TakeCommand()
                                    Speak("This Is What I Found For Your Search.")
                                    webbrowser.open(f"https://www.google.com/search?q={query}")
                                    try:
                                        results = wikipedia.summary(query, sentences=3)
                                        Speak(results)
                                    except:
                                        Speak(f"Sorry, I Cannot Tell Anything About {query}")
                                else:
                                    webbrowser.open('https://www.google.com')
                            except:
                                Speak("Sorry, But This Is Not Possible Right Now.")
                        elif 'open' in query:
                            webbrowser.open('https://www.google.com')
                    elif 'chrome' in query and ('open' in query or 'start' in query): startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    elif 'whatsapp' in query and ('open' in query or 'start' in query): startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2323.2.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                    elif 'notepad' in query and ('open' in query or 'start' in query): startfile("C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2304.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe")
                    elif (('search' in query or 'where' in query or 'locate' in query or 'google map' in query or 'google maps' in query or 'googlemap' in query or 'googlemaps' in query or 'map' in query or 'maps' in query) and ('youtube' not in query and 'wikipedia' not in query)):
                        try:
                            Place = query.replace("googlemaps ","")
                            Place = Place.replace("googlemap ","")
                            Place = Place.replace("google ","")
                            Place = Place.replace("search ","")
                            Place = Place.replace("maps","")
                            Place = Place.replace("map","")
                            Place = Place.replace("where ","")
                            Place = Place.replace("for ","")
                            Place = Place.replace("the ","")
                            Place = Place.replace("is ","")
                            Place = Place.replace("on ","")
                            Place = Place.replace("in ","")
                            Place = Place.strip()
                            Url_Place = "https://www.google.com/maps/place/" + str(Place)
                            geolocator = Nominatim(user_agent="myGeocoder")
                            location = geolocator.geocode(Place , addressdetails= True)
                            target_latlon = location.latitude , location.longitude
                            location = location.raw['address']
                            target = {'city' : location.get('city',''),
                                        'state' : location.get('state',''),
                                        'country' : location.get('country','')}
                            current_loca = geocoder.ip('me')
                            current_latlon = current_loca.latlng
                            webbrowser.open(url=Url_Place)
                            distance = str(great_circle(current_latlon,target_latlon))
                            distance = str(distance.split(' ',1)[0])
                            distance = round(float(distance),2)
                            Speak(target)
                            Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")
                        except:
                            Speak("Sorry, But This Is Not Possible Right Now.")
                    elif 'youtube' in query or 'play' in query or 'start' in query or 'how to' in query:
                        query = query.replace("please","")
                        query = query.replace("from ","")
                        query = query.replace("okay ","")
                        query = query.replace("ok ","")
                        query = query.replace("of ","")
                        query = query.replace("on ","")
                        query = query.replace("youtube","")
                        if 'and' in query or 'search' in query or 'find' in query or 'play' in query  or 'how to' in query:
                            query = query.replace("search","")
                            query = query.replace("find","")
                            query = query.replace("and","")
                            query = query.replace("from","")
                            query = query.replace("open","")
                            query = query.replace("please","")
                            query = query.strip()
                            try:
                                if 'play' not in query:
                                    Speak("This Is What I Found On Youtube For Your Search!")
                                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                                if 'play' in query:
                                    query = query.replace("play ","")
                                    Speak(f"Playing {query} From YouTube...")
                                    pywhatkit.playonyt(query)
                                # elif query != "":
                                #     pywhatkit.playonyt(query)
                                #     Speak('This Might Be Help You...')
                                else:
                                    webbrowser.open("https://www.youtube.com/")
                            except:
                                Speak("Sorry, But This Is Not Possible Right Now.")
                        elif 'open' in query:
                            webbrowser.open("https://www.youtube.com/")
                    elif 'open' in query or 'start' in query:
                        query = query.replace("open","")
                        query = query.replace("the","")
                        query = query.replace("start","")
                        press("super")
                        sleep(0.4)
                        typewrite(query)
                        press("enter")
                    elif 'remember' in query and 'what' in query:
                        with open("Database\\Remember List.txt","r") as File:
                            Content = File.read()
                        Speak(f"You Told Me To Remember Following Sentences\n\n{Content[:-1]}")
                    elif 'remember' in query and ('clear' in query or 'erase' in query):
                        open("DataBase\\Remember List.txt","w")
                        Speak("Remember List Is Successfully Cleared...")
                    elif 'remember' in query:
                        query = query.replace("remember that","")
                        query = query.replace("remember this","")
                        query = query.replace("remember","")
                        query = query.strip()
                        with open("DataBase\\Remember List.txt","a") as R_List:
                            R_List.write(f"{query}\n")
                        Speak(f"I Will Remember This, {query}")
                    elif 'wikipedia' in query:
                        Speak('Searching On Wikipedia...')
                        query = query.replace("on wikipedia", "")
                        query = query.replace("wikipedia", "")
                        query = query.replace("search", "")
                        query = query.replace("search on wikipedia", "")
                        try:
                            results = wikipedia.summary(query, sentences=4)
                            Speak("According to Wikipedia")
                            Speak(results)
                        except:
                            Speak(f"Sorry, {query} Does Not Found In Any Pages")
                    elif 'download' in query and "video" in query:
                        from pytube import YouTube
                        from pyautogui import hotkey
                        import pyperclip
                        sleep(2)
                        click(x=1000,y=52)
                        hotkey('ctrl','c')
                        value = pyperclip.paste()
                        Link = str(value)
                        url = YouTube(Link)
                        video = url.streams.first()
                        video.download('DataBase\\YouTube Downloads\\')
                        Speak("Done Sir , I Have Downloaded The Video .")
                        Speak("Here Is Your All Downloaded Videos.")
                        os.startfile('DataBase\\YouTube Downloads\\')
                    elif 'speed test' in query or 'speed' in query or 'test' in query or 'speedtest' in query:
                        Speak("I Am Checking The Internet Speed Sir, Wait For A While...")
                        import speedtest
                        speed = speedtest.Speedtest()
                        Upload = int(int(speed.upload())/1024/1024)
                        Download = int(int(speed.download())/1024/1024)
                        Speak(f"Downloading Speed Is {Download} M.B. Per Seconds.")
                        Speak(f"Uploading Speed Is {Upload}  M.B. Per Seconds.")
                    elif (('chat' in query or 'conversation' in query) and ('show' in query or 'display' in query)): 
                        os.startfile("Chat.txt")
                        Speak("Here It Is Sir...")
                    elif 'clear the chat' in query or 'clear chat' in query or 'clear the convesation' in query or 'clear conversation' in query or 'erase' in query or 'reset' in query:
                        with open("Chat.txt", "w") as Chat:
                            Chat.write("")
                            Speak("Reseting Conversation")
                            Speak("Conversation Reset Successfully")
                    elif (('play' in query or 'start' in query) and ('folder' in query or 'offline' in query)):
                        try:
                            PlaySong()
                            Speak("Playing Songs From Your Songs Folder..")
                        except:
                            Speak("Sorry But This Is Not Possible Right Now...")
                    elif 'message' in query:
                        name = Filter_WhatsApp(query)
                        if name == "":
                            Speak("To Whom, You Want To Message...")
                            name = self.TakeCommand()
                            name = name.replace("for ","")
                            name = name.replace("to ","")
                            name = name.strip()
                        Speak(f"What Is The Message For {name}")
                        MSG = self.TakeCommand()
                        startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2323.2.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(3)
                        click(x=383, y=120)
                        sleep(1)
                        click(x=383, y=120)
                        sleep(1)
                        write(name)
                        sleep(1)
                        click(x=310, y=186)
                        sleep(0.5)
                        click(x=706, y=696)
                        sleep(0.5)
                        write(MSG)
                        press('enter')
                    elif 'video call' in query or 'videocall' in query:
                        name = Filter_WhatsApp(query)
                        if name == "":
                            Speak("To Whom, You Want To Make Video Call")
                            name = self.TakeCommand()
                            name = name.replace("to ","")
                            name = name.replace("for ","")
                            name = name.strip()
                        startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2323.2.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(3)
                        click(x=383, y=120)
                        sleep(1)
                        click(x=383, y=120)
                        sleep(1)
                        write(name)
                        sleep(1)
                        click(x=310, y=186)
                        sleep(1)
                        click(x=1200, y=73)
                    elif 'call' in query:
                        name = Filter_WhatsApp(query)
                        if name == "":
                            Speak("To Whom, You Want To Call")
                            name = self.TakeCommand()
                            name = name.replace("to ","")
                            name = name.replace("for ","")
                            name = name.strip()
                        startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2323.2.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(3)
                        click(x=383, y=120)
                        sleep(1)
                        click(x=383, y=120)
                        sleep(1)
                        write(name)
                        sleep(1)
                        click(x=310, y=186)
                        sleep(1)
                        click(x=1253, y=72)
                    elif 'chat' in query:
                        name = Filter_WhatsApp(query)
                        if name == "":
                            Speak("To Whom, You Want To Chat")
                            name = self.TakeCommand()
                            name = name.replace("to ","")
                            name = name.replace("for ","")
                            name = name.strip()
                        startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2323.2.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(3)
                        click(x=383, y=120)
                        sleep(1)
                        click(x=383, y=120)
                        sleep(1)
                        write(name)
                        sleep(1)
                        click(x=310, y=186)
                        sleep(0.5)
                        click(x=706, y=696)
                        sleep(0.5)
                    elif 'weather' in query:
                        Speak("Checking Wheather Sir, Please Wait...")
                        City = Filter_Weather(query)
                        if City == "":
                            City = "pune"
                        api_key = Weather
                        base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
                        units_format = "&units=metric"
                        complete_url = base_url + City + "&appid=" + api_key + units_format
                        try:
                            data = requests.get(complete_url).json()
                            if data['cod'] == '404':
                                Speak('City Is Not Fount In Our Database...')
                            else:
                                weather_desc = data['weather'][0]['description']
                                temp = data['main']['feels_like']
                                humidity = data['main']['humidity']
                                pressure = data['main']['pressure']
                                speed = data['wind']['speed']
                                report = f"""
                                The Weather In {City} Is Currently {weather_desc}.
                                The Temperature Is Feels Like {temp:.1f} degrees Celsius.
                                The humidity is {humidity}%.
                                Atmospheric Pressure Is {pressure} Hectopascals.
                                And The Wind Speed Is About {speed} Kilometes Per Hour"""
                                Speak(report)
                        except:
                            Speak('An Error Occurred While Fetching The Weather Data...\nI am Sorry For That...')
                    elif 'temperature' in query or 'temp' in query:
                        City = Filter_Weather(query)
                        Speak(f"Checking Current Temperature In {City}")
                        if City == "":
                            City = "pune"
                        search = f"temperature in {City}"
                        url = f"https://www.google.com/search?q={search}"
                        try:
                            r = requests.get(url)
                            Data = BS(r.text,"html.parser")
                            Temperature = Data.find("div", class_= "BNeawe").text
                            Speak(f"Current {search.title()} Is {Temperature}")
                        except:
                            Speak("An Error Occurred While Fetching The Temperature...\nI am Sorry For That...")
                    elif 'calculate' in query:
                        Speak("Calculating...")
                        query = query.replace("calculate","")
                        query = query.replace("plus","+")
                        query = query.replace("into","*")
                        query = query.replace("multiply","*")
                        query = query.replace("times","*")
                        query = query.replace("divide by","/")
                        query = query.replace("divide","/")
                        query = query.replace("by","/")
                        query = query.replace("pie","pi")
                        Speak(WolframAlpha(query))
                    elif 'copy me' in query:
                        Speak("The Game Is Begin")
                        while True:
                            query = self.TakeCommand()
                            if "stop" in query:
                                Speak("Okay Sir, This Game Is Over Now...")
                                break
                            Speak(query)
                    elif 'the time' in query:
                        strTime = datetime.now().strftime("%H:%M")
                        Speak(f"Sir, the time is {strTime}")
                    elif 'my location' in query:
                        Location = "https://www.google.com/maps/place/Narhe,+Pune,+Maharashtra/@18.448879,73.8046413,14z/data=!3m1!4b1!4m6!3m5!1s0x3bc2953f2263c307:0x79aeb881437adebd!8m2!3d18.4464732!4d73.826375!16s%2Fg%2F1tfxf3v9?entry=ttu"
                        Speak("Checking Your Location...")
                        ip_add = requests.get('https://api.ipify.org').text
                        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
                        webbrowser.open(Location)
                        geo_q = requests.get(url)
                        geo_d = geo_q.json()
                        Location = "Narhe"
                        city = 'Pune'
                        # city = geo_d["city"]
                        state = geo_d["region"]
                        country = geo_d['country']
                        Speak(f"Sir, You Are Currently In {Location}, Which Is In {city} City, {state} State, Country {country}.")
                        Speak("I Provided Your Precise Location In Google Maps")
                    elif 'ip' in query: Speak(My_IP())
                    elif query.startswith('say '): Speak(query[4:])
                    elif 'note' in query or 'write a note' in query:
                        Speak("Tell Me The Query .")
                        Speak("I Am Ready To Write .")
                        writes = self.TakeCommand()
                        time = datetime.now().strftime("%H:%M")
                        filename = str(time).replace(":","-") + "-note.txt"
                        with open(filename,"w") as file:
                            file.write(writes)
                        path_1 = str(filename)
                        path_2 = "DataBase\\NotePad\\" + str(filename)
                        os.rename(path_1,path_2)
                        os.startfile(path_2)
                        Speak(f"The File Is Successfully Saved In Our Database, By The Name {filename}")
                    elif 'cases' in query or 'covid' in query:
                        Speak("Sir, Which Country's Information Do You Want ?")
                        Country = self.TakeCommand()
                        Country = Country.replace("of ","")
                        Country = Country.replace("for ","")
                        try:
                            url = "https://www.worldometers.info/coronavirus/country/" + Country + "/"
                            data = requests.get(url)
                            soup = BS(data.text,'html.parser')
                            Corona = soup.find_all("div",class_="maincounter-number")
                            Data = []
                            for Case in Corona:
                                Span = Case.find('span')
                                Data.append(Span.string)
                            Cases, Deaths, Recovered = Data
                            Speak(f"Total Cases Are : {Cases}")
                            Speak(f"Total Deaths Are : {Deaths}")
                            Speak(f"Total Recovered : {Recovered}")
                        except:
                            Speak("An Error Occurred While Fetching The Information...\nI am Sorry For That...")
                    elif "terminate" in query:
                        Speak("Terminating The Program")
                        sys.exit()
                    else:
                        Speak(ChatBot(query))
                        if (("restore" not in query) and ("bye" in query or "exit" in query or "sleep" in query or "go " in query or "by" in query or "relax" in query or "rest" in query or "goodbye" in query)):
                            ui.Print_T("Sleeping...")
                            break

StartExecution = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):
        super(Gui_Start, self).__init__()
        self.Eric_ui = Ui_MainWindow()
        self.Eric_ui.setupUi(self)
        self.Eric_ui.Start_Button.clicked.connect(self.StartFunc)
        self.Eric_ui.Exit_Button.clicked.connect(self.close)

    def StartFunc(self):
        # self.Eric_ui.Start_Button.clicked.connect(self.Nothing)

        self.Eric_ui.Visualizing_Main = QMovie("DataBase/Gui Materials/Visualizing.gif")
        self.Eric_ui.Visualizing.setMovie(self.Eric_ui.Visualizing_Main)
        self.Eric_ui.Visualizing_Main.start()

        self.Eric_ui.Recognize_Main = QMovie("DataBase/Gui Materials/Recognizing.gif")
        self.Eric_ui.Recognize.setMovie(self.Eric_ui.Recognize_Main)
        self.Eric_ui.Recognize_Main.start()
        
        self.Eric_ui.Sleeping_Main = QMovie("DataBase/Gui Materials/Sleeping.gif")
        self.Eric_ui.Sleeping.setMovie(self.Eric_ui.Sleeping_Main)
        self.Eric_ui.Sleeping_Main.start()
        
        self.Eric_ui.Listening_Main = QMovie("DataBase/Gui Materials/Listening.gif")
        self.Eric_ui.Listening.setMovie(self.Eric_ui.Listening_Main)
        self.Eric_ui.Listening_Main.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        StartExecution.start()

    def Updated_GUI(self, State):
        if State == "Listening":
            self.Eric_ui.Recognize.hide()
            self.Eric_ui.Sleeping.hide()
            self.Eric_ui.Listening.raise_()
            self.Eric_ui.Visualizing.raise_()
            self.Eric_ui.Listening.show()
            self.Eric_ui.Visualizing.show()
        elif State == "Recognizing":
            self.Eric_ui.Sleeping.hide()
            self.Eric_ui.Visualizing.hide()
            self.Eric_ui.Listening.hide()
            self.Eric_ui.Recognize.raise_()
            self.Eric_ui.Recognize.show()
        elif State == "Sleeping":
            self.Eric_ui.Recognize.hide()
            self.Eric_ui.Visualizing.hide()
            self.Eric_ui.Listening.hide()
            self.Eric_ui.Sleeping.raise_()
            self.Eric_ui.Sleeping.show()
        elif State == "Visualizing":
            self.Eric_ui.Recognize.hide()
            self.Eric_ui.Listening.hide()
            self.Eric_ui.Sleeping.hide()
            self.Eric_ui.Visualizing.raise_()
            self.Eric_ui.Visualizing.show()
        self.Eric_ui.Interface.raise_()
        self.Eric_ui.Remove.raise_()
        self.Eric_ui.Remove_2.raise_()
        self.Eric_ui.Remove_3.raise_()
        self.Eric_ui.Remove_4.raise_()
        self.Eric_ui.Remove_5.raise_()
        self.Eric_ui.Clock.raise_()
        self.Eric_ui.Date.raise_()
        self.Eric_ui.Day.raise_()
        self.Eric_ui.Time.raise_()
        self.Eric_ui.Terminal.raise_()
        self.Eric_ui.Terminal_Output.raise_()
        self.Eric_ui.Start.raise_()
        self.Eric_ui.Exit.raise_()
        self.Eric_ui.Cut.raise_()
        self.Eric_ui.Cut_2.raise_()
        self.Eric_ui.Cut_3.raise_()
        self.Eric_ui.Cut_4.raise_()
        self.Eric_ui.Cut_5.raise_()
        self.Eric_ui.Cut_6.raise_()
        self.Eric_ui.Start_Button.raise_()
        self.Eric_ui.Exit_Button.raise_()

    def Print_T(self, Text):
        self.Eric_ui.Terminal_Output.appendPlainText(Text)

    def showtime(self):
        Current_Time = QTime.currentTime()
        Current_Date = QDate.currentDate()
        Label_Time = Current_Time.toString("hh:mm:ss")
        Label_Date = Current_Date.toString(Qt.ISODate)
        self.Eric_ui.Time.setText(f"   • {Label_Time}")
        self.Eric_ui.Day.setText("• Tuesday")
        self.Eric_ui.Date.setText(f" • 18-07-2023")

if __name__ == "__main__":
    Gui_App = QApplication(sys.argv)
    ui = Gui_Start()
    ui.show()
    exit(Gui_App.exec_())
