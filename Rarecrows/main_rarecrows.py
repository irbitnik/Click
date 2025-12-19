import func
import set
import sys
import pyautogui
import keyboard as key
import random as rand
import time as t


if __name__ == '__main__':  # TODO Сделать десктопным
    print('Для запуска скрипта нажмите "Enter"')  # TODO Несколько потоков
    print('Для завершения скрипта нажмите "Esc"')
    key.wait('enter', suppress=True)
    ops = False
    while True:
        for i in set.coord:
            try:
                pyautogui.locateOnScreen('image/ops.png', confidence=0.8, region=(0, 260, 480, 240))
                x = rand.randint(30, 445)  # TODO Оформить поиск картинок как функции
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
                        try:
                            pyautogui.locateOnScreen('image/gnomes.png', confidence=0.8, region=(0, 310, 80, 150))
                            func.rand_click(i)  # TODO Добавить "промахивание" мышкой по грядке
                            if key.is_pressed("esc"):
                                sys.exit()
                        except pyautogui.ImageNotFoundException:
                            key.wait('enter', suppress=True)
        t.sleep(rand.uniform(1, 3))  # TODO Добавить случайные события
