import func
import set
import sys
import pyautogui
import keyboard as key
import random as rand
import time as t


if __name__ == '__main__':
    print('Для запуска скрипта нажмите "Enter"')
    print('Для завершения скрипта нажмите "Esc"')
    key.wait('enter', suppress=True)
    ops = False
    while True:
        for i in set.coord:
            try:
                pyautogui.locateOnScreen('image/ops.png', confidence=0.8, region=(0, 260, 480, 240))
                x = rand.randint(30, 445)
                y = rand.randint(445, 480)
                pyautogui.click(x, y, duration=rand.uniform(0.2, 0.4), tween=pyautogui.easeInOutCubic)
                ops = True
                t.sleep(rand.randint(10, 20))
            except pyautogui.ImageNotFoundException:
                try:
                    pyautogui.locateOnScreen('image/load.png', confidence=0.8, region=(0, 260, 480, 240))
                    t.sleep(rand.randint(10, 20))
                except pyautogui.ImageNotFoundException:
                    if ops:
                        x = rand.randint(425, 460)
                        y = rand.randint(630, 660)
                        pyautogui.click(x, y, duration=rand.uniform(0.2, 0.4), tween=pyautogui.easeInOutCubic)
                        t.sleep(rand.randint(3, 5))
                        x = rand.randint(320, 365)
                        y = rand.randint(625, 670)
                        pyautogui.click(x, y, duration=rand.uniform(0.2, 0.4), tween=pyautogui.easeInOutCubic)
                        ops = False
                    if not ops:
                        func.rand_click(i)
                        if key.is_pressed("esc"):
                            sys.exit()
        t.sleep(rand.uniform(1, 3))


