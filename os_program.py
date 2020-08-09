import os

while True:
    print("1.Notepad\n2.Chrome\n3.VLC Media Player\n4.Exit\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        os.system("notepad")
    elif choice == 2:
        os.system("chrome")
    elif choice == 3:
        os.system("vlc")
    elif choice == 4:
        break
