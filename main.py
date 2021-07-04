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


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


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
                exit()
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
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
        time.sleep(2)

        myScreenshot = pyautogui.screenshot(region=(393, 472, 898, 332))
        myScreenshot.save(
            r'C:\\Users\\Jason\Desktop\\Self Projects\\Screen Reader\\images\\screenshot_1.png')

        dealerHandimg = pyautogui.screenshot(region=(1017, 317, 72, 69))
        dealerHandimg.save(
            r'C:\\Users\\Jason\\Desktop\\Self Projects\\Screen Reader\\images\\dealerHand.png')

        cardTotal = pyautogui.screenshot(region=(1012, 650, 77, 74))
        cardTotal.save(
            r'C:\\Users\\Jason\\Desktop\\Self Projects\\Screen Reader\\images\\userTotal.png')

        if(pyautogui.locateOnScreen('images\\Deal_button.png') != None):
            dealbuttonx, dealbuttony = pyautogui.locateCenterOnScreen(
                'images\\Deal_button.png')
            pyautogui.click(dealbuttonx, dealbuttony)

        dealerImage = cv2.imread('images\\dealerHand.png')
        gray = get_grayscale(dealerImage)
        noise = remove_noise(gray)
        cv2.imwrite('images\\dealerHand.png', gray)
        dealersHand = pytesseract.image_to_string(gray)
        print(dealersHand)
        # dealersHand = int(dealersHand)

        # playerImage = cv2.imread('images\\userTotal.png')
        # playersHand = pytesseract.image_to_string(playerImage)
        # print(playersHand)
        # playersHand = int(playersHand)

        # if(dealersHand == 7 or dealersHand == 8 or dealersHand == 9 or dealersHand == 10 or dealersHand == 11):
        #     while(playersHand < 17):
        #         hitbuttonx, hitbuttony = pyautogui.locateCenterOnScreen(
        #             'images\\Hit_button.png')
        #         pyautogui.click(hitbuttonx, hitbuttony)
        #         cardTotal = pyautogui.screenshot(region=(1012, 650, 77, 74))
        #         cardTotal.save(
        #             r'C:\\Users\\Jason\\Desktop\\Self Projects\\Screen Reader\\images\\userTotal.png')
        #         playerImage = cv2.imread('images\\userTotal.png')
        #         playersHand = int(pytesseract.image_to_string(playerImage))
        #     if(playersHand >= 21):
        #         break
        #     if(pyautogui.locateOnScreen('images\\Stand_button.png') != None):
        #         standbuttonx, standbuttony = pyautogui.locateCenterOnScreen(
        #             'images\\Stand_button.png')
        #         pyautogui.click(standbuttonx, standbuttony)
        # img = cv2.imread('screenshot_1.png')
        # gray = get_grayscale(img)
        # print(pytesseract.image_to_string(gray))
        # cv2.imwrite('screenshot_1.png', gray)
        while (main.status == 'pause'):
            time.sleep(2)

        if (main.status == 'exit'):
            print('Main program closing')
            break


s = threading.Thread(target=main, name='mainprogram')
s.start()
t = threading.Thread(target=exit_program, name='screenshot')
t.start()
