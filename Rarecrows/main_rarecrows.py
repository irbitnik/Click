from func import Image, MouseControl
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

    count = 0
    mouse = MouseControl()
    img_ops = Image('image/ops.png', (0, 260, 480, 240))
    img_load = Image('image/load.png', (0, 260, 480, 240))
    img_gnomes = Image('image/gnomes.png', (0, 310, 80, 150))
    img_help = Image('image/help.png', (0, 260, 480, 100))
    flag_ops = False

    while count < set.shovels / 5:

        for i in set.coord:
            try:
                img_help.find_image()
                mouse.rand_click((30, 45, 270, 290))
                print('Обработка хелпа')
                t.sleep(rand.randint(2, 4))
            except pyautogui.ImageNotFoundException:
                try:
                    img_ops.find_image()
                    mouse.rand_click((30, 445, 445, 480))
                    print('Обработка плохого интернет соединения')
                    flag_ops = True
                    t.sleep(rand.randint(10, 20))
                except pyautogui.ImageNotFoundException:
                    try:
                        img_load.find_image()
                        t.sleep(rand.randint(10, 20))
                    except pyautogui.ImageNotFoundException:
                        if flag_ops:
                            mouse.rand_click((425, 460, 630, 660))
                            t.sleep(rand.randint(3, 5))
                            mouse.rand_click((320, 365, 625, 670))
                            print('Выбрал редиску')
                            flag_ops = False
                        if not flag_ops:
                            try:
                                if rand.random() < 0.03:
                                    continue
                                if key.is_pressed("esc"):
                                    sys.exit()
                                img_gnomes.find_image()
                                mouse.rand_click(i)
                                mouse.add_move()
                            except pyautogui.ImageNotFoundException:
                                print("Не могу найти гномов")
                                t.sleep(rand.randint(30, 50))

        mouse.rand_event(rand.randint(1, 10))
        mouse.rand_event(0)

        count += 1
        if count % 20 == 0:
            print(f'Потрачено {count * 5} лопат')

    mouse.rand_event(4)
    print('Лимит лопат на сегодня кончился')
