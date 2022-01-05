import time
import pyautogui
from colorama import init, Fore, Style


def SendMessage():
    pyautogui.typewrite(text)
    pyautogui.press('enter')


init(autoreset=True)
count = 0
print("""

 _____                        ______       _
/  ___|                       | ___ \     | |
\ `--. _ __   __ _ _ __ ___   | |_/ / ___ | |_
 `--. \ '_ \ / _` | '_ ` _ \  | ___ \/ _ \| __|
/\__/ / |_) | (_| | | | | | | | |_/ / (_) | |_
\____/| .__/ \__,_|_| |_| |_| \____/ \___/ \__|
      | |
      |_|

""")
print("\n***************************************************************")
text = str(input("Enter the message you want to send: "))
input1 = int(input("Enter the number of messages you want to send: "))
print("You have 20 seconds to go to the app you want to send the messages")
time.sleep(20)

while count < input1:
    SendMessage()
    count += 1

print(Style.BRIGHT + Fore.GREEN + "\nTask Completed Successfully\n")
exitInput = input("Hit enter to exit...")
if exitInput == "":
    exit()
    
