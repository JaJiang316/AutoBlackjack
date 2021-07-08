# AutoBlackjack 🎰

## About 📚

AutoBlackjack is a program I developed to play blackjack for you without any human interactions involved. The goal was to use basic blackjack rules which the program follows and based off what type of cards the dealer or player has, it would decide on what to do. The program is designed to specifically work on https://games.washingtonpost.com/games/blackjack and not any other site. It's also not guarenteed you will win with this program as its all probability based and the dealer can use more then 1 set of cards which decreases chances of winning.

## Built With ⚒️

I used multiple libraries to build the projects
  -Pyautogui
  -Pytesseract
  -pynput
  -opencv-python
  -numpy
 
 ## Getting Started
 
The first thing you need to do is clone the repo and cd into the repository
 
```bash
 $ git clone https://github.com/JaJiang316/AutoBlackjack.git
 $ cd AutoBlackjack
```
After cloning the repository you will need to create a virtual environment you will go into your virtual environment and run the following command

```bash
 $ pip3 install -r requirements.txt
```
Next you will need to configure the program for your environment. Inside the main program you will find

```python
myScreenshot.save(
    r'C:\\Users\\Jason\Desktop\\Self Projects\\Screen Reader\\images\\screenshot_1.png')
```
You will need to update that your where your image folder is located on your computer without changes the png file. Do this everywhere you see this line of code. Next you will need to configure where the program needs to look to read the dealers and players hand. Find these lines of code in the main program and uncomment it

```python
# x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
```

You will need to find the top left corner of the dealers hand and players hand and change the values of the x,y,length,width of these two lines of code.
```python
Example: dealerHandimg = pyautogui.screenshot(region=(x, y, length, width))
```
```python
dealerHandimg = pyautogui.screenshot(region=(1014, 400, 76, 72))
```
```python                                
cardTotal = pyautogui.screenshot(region=(1012, 730, 77, 74))
```
After configuring these changes you can comment back the code for finding your mouse position and the program.
