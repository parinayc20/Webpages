#There is no need to load a you can directly start with your questions
#However if you give the command to load a it will load a again
#Please update to python 3.9 else errors MIGHT come (I am not sure that errors will come or not)
import pyttsx3
import aiml
import os
import speech_recognition as sr #install pyaudio as well, if errors come see the readme file
import requests 
import webbrowser
import wikipedia

r=sr.Recognizer()
kernel = aiml.Kernel()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)#you can change this to voices[1].id if you want a female voice
engine.setProperty('volume',100)
engine.setProperty('rate',200)#you can alter the number written here if you want the voice to speak faster or slower

def exit():
    print("BOT:",end=" ")
    sp("It was my pleasure talking to you. Goodbye...")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sp(out):
    print(out)
    speak(out)

def inputting(c):
    i=""
    if(c=="1"):
        i=input("USER: ")
    else:
        print("Listening...")
        i=listening()
        print("USER:",end=" ")
        print(i)   
    return i

def getValueOf(k, L):
    i=-1
    c=0
    for d in L:
        i=i+1
        if (d["Country"].lower()==k.lower()):
            c=1
            break
    if(c==1):
        return i 
    else:
        return -1

def statistics():
    sp("GLOBALLY OR COUNTRY WISE")
    count=inputting(c[0])
    print("Processing...")
    key='5cf9dfd5-3449-485e-b5ae-70a60e997864'
    url='https://api.covid19api.com/summary'
    paramsa={'X-Access-Token':key}
    response=requests.get(url,params=paramsa)
    stats=response.json()
    if(count.lower()=="globally" or count.lower()=="global"):
        sp("For global")
        sp("Total Confirmed:\t"+str(stats["Global"]["TotalConfirmed"]))
        sp("New Confirmed:\t\t"+str(stats["Global"]["NewConfirmed"]))
        sp("Total Recovered:\t"+str(stats["Global"]["TotalRecovered"]))
        sp("New Recovered:\t\t"+str(stats["Global"]["NewRecovered"]))
        sp("Total Deaths:\t\t"+str(stats["Global"]["TotalDeaths"]))
        sp("New Deaths:\t\t"+str(stats["Global"]["NewDeaths"]))
        return
    print("BOT:",end=" ")
    sp("PLEASE SPECIFY THE COUNTRY")
    country=inputting(c[0])
    place=getValueOf(country,stats["Countries"])
    if(place==-1):
        print("BOT:",end=" ")
        sp("Sorry! Country not found")
    else:
        print("BOT:",end=" ")
        sp("For "+str(country))
        sp("Date:\t"+str(stats["Countries"][place]["Date"]))
        sp("Total Confirmed:\t"+str(stats["Countries"][place]["TotalConfirmed"]))
        sp("New Confirmed:\t\t"+str(stats["Countries"][place]["NewConfirmed"]))
        sp("Total Recovered:\t"+str(stats["Countries"][place]["TotalRecovered"]))
        sp("New Recovered:\t\t"+str(stats["Countries"][place]["NewRecovered"]))
        sp("Total Deaths:\t\t"+str(stats["Countries"][place]["TotalDeaths"]))
        sp("New Deaths:\t\t"+str(stats["Countries"][place]["NewDeaths"]))
        
def browser1():
    url="http://bit.ly/2LDx8iq"
    sp("Finding hospitals near you")
    webbrowser.open_new_tab(url)

def browser2():
    url="https://www.worldometers.info/coronavirus/"
    sp("Showing you the current covid statistics")
    webbrowser.open_new_tab(url)

def browser3():
    url="https://www.youtube.com/watch?v=3PmVJQUCm4E"
    sp("Showing you the correct way to wash your hands")
    webbrowser.open_new_tab(url)

def health_checkup():
    sp("Running your health checkup")
    print("BOT:",end=" ")
    sp("Are you Covid-19 positive?")
    p = inputting(c[0])
    if p.lower() == "yes":
        print("BOT:",end=" ")
        sp("You are covid positive, please take proper care")
    else:
        print("BOT:",end=" ")
        sp("What is your body temperature? ")
        temperature=inputting(c[0])
        safe = 0
        unsafe = 0
        if(float(temperature) >= 99.5):
            print("BOT:",end=" ")
            sp("Your body temperature is high, take care of yourself")
            unsafe+=1
        else:
            print("BOT:",end=" ")
            sp("Your body temperature is fine, stay healthy")
            safe+=1
        print("BOT:",end=" ")
        sp("Did you visit any place outside your city in past 14 days? ")
        w=inputting(c[0])
        if w.lower() == "yes":
            unsafe += 1
            print("BOT:",end=" ")
            sp("Was your visit out of country? ")
            x=inputting(c[0])
            if x.lower() == "yes":
                unsafe += 1
        else:
            safe += 1

        print("BOT:",end=" ")
        sp("Do you have cough, fever, or experience difficulty in breathing? ")
        y=inputting(c[0])
        if y.lower() == "yes":
            unsafe += 5
        else:
            safe += 1

        if safe >= unsafe:
            print("BOT:",end=" ")
            sp("According to the cobot19, you are safe right now")
        else:
            print("BOT:",end=" ")
            sp("According to the cobot19, you are at risk, please take care or consult doctor")

def change_input():
    sp("Changing your input medium")
    if(c[0]=="1"):
        c[0]="7"
    else:
        c[0]="1"
    print("BOT:",end=" ")
    sp("Input medium changed")

def wiki():
    sp("For what do you want to search wikipedia")
    input1=inputting(c[0])
    print("Processing...")
    try:
        output=wikipedia.summary(input1,sentences=3)
        print("Bot:",end=" ")
        print("According to Wikipedia")
        speak("According to Wikipedia")
        sp(output)
    except Exception:
        print("BOT:",end=" ")
        sp("Sorry! No such content found")
    

def listening():
    said=""
    while(said==""):
        try:
            with sr.Microphone() as source:
                audio=r.listen(source)
                print("Recognizing...")
                said=r.recognize_google(audio,language='en-in')
        except Exception:
            print("Sorry! Please repeat...")
            speak("Sorry! Please repeat...")
            print("Listening...")
            said=""
    return said     

kernel.bootstrap(learnFiles="startup.xml")
kernel.bootstrap(learnFiles="a.xml")
print()
print()

greeting="Hello! I am Cobot-19. I am here to help you."
print(greeting)
speak(greeting)
c=["0","0"]
print("BOT:",end=" ")
sp("Please Specify Input")
print("1-Write")
speak("Press 1 to write")
print("Any other key-Speak")
speak("Press any other key to speak")
c[0]=input("USER: ")

print("BOT:",end=" ")
sp("Thanks for that! Now, please specify your queries below")
I=inputting(c[0])
while (I!="exit" and I!="Exit"):
    print("BOT:",end=" ") 
    output=kernel.respond(I)
    if(output=="1"):
        statistics()
    elif(output=="2"):
        browser1()
    elif(output=="3"):
        browser2()
    elif(output=="4"):
        browser3()
    elif(output=="5"):
        health_checkup()
    elif(output=="6"):
        wiki()
    elif(output=="7"):
        change_input()
    else:
        print(output)
        speak(output)
    I=inputting(c[0])
if(I=="exit" or I=="Exit"):
    exit()
