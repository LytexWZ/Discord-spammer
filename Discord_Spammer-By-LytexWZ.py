#This script is harmless and does not inject any ilegal thing into your discord app, it uses key events to spam the chat
#Made by LytexWZ to win Mr.Juice in the discord.gg/universalfarm server messages leaderboard

import keyboard
import time
from threading import Thread, Event

interval = 0.7
duration = 30
toggle_event = Event()

ascii_art = """
 _______   ______   ______    ______    ______   _______   _______            ______   _______    ______   __       __  __       __  ________  _______  
|       \ |      \ /      \  /      \  /      \ |       \ |       \          /      \ |       \  /      \ |  \     /  \|  \     /  \|        \|       \ 
| $$$$$$$\ \$$$$$$|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$\| $$$$$$$\        |  $$$$$$\| $$$$$$$\|  $$$$$$\| $$\   /  $$| $$\   /  $$| $$$$$$$$| $$$$$$%
| $$  | $$  | $$  | $$___\$$| $$   \$$| $$  | $$| $$__| $$| $$  | $$ ______ | $$___\$$| $$__/ $$| $$__| $$| $$$\ /  $$$| $$$\ /  $$$| $$__    | $$__| $$
| $$  | $$  | $$   \$$    \ | $$      | $$  | $$| $$    $$| $$  | $$|      \ \$$    \ | $$    $$| $$    $$| $$$$\  $$$$| $$$$\  $$$$| $$  \   | $$    $$
| $$  | $$  | $$   _\$$$$$$\| $$   __ | $$  | $$| $$$$$$$\| $$  | $$ \$$$$$$ _\$$$$$$\| $$$$$$$ | $$$$$$$$| $$\$$ $$ $$| $$\$$ $$ $$| $$$$$   | $$$$$$%
| $$__/ $$ _| $$_ |  \__| $$| $$__/  \| $$__/ $$| $$  | $$| $$__/ $$        |  \__| $$| $$      | $$  | $$| $$ \$$$| $$| $$ \$$$| $$| $$_____ | $$  | $$
| $$    $$|   $$ \ \$$    $$ \$$    $$ \$$    $$| $$  | $$| $$    $$         \$$    $$| $$      | $$  | $$| $$  \$ | $$| $$  \$ | $$| $$     \| $$  | $$
 \$$$$$$$  \$$$$$$  \$$$$$$   \$$$$$$   \$$$$$$  \$$   \$$ \$$$$$$$           \$$$$$$  \$$       \$$   \$$ \$$      \$$ \$$      \$$ \$$$$$$$$ \$$   \$$
"""

def press_keys():
    while True:
        toggle_event.wait()
        start_time = time.time()
        while time.time() - start_time < duration:
            keyboard.write('.')
            time.sleep(0.01)
            keyboard.send('enter')
            time.sleep(interval - 0.01)
            if not toggle_event.is_set():
                break
        time.sleep(30)

def toggle():
    while True:
        keyboard.wait('-')
        if toggle_event.is_set():
            toggle_event.clear()
        else:
            toggle_event.set()
        time.sleep(0.3)

if __name__ == "__main__":
    print(ascii_art)
    print("Script made by LytexWZ")
    print("Press '-' to toogle the loop.")
    
    # Start key pressing thread
    Thread(target=press_keys, daemon=True).start()
    # Start listening thread
    Thread(target=toggle, daemon=True).start()
    
    # Keep script alive
    while True:
        time.sleep(1)
