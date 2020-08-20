import pyttsx3 as tts
import os

while True:

    print()
    print("What do you want, please enter something: ", end="")
    menu = input("").lower()

    # break condition
    if (("stop" in menu) or ("exit" in menu) or  ("close" in menu)):
        print("\n--------------------- Exit from Menu --------------------")
        tts.speak("Bye, meet you soon!")
        break

    # for chrome and for firefox
    elif ((("run" in menu) or ("launch" in menu) or ("open" in menu) or ("execute" in menu) or ("want" in menu)) and (("google" in menu) or ("browser" in menu) or ("chrome" in menu))):
        print("\nOpening Google chrome for you...\n")
        tts.speak("Here is google chrome for you!")
        os.system("chrome")

    elif ((("run" in menu) or ("launch" in menu) or ("open" in menu) or ("execute" in menu) or ("want" in menu)) and (("firefox" in menu) or ("mozilla" in menu))):
        print("\nOpening firefox for you...\n")       
        tts.speak("Here is mozilla firefox for you!")
        os.system("firefox")

    # for editor and IDE
    elif ((("run" in menu) or ("launch" in menu) or ("open" in menu) or ("execute" in menu) or ("want" in menu)) and (("notepad" in menu) or (" text editor" in menu))):
        print("\nOpening notepad for you...\n")
        tts.speak("Here is Notepad for you!")
        os.system("notepad")

    elif (("sublime" in menu)  and (("run" in menu) or ("launch" in menu) or ("open" in menu) or ("execute" in menu) or ("want" in menu))):
        print("\nOpening sublime text editor for you...\n")        
        tts.speak("Here is sublime text editor for you!")
        os.system("sublime_text")

    elif ((("run" in menu) or ("launch" in menu) or ("open" in menu) or ("execute" in menu) or ("want" in menu)) and (("vscode" in menu) or ("ide" in menu) or ("IDE" in menu) or ("visual studio" in menu))):
        print("\nOpening Visual studio code for you...\n")
        tts.speak("Here is Visual studio code for you!")
        os.system("Code")

    elif ((("run" in menu) or ("launch" in menu) or ("open" in menu) or ("execute" in menu) or ("want" in menu)) and (("spyder" in menu))):
        print("\nOpening spyder IDE for you...\n")
        tts.speak("Here is spyder IDE for you!")
        os.system("spyder")


    # for music
    elif ((("windows" in menu) or ("wm" in menu) or ("media" in menu) or ("mp3" in menu) or ("mp4" in menu)) and ("player" in menu)):
        print("\nOpening windows media  player for you...\n")
        tts.speak("Here is Windows media player for you!")
        os.system("wmplayer")

    elif ((("vlc" in menu) or ("media" in menu)) and ("player" in menu)):
        print("\nOpening VLC media player for you...\n")
        tts.speak("Here is vlc media player for you!")
        os.system("vlc")

    else:
        print("\n******* Menu not found, please try again *******\n")
        tts.speak("Sorry, menu not available, please try with another menu!")
