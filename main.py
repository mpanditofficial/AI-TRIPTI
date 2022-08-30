"""
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
pip install pywhatkit
pip install wikipedia
pip install pyjokes

"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb
import os
import pyautogui

count=0
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(audio, rate=180):
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = r.listen(source)
        r.pause_threshold = 2

    try:
        print("Recognizing....")
        command = r.recognize_google(voice, language='en-in')
        command = command.lower()
        if 'tripti' in command:
            command = command.replace('tripti','')
            print(command)

    except Exception as e:
        return "None"
    return command


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    print("The current time is ", Time)
    talk("the current time is",)
    talk(Time)



def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
    talk("the current date is")
    talk(day)
    talk(month)
    talk(year)


def wishme():
    print("Welcome back sir!!")
    talk("Welcome back sir!!")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        print("Good Morning !!")
        talk("Good Morning !!")

    elif hour >= 12 and hour < 16:
        print("Good Afternoon !!")
        talk("Good Afternoon !!")

    elif hour >= 16 and hour < 24:
        print("Good Evening !!")
        talk("Good Evening !!")

    else:
        print("Good Night Sir, See You Tomorrow.")
        talk("Good Night Sir, See You Tomorrow")

    print("Tripti at your service sir, please tell me how may I help you.")
    talk("Tripti at your service sir, please tell me how may I help you.")


if __name__ == "__main__":
    wishme()
    while True:
        command = take_command().lower()

        if "who are you" in command:
            print("I'm T.R.I.P.T.I.  an AI created by Mr. Manish and I'm a desktop voice assistant.")
            talk("I'm TRIPTI an AI created by Mr. Manish and I'm a desktop voice assistant.")

        elif "your name" in command:
            print("You can call me T.R.I.P.T.I. which is an acronym of Technically Really Intelligent Packet Transmitting Interpreter.")
            talk(" You can call me Tripti which is an acronym of Technically Really Intelligent Packet Transmitting Interpreter ")

        elif "you do" in command:
            print("I have a lot to offer :\n"
                  "I can open any Website, Chrome and Youtube.\n"
                  "I can search anything on chrome,just say 'search'. \n"
                  "I can also search about famous personality on wikipedia.\n"
                  "I can help you to take a Screenshot.\n"
                  "You can ask me to play some music and videos to entertain you.\n"
                  "I can tell you the current date and time.\n"
                  "I can also tell you a joke to put a smile on your face and even remember anything for you.\n")

            talk("I have a lot to offer :\n"
                  "I can open any Website, Chrome and Youtube.\n"
                  "I can search anything on chrome, just say 'search'.\n"
                  "I can also search about famous personality on wikipedia.\n"
                  "I can help you to take a Screenshot.\n"
                  "You can ask me to play some music and videos to entertain you.\n"
                  "I can tell you the current date and time.\n"
                  "I can also tell you a joke to put a smile on your face and even remember anything for you.\n")


        elif "how are you" in command:
            print("I'm fine sir, What about you?")
            talk("I'm fine sir, What about you?")


        elif 'thank' in command:
            print("I’m so pleased to hear that you liked it.")
            talk("I’|m so pleased to hear that you liked it")


        elif "time" in command:
            time()

        elif "date" in command:
            date()

        elif 'play' in command:
            song = command.replace('play','')
            print('playing '+song)
            talk('playing ' +song)
            pywhatkit.playonyt(song)

        elif 'who is' in command:
            try:
                print("Ok wait sir, I'm searching...")
                talk("Ok wait sir, I'm searching...")
                command = command.replace("wikipedia", "")
                result = wikipedia.summary(command, sentences=1)
                print("According to wikipedia, ",result)
                talk("According to wikipedia, ")
                talk(result)
            except:
                talk("Can't find this page sir, please ask something else")




        elif "open " in command:
            wordlist = command.split()
            web = wordlist[-1]
            website = web+".com"
            print("opening " + web)
            talk("opening " +web)
            wb.open_new_tab(website)



        elif "chrome" in command:
            talk("opening Chrome")
            chromePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(chromePath)

        elif "search" in command:
            try:
                print("What should I search ?")
                talk("What should I search ?")
                search = take_command()
                print(search)
                wb.open_new_tab(search)

            except Exception as e:
                talk("Can't open now, please try again later.")
                print("Can't open now, please try again later.")


        elif "remember something" in command:
            talk("What should I remember")
            data = take_command()
            print("Ok sir I will remember that " + str(data))
            talk("Ok sir I will remember that " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()


        elif "do you remember anything" in command:
            f = open('data.txt')
            rem= f.read()
            print("You told me to remember that", rem)
            talk("You told me to remember that " + rem)
            f.close()
            

        elif 'are you single' in command:
            print('I am in a relationship with wifi.')
            talk('I am in a relationship with wifi')

        elif 'joke' in command:
            j = pyjokes.get_joke()
            print(j)
            talk(j)
        
        elif 'screenshot' in command:
            img = pyautogui.screenshot()
            img.save(f"screenshots\\img{count}.png")
            count = count+1
            print("Screenshot has successfully taken.")
            talk("Screenshot has successfully taken")

        elif 'bye' in command:
            print('Bye Sir , Thank you for spending time with me !!')
            talk('Bye Sir , Thank you for spending time with me ')
            break

        else:
            print('Please say that command again !')
            talk('Please say that command again !')


'''
# open any site
# tells you the time
# play music
# play videos
# can take screenshot
# search about famous personality
# can remember
# tell jokes

'''