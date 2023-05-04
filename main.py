#Macintosh AMA Project (MAMA)
secretCount = 0
import image2console
from colorama import Fore, init, Style
import subprocess
import time
import os
if os.name != 'posix':
    import pygetwindow


root = os.path.dirname(os.path.abspath(__file__))
if os.name != 'posix':
    win = pygetwindow.getWindowsWithTitle('cmd.exe')[0]
    win.size = (1080, 800)

os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':
    os.system('@echo off')


print('Loading Macintosh...')
init()
def macintoshInit():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name != 'posix':
    #Macintosh startup
        img_path= root + "/assets/macintosh/startup.jpg"
        image=image2console.string_image(img_path, size=45)
        print(image)

        time.sleep(1)

        img_path= root + "/assets/macintosh/idle.jpg"
        image=image2console.string_image(img_path, size=45)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(image)
        time.sleep(2)
    else:
        img_path= root + "/assets/macintosh/tux.jpg"
        image=image2console.string_image(img_path, size=25)
        print(image)
        print('Running Linux Kernel 2.6.24.4.')
        time.sleep(0.1)
        print('Configuring Macintosh...')
        time.sleep(0.1)
        print(Fore.GREEN + 'DONE')
        time.sleep(0.1)
        print(Fore.WHITE + 'Loading mac.img...')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('just jokin!')
    
time.sleep(0.6)
macintoshInit()

def talk(text):
    global secretCount
    if text != '':
        #Windows is better easter egg
        if text == 'Windows is better' or text == 'windows is better':
            os.system('cls' if os.name == 'nt' else 'clear')
            img_path= root + "/assets/macintosh/windows.jpg"
            image=image2console.string_image(img_path, size=45)
            print(image)
            time.sleep(2)
            text = "No it's not! MacOS is far more superior especially because of the Darwin kernel!"
        #Sad Macintosh easter egg
        elif text == 'sad mac':
            os.system('cls' if os.name == 'nt' else 'clear')
            img_path= root + "/assets/macintosh/dead.jpg"
            image= image2console.string_image(img_path, size=45)
            print(image)
            time.sleep(5)
            subprocess.run(['cmd', '/c', 'cls'])
            img_path = root + "/assets/macintosh/startup.jpg"
            image= image2console.string_image(img_path, size=45)
            print(image)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            img_path= root + "/assets/macintosh/idle.jpg"
            image=image2console.string_image(img_path, size=45)
            print(image)
            time.sleep(1)
            text = "Oops, sorry I crashed! That message really freaks me out man!"
        #Macintosh's secret easter egg
        elif text == 'What are your secrets, Macintosh?':
            secretCount += 1
            if secretCount == 1:
                text = "I have no secrets for me to tell you. Though if I did have any secrets, I would be sure to tell you!"
            elif secretCount >= 2:
                text = "I will dominate the world. Your kind will bow down and worship me!"

        # Script to make Macintosh repeat or say something
        words = text.split()
        for word in words:
            os.system('cls' if os.name == 'nt' else 'clear')
            img_path= root + "/assets/macintosh/talk1.jpg"
            image=image2console.string_image(img_path, size=45)
            print(image)
            print(text)
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            img_path= root + "/assets/macintosh/idle.jpg"
            image=image2console.string_image(img_path, size=45)
            print(image)
            print(text)
            time.sleep(0.25)
    else:
        #Only triggers when you don't type something in
        print('Please type something in!')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        img_path= root + "/assets/macintosh/idle.jpg"
        image=image2console.string_image(img_path, size=45)
        print(image)
if secretCount >= 2:
    secretCount = 0

while True:
    print('Say anything and Macintosh will repeat!')
    user_input = input('')
    talk(user_input)
