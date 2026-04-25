import random
import openai
from DataBase.Config import *
from Features import Filter_1
from Features import Filter_2

Reply_Hello = ("Hey, How Are You ?")
            # "Hello Sir",
            # "Hello Sir, Nice To Meet You Again.",
            # "Of Course Sir, Hello .")

Reply_Bye = ('Bye Sir.',
            "It's Okay.",
            "It Will Be Nice To Meet You.",
            "Thanks.",
            "Okay Sir, You Can Call Me Anytime.",
            "Okay.",
            "Thank You, I am Going Offline")

Reply_How = ('I Am Fine.',
            "Excellent.",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

Reply_Nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.",
            "Thank You")

Reply_Functions = ('I Can Perform Many Tasks Such As Assist You, Casual Chatting, Searching On Web For Best Result, Some Basic Maths And Much More',
            'Let Me Ask You First, How Can I Help You ?')

Sorry_Reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.",
                "I'm sorry, I don't know how to respond to that.")

Whatsup_Reply = ("Not Much, Just Waiting For Your Command",
                 "Just Hanging Out. How About You",
                 "Nothing Too Exciting",
                 "Just Finished Some Work",
                 "Well, I Am Working On a Top Secret Project That involves building a time machine.")

Reply_Fine = ("That's Good To Hear.",
              "I'm Glad To Hear That",
              "Great!",
              "I'm Here If There's Anything I Can Do For You.",
              "Ohh That's Great!")

def ChatBot(query):
        query = query.replace("whatsapp","what's up")

        if (("how are you" in query or "are you fine" in query or "what's up" in query or "whats up" in query) and ("translate" not in query)):
            reply = random.choice(Reply_How)
            return reply
        
        elif (("hey" in query or "hello" in query or "hi" in query or "hay" in query) and ("translate" not in query and "this" not in query)):
            reply = Reply_Hello
            return reply
        
        elif len(query) <= 3:
            return ""
        
        elif (("fine" in query or "good" in query) and ("translate" not in query)):
            reply = random.choice(Reply_Fine)
            return reply

        elif (("restore" not in query or "translate" not in query) and ("by" in query or "bye" in query or "exit" in query or "sleep" in query or "go" in query or "by" in query or "relax" in query or "rest" in query or "goodbye" in query)):
            reply = random.choice(Reply_Bye)
            return reply

        elif (("nice" in query or "good" in query or "excellent" in query or "great" in query) and ("translate" not in query)):
            reply = random.choice(Reply_Nice)
            return reply
        
        elif "thank" in query:
            reply = ("welcome","your welcome")
            reply = random.choice(reply)
            return reply

        elif (("functions" in query or "abilities" in query  or "what can you do" in query) and ("translate" not in query)):
            reply = random.choice(Reply_Functions)
            return reply

        elif (("what are you doing" in query or "how about you" in query or "what's going on" in query or "whats going on" in query) and ("translate" not in query)):
            reply = random.choice(Whatsup_Reply)
            return reply
        
        else:
            query = Filter_1(query)
            openai.api_key = Bot_Value
            with open("Chat.txt", "a") as Chat:
                Chat.write(f"User : {query}\n")
            response = openai.Completion.create(
                model = "text-davinci-002",
                prompt = query,
                temperature = 0.5,
                max_tokens = 60,
                top_p = 0.3,
                frequency_penalty = 0.5,
                presence_penalty = 0
            )
            # print(Content)
            Output = response.choices[0].text.strip()
            Output = Filter_2(Output)
            with open("Chat.txt", "a") as Chat:
                Chat.write(f"Eric : {Output}\n")
            if 'program' in query or 'code' in query or '<' in Output:
                return "The Code Is Provided In Conversation File"
            else:
                return Output
