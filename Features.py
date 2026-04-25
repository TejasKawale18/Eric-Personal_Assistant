import os
from bs4 import BeautifulSoup as BS
import wolframalpha
from DataBase.Config import *

def Filter_WhatsApp(query):
    query = query.replace("whatsapp","")
    query = query.replace("what's up","")
    query = query.replace("message","")
    query = query.replace("from ","")
    query = query.replace("with ","")
    query = query.replace("on ","")
    query = query.replace("a ","")
    query = query.replace("send","")
    query = query.replace("write","")
    query = query.replace("type","")
    query = query.replace("to ","")
    query = query.replace("for ","")
    query = query.replace("call","")
    query = query.replace("the ","")
    query = query.replace("speaker","")
    query = query.replace("make ","")
    query = query.replace("show ","")
    query = query.replace("chat","")
    query = query.replace("of ","")
    query = query.replace("video","")
    query = query.replace("videocall ","")
    query = query.replace("help","")
    query = query.replace("hey ","")
    query = query.replace("hello ","")
    query = query.replace("hii ","")
    query = query.replace("hi ","")
    query = query.replace("eric","")
    query = query.strip()
    return query

def Filter_Weather(query):
    query = query.replace("tell","")
    query = query.replace("right","")
    query = query.replace("now","")
    query = query.replace("me ","")
    query = query.replace("weather","")
    query = query.replace("the ","")
    query = query.replace("of ","")
    query = query.replace("what ","")
    query = query.replace("is ","")
    query = query.replace("get ","")
    query = query.replace("current ","")
    query = query.replace("temperature","")
    query = query.replace("in ","")
    query = query.replace("hey ","")
    query = query.replace("hello ","")
    query = query.replace("hii ","")
    query = query.replace("hi ","")
    query = query.replace("eric","")
    query = query.strip()
    return query

def Filter_1(query):
    query = query.strip()
    return query

def Filter_2(query):
    query = query.lower()
    query = query.strip()
    query = query.title()
    return query

def PlaySong():
    from random import choice
    music_dir = 'DataBase\\Songs\\'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,choice(songs)))

def My_IP():
    import socket
    Host_Name = socket.gethostname()
    IP_Address = socket.gethostbyname(Host_Name)
    return f"Your IP Address: {IP_Address}"

def WolframAlpha(query):
    api_key = Wolfram
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    try:
        Answer = next(requested.results).text
        try:
            Answer = int(Answer)
        except:
            pass
        if Answer is not int:
            try:
                Answer = Answer[:20]
                Answer = float(Answer)
                Answer = round(Answer,4)
            except:
                pass
        return Answer
    except:
        return "Sorry, But This Is Not Possible Right Now..."