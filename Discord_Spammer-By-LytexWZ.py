# This script is harmless and does not inject any illegal thing into your Discord app, it uses key events to spam the chat
# Made by LytexWZ to win Mr.Juice in the discord.gg/universalfarm server messages leaderboard

import keyboard
import time
from threading import Thread, Event

interval = 0.7
duration = 30
toggle_event = Event()
enter_press_count = 0

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
    global enter_press_count
    while True:
        toggle_event.wait()
        start_time = time.time()
        while time.time() - start_time < duration:
            if not toggle_event.is_set():
                break
            keyboard.write('.')
            time.sleep(0.02)
            keyboard.send('enter')
            enter_press_count += 1
            print(f"Messages sent: {enter_press_count}", end='\r')
            time.sleep(interval - 0.01)
        if toggle_event.is_set():
            for i in range(30, 0, -1):
                print(f"Sleeping for {i} seconds to avoid spam cooldown... ", end='\r')
                time.sleep(1)
            print(" " * 50, end='\r')  # Clear the line

def toggle():
    script_enabled = False
    while True:
        keyboard.wait('-')
        if toggle_event.is_set():
            toggle_event.clear()
            print("\nScript is disabled.")
            script_enabled = False
        else:
            toggle_event.set()
            print("\nScript is enabled.")
            script_enabled = True
        time.sleep(0.3)

if __name__ == "__main__":
    print(ascii_art)
    print()
    print("Script made by LytexWZ, feel free to report any issues here: https://github.com/LytexWZ")
    print("Press '-' to toggle the loop.")
    print()
    print("Script is inactive.")
    print("This script will stop after 30 secs to avoid discord spam cooldown.")
    print("Be aware that once the spam cooldown has started, you will NOT be able to stop it, this is made to prevent detection.")
    
    # Start key pressing thread
    Thread(target=press_keys, daemon=True).start()
    # Start listening thread
    Thread(target=toggle, daemon=True).start()
    
    # Keep script alive
    while True:
        time.sleep(1)
    # Keep script alive
    while True:
        time.sleep(1)
