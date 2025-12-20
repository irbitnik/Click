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

        x = rand.randint(85, 140)
        y = rand.randint(195, 240)
        pyautogui.click(x, y, duration=rand.uniform(0.5, 1), tween=pyautogui.easeInOutCubic)

        for i in set.coord:  # TODO Оформить поиск картинок как функции
            try:
                pyautogui.locateOnScreen('image/ops.png', grayscale=True, confidence=0.8, region=(0, 260, 480, 240))
                func.rand_click((30, 445, 445, 480))
                print('Обработка плохого интернет соединения')
                ops = True
                t.sleep(rand.randint(10, 20))
            except pyautogui.ImageNotFoundException:
                try:
                    pyautogui.locateOnScreen('image/load.png', grayscale=True, confidence=0.8, region=(0, 260, 480, 240))
                    t.sleep(rand.randint(10, 20))
                except pyautogui.ImageNotFoundException:
                    if ops:
                        func.rand_click((425, 460, 630, 660))
                        t.sleep(rand.randint(3, 5))
                        func.rand_click((320, 365, 625, 670))
                        print('Снова выбрал редиску')
                        ops = False
                    if not ops:
                        try:
                            pyautogui.locateOnScreen('image/gnomes.png', grayscale=True, confidence=0.8, region=(0, 310, 80, 150))
                            func.rand_click(i)  # TODO Добавить "промахивание" мышкой по грядке
                            if key.is_pressed("esc"):
                                sys.exit()
                        except pyautogui.ImageNotFoundException:
                            print("Не могу найти гномов")
                            t.sleep(rand.randint(30, 50))
        func.rand_event(rand.randint(1, 10))
