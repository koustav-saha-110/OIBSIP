import os
import time
import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as speech

system = pyttsx3.init()
system.setProperty('rate', 170)


def say(audio):
    print(audio)
    system.say(audio)
    system.runAndWait()


def wishme():
    hour = time.strftime("%H")
    hour = int(hour)

    if 0 <= hour <= 11:
        say("Good Morning..")

    elif 12 <= hour <= 17:
        say("Good Afternoon..")

    elif 18 <= hour <= 23:
        say("Good Evening..")


def speak():
    s = speech.Recognizer()
    with speech.Microphone() as source:
        print('listening..')
        s.energy_threshold = 400
        s.pause_threshold = 1
        sound = s.listen(source)

        try:
            print('recognizing..')
            content = s.recognize_google(sound, language='en-in')
            print(f"User said : {content}")
            return content

        except Exception as e:
            print(e)
            return "none"


def execute_command(audio):
    if "none" in audio:
        say("sorry i didnt understand that..")
        say("please try again..")

    else:
        if "date and time" in audio:
            dateandtime()

        elif "exit" in audio:
            say("Goodbye.."), exit()

        elif "wikipedia" in audio:
            say("searching in wikipedia..")
            audio = audio.replace("search in wikipedia about ", "")
            result = wikipedia.summary(audio, sentences=3)
            say("according to the wikipedia summary..")
            say(result)
            time.sleep(3)

        elif "google" in audio:
            say("opening google.com..")
            webbrowser.open("https://www.google.com/")
            say("successfully opened google.com")
            time.sleep(2)

        elif "youtube" in audio:
            say("opening youtube.com..")
            webbrowser.open("https://www.youtube.com/")
            say("successfully opened youtube.com")
            time.sleep(2)

        elif "github" in audio:
            say("opening github..")
            webbrowser.open("https://www.github.com/koustav-saha-110")
            say("successfully opened github")
            time.sleep(2)

        elif "search" in audio:
            say("what should i search?..")
            search = speak().lower()
            say("searching..")
            webbrowser.open("https://www.google.com/search?q=" + search)
            say("searched successfully..")
            time.sleep(2)

        elif "close the web browser" in audio:
            say("ok, closing the web browser")
            os.system("taskkill /F /IM msedge.exe")
            say("successfully closed the browser")
            time.sleep(2)

        elif "current path" in audio:
            path = os.getcwd()
            print(f"The Current path is : {path}")
            system.say(f"The Current path is : {path}")
            system.runAndWait()

        elif "create a to do list" in audio or "write a note" in audio:
            path = os.getcwd()
            say("tell me what should i write on it??")
            content = speak().lower()
            say("what will be the name of the file??")
            name = speak().lower()
            name = name + ".txt"
            open(name, "w").write(content)
            os.startfile(f"{path}/{name}")
            say("successfully written and saved..")
            time.sleep(5)

        elif "create a new file" in audio:
            say("What will be the name of the file?")
            name = speak().lower()
            say("enter what will be the extension of the file..")
            ext = input("Enter the extension name(like -> .txt,.py etc(use dot before the extension)) : ")
            name = name + ext
            open(name, "w").close()
            say("the file has been successfully created..")
            time.sleep(1)

        elif "new folder" in audio:
            say("what will be the name of the folder??")
            name = speak().lower()

            if (not os.path.exists(name)):
                os.mkdir(name)
                say("the folder is successfully created..")

            else:
                say("The folder with the given name already exists..")
                say("Failed to create the folder with the given name..")
                say("Try gain with a different name..")

        elif "stop listening" in audio:
            say("enter for how many seconds you want me to stop listening to your command..")
            seconds = int(input("Enter the seconds : "))
            print("stopped listening for " + str(seconds) + " seconds")
            system.say("stopped listening for " + str(seconds) + " seconds")
            time.sleep(seconds)
            say("hey, i am listening now.")

        elif "more than one" in audio:
            print("executing the command..")

            say("enter how many files you want to create?..")
            number = int(input("Enter the number : "))

            say("what should be the name of the file?..")
            name = speak().lower()

            path = os.getcwd()

            for i in range(number + 1):
                os.mkdir(f"{name}{i + 1}")

            say("done..")
            print(f"{number} Folders Created in the path : {path}")
            system.say(f"{number} Folders Created in the path : {path}")
            system.runAndWait()

        else:
            say("i cant do that operation!...")
            say("say something else..")
            time.sleep(2)


def dateandtime():
    d = time.strftime("%D")
    t = time.strftime("%H-%M-%S")

    print(f"Today's Date : {d}")
    system.say(f"Today's Date : {d}")
    system.runAndWait()

    print(f"Time right now : {t}")
    system.say(f"Time right now : {t}")
    system.runAndWait()


if __name__ == "__main__":
    wishme()
    say("how can i assist you today?..")

    while True:
        command = speak().lower()
        execute_command(command)