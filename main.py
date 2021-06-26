from PIL import Image
import pyautogui
import pytesseract
import threading
from pynput import keyboard
import numpy as np
import cv2
import time
import gc
import sys
from pytesseract.pytesseract import is_valid

pyautogui.PAUSE = 4
pyautogui.FAILSAFE = True
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# def remove_noise(image):
#     return cv2.medianBlur(image, 5)


# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            button = pyautogui.confirm(
                text='Continue or Stop the program', title='Confirm', buttons=['Continue', 'Exit'])
            if(button == 'Continue'):
                main.status = 'run'
            if(button == 'Exit'):
                main.status = 'exit'
            # user_input = input(
            #     'Program paused, would you like to continue? (y/n) ')
            # while user_input != 'y' and user_input != 'n':
            #     user_input = input('Incorrect input, try either "y" or "n" ')
            # if user_input == 'y':
            #     main.status = 'run'
            # elif user_input == 'n':
            #     main.status = 'exit'
            #     exit()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'run'
    while True:
        print('running')
        time.sleep(2)
        myScreenshot = pyautogui.screenshot(region=(300, 300, 300, 400))
        myScreenshot.save(
            r'C:\Users\Jason\Desktop\Self Projects\Screen Reader\screenshot_1.png')
        # img = cv2.imread('screenshot_1.png')
        # gray = get_grayscale(img)
        # print(pytesseract.image_to_string(gray))
        # cv2.imwrite('screenshot_1.png', gray)
        while (main.status == 'pause'):
            time.sleep(2)

        if (main.status == 'exit'):
            print('Main program closing')
            exit()


s = threading.Thread(target=main)
s.start()
t = threading.Thread(target=exit_program)
t.daemon = True
t.start()
