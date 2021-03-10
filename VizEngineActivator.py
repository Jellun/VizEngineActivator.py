import pyautogui
import time
x = 1
while True:
    try:
        time.sleep(10)
        if x % 2 == 0:
            vizEng01Location = pyautogui.locateOnScreen('Eng01.PNG', grayscale=True)
            if vizEng01Location == None:
                vizEng01Location = pyautogui.locateOnScreen('Eng01A.PNG', grayscale=True)
            eng01x, eng01y = pyautogui.center(vizEng01Location)
            pyautogui.click(eng01x, eng01y)
            pyautogui.press('enter', interval=0.1)
            pyautogui.typewrite('version', interval=0.05)
            pyautogui.press('enter', interval=0.1)
        else:
            vizEng02Location = pyautogui.locateOnScreen('Eng02.PNG', grayscale=True)
            if vizEng02Location == None:
                vizEng02Location = pyautogui.locateOnScreen('Eng02A.PNG', grayscale=True)
            eng02x, eng02y = pyautogui.center(vizEng02Location)
            pyautogui.click(eng02x, eng02y)
            pyautogui.press('enter', interval=0.1)
            pyautogui.typewrite('version', interval=0.05)
            pyautogui.press('enter', interval=0.1)
        x += 1
    except Exception as e:
        print("Error: " + str(e))
