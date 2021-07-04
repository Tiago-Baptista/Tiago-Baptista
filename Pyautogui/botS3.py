import pyautogui
from time import sleep
from random import randint
pyautogui.press('winleft')
sleep(0.5)
pyautogui.press('down')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
for c in range(0, 10):
#fazer ataque
    pyautogui.press('F5')
    sleep(2)
    pyautogui.moveTo(x=809, y=1003)
    sleep(0.5)
    pyautogui.click()
    sleep(10)
#voltar ao contador
    pyautogui.moveTo(x=869, y=307)
    sleep(1)
    pyautogui.moveTo(x=871, y=377)
    sleep(0.5)
    pyautogui.click()
#esperar 4min a 5min
    x = randint(250, 300)
    sleep(x)
# abrir o browser
    pyautogui.press('winleft')
    sleep(0.5)
    pyautogui.press('down')
    sleep(0.5)
    pyautogui.press('right')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
