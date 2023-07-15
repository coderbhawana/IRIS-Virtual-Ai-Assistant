import sys
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import requests
import pywhatkit as kit
import os
import subprocess as sp
import pyautogui
import json
import ecapture as ec
import wikipedia

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def play_youtube(query):
    kit.playonyt(query)


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Dell\\OneDrive\\Pictures\\Screenshots\images.png")


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])


def time(query):
    Time = datetime.datetime.now().strftime("%I:%M:%S")


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def get_news():
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=34c6bf17ef8c4fdd86e7c815fcb16d5d"
    response = requests.get(url)
    data = json.loads(response.text)
    articles = data["articles"]
    for article in articles:
        title = article["title"]
        source = article["source"]["name"]
        speak(f" {title}")
        print(f"{source} - {title}")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    return recognizer.recognize_google(audio)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
        print("iris : Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
        print("iris : Good Afternoon!")
    elif 18 <= hour < 22:
        speak("Good Evening!")
        print("iris : Good Evening!")
    else:
        speak("Good Night!")
        print("iris : Good Night!")

    speak(f"I am iris. Please tell me how may I help you")
    print(f"iris : I am IRIS. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" Bhawana : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return 'None'
    return query


def get_command():
    pass


def search_web(query):
    pass


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://youtube.com")
        elif 'close youtube' in query:
            speak("here you go to youtube\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open chatgpt' in query:
            speak("Here you go to chatgpt\n")
            webbrowser.open("https://chat.openai.com/")
        elif 'close chatgpt' in query:
            speak("here you go to chatgpt\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif "play on youtube" in query:
            speak("What would you like me to play on YouTube?")
            query = listen()
            play_youtube(query)


        # normal communications
        elif 'hello' in query:
            speak("hello,how are you?")
            speak("Your Personal AI Assistant!")
            speak("How May I Help You?")
            print("iris : hello,how are you?")
            print("Your Personal AI Assistant!")
            print("How May I Help You?")
        elif 'Iris' in query:
            speak("Yes")
            print("iris : yes")
        elif 'how are you' in query:
            speak("I am fine")
            speak("Whats About YOU?")
            print("iris : I am fine")
            print("Whats About YOU?")
        elif 'i am fine' in query:
            speak("good. how can i help you?")
            print("iris : good. how can i help you?")
        elif 'i want help' in query:
            speak("yes,i am here to help you ")
            print("iris : yes,i am here to help you ")
        elif 'are you human' in query:
            speak("no i am an ai assistant made by Bhawana")
            print("iris : no i am an ai assistant made by Bhawana")
        elif 'what is your name' in query:
            speak("my name is iris")
            print("iris : my name is iris")
        elif 'you need a break' in query:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak("Just Say Wake Up Jarvis!")

        elif 'open myntra' in query:
            speak("Here you go to myntra\n")
            webbrowser.open("https://myntra.com/")
        elif 'close myntra' in query:
            speak("here you go to myntra\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'facebook' in query:
            speak("Here you go to facebook\n")
            webbrowser.open('https://www.facebook.com/')
        elif 'close facebook' in query:
            speak("here you go to facebook\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open instagram' in query:
            speak("Here you go to instragram\n")
            webbrowser.open('https://www.instagram.com/')
        elif 'close instragram' in query:
            speak("here you go to instragram\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif "search" in query:
            speak("What would you like me to search for?")
            print("iris : What would you like me to search for?")
            query = listen()
            search_web(query)

        elif "news" in query:
            speak("okay i will search for you")
            print("iris : okay i will search for you")
            speak("Here you go to news\n")
            get_news()

        elif "take a photo" in query:
            speak("Here you go to take your photo \n")
            ec.capture(0, "robo camera", "img.jpg")

        elif 'open dominos' in query:
            speak("Here you go to dominos\n")
            webbrowser.open("https://www.dominos.co.in/")
        elif 'close dominos' in query:
            speak("here you go to dominos\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open flipkart' in query:
            speak("Here you go to flipkart\n")
            webbrowser.open("https://flipkart.com")
        elif 'close flipkart' in query:
            speak("here you go to flipkart\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open zomato' in query:
            speak("Here you go to zomato\n")
            webbrowser.open("https://zomato.com")
        elif 'close zomata' in query:
            speak("here you go to zomato\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open amazon' in query:
            speak("Here you go to amazon\n")
            webbrowser.open("https://amazon.com")
        elif 'close amazon' in query:
            speak("here you go to amazon\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open resso' in query:
            speak("Here you go to resso\n")
            webbrowser.open("https://resso.com")
        elif 'close resso' in query:
            speak("here you go to resso\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open google' in query:
            speak("Here you go to google\n")
            webbrowser.open("https://google.com")
        elif 'close google' in query:
            speak("here you go to google\n")
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open whatsapp' in query:
            speak("Here you go to whatsapp\n")
            webbrowser.open("web.whatsapp.com")

        elif 'open notepad' in query:
            speak("Here you go to notepad\n")
            open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            speak("Here you go to cmd\n")
            open_cmd()

        elif 'open camera' in query:
            speak("Here you go to camera\n")
            open_camera()

        elif 'open calculator' in query:
            speak("Here you go to calculator\n")
            open_calculator()

        elif 'play music' in query:
            music_dir = 'C://Users//Public//Music'
            songs = os.listdir(music_dir)
            speak("Here you go to music\n")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%I:%M:%S")
            speak("the time is")
            speak(Time)
            print("The current time is ", Time)

        elif 'the date' in query:
            day = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)
            speak("The current date is " + str(day) + str(month) + str(year))
            print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                speak(month)
                print(month)


            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                speak(day)
                print(day)


            tell_day()

        elif 'close notepad' in query:
            speak("Here you go to close notepad\n")
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'close calculator' in query:
            speak("Here you go to close calculator\n")
            os.system("TASKKILL /F /IM calc.exe")

        elif 'open blackboard' in query:
            speak("Here you go to blackboard\n")
            webbrowser.open("blackboard.com")

        elif 'open stack overflow' in query:
            speak("Here you go to stack overflow\n")
            webbrowser.open("stackoverflow.com")

        elif "advice" in query:
            speak(f"Here's an advice for you")
            print(f" iris : Here's an advice for you")

            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen.")
            print("iris : For your convenience, I am printing it on the screen.")
            print(advice)

        elif "jokes" in query:
            speak(f"Hope you like this one")
            print("iris : Hope you like this one")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen.")
            print("iris : For your convenience, I am printing it on the screen.")
            print(joke)

        elif "exit" in query:
            speak("Goodbye! Thanks for testing me . Have a nice day !!!")
            print("iris : Goodbye! Thanks for testing me . Have a nice day !!!")
            sys.exit()

        elif "send a whatsapp message" in query:
            speak("Here you go to send whatsapp message\n")
            speak('On what number should I send the message? Please enter in the console: ')
            print('iris : On what number should I send the message? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message? please enter your message")
            print("iris : What is the message? please enter your message")
            message = input("Enter your message: ")
            send_whatsapp_message(number, message)
            speak("I've sent the message.")
            print("iris : I've sent the message.")

        elif "screenshot" in query:
            speak("Here you go to take screenshot\n")
            screenshot()
            speak("I've taken screenshot, please check it in the folder.")
            print("iris : I've taken screenshot, please check it in the folder.")
            break
        else:
            speak("Sorry, I didn't understand that. Could you please repeat?")
            print("iris : Sorry, I didn't understand that. Could you please repeat?")