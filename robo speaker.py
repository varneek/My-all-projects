import pyttsx3

print("Welcome to robo speaker, this program is made by Varneek Nagar!")
speak = pyttsx3.init()
print("enter 0 to close the program")
while True:
    x = input('enter what you want to say:-')
    if x == "0":
        speak.say("Thankyou for using this program...program is closing")
        speak.runAndWait()
        break
    speak.say(x)
    speak.runAndWait()