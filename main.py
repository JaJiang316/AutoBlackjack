import pyautogui
import pytesseract
from threading import Thread
from pynput import keyboard
import time
pyautogui.PAUSE = 1


def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            user_input = input(
                'Program paused, would you like to continue? (y/n) ')

            while user_input != 'y' and user_input != 'n':
                user_input = input('Incorrect input, try either "y" or "n" ')

            if user_input == 'y':
                main.status = 'run'
            elif user_input == 'n':
                main.status = 'exit'
                exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'run'

    while True:
        print('running')
        time.sleep(1)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(
            r'C:\Users\Jason\Desktop\Self Projects\Screen Reader\screenshot_1.png')
        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


Thread(target=main).start()
Thread(target=exit_program).start()
