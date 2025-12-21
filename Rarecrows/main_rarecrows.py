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

    count = 0
    ops = False
    while count <= set.shovels/5:

        func.first_click()

        for i in set.coord:
            try:
                func.find_image('image/ops.png', (0, 260, 480, 240))
                func.rand_click((30, 445, 445, 480))
                print('Обработка плохого интернет соединения')
                ops = True
                t.sleep(rand.randint(10, 20))
            except pyautogui.ImageNotFoundException:
                try:
                    func.find_image('image/load.png', (0, 260, 480, 240))
                    t.sleep(rand.randint(10, 20))
                except pyautogui.ImageNotFoundException:
                    if ops:
                        func.rand_click((425, 460, 630, 660))
                        t.sleep(rand.randint(3, 5))
                        func.rand_click((320, 365, 625, 670))
                        print('Выбрал редиску')
                        ops = False
                    if not ops:
                        try:
                            func.find_image('image/gnomes.png', (0, 310, 80, 150))
                            func.rand_click(i)
                            func.add_move()
                            if key.is_pressed("esc"):
                                sys.exit()
                        except pyautogui.ImageNotFoundException:
                            print("Не могу найти гномов")
                            t.sleep(rand.randint(30, 50))

        func.rand_event(rand.randint(1, 10))

        count += 1
        if count % 20 == 0:
            print(f'Потрачено {count*5} лопат')
