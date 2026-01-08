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
    ops = Image('image/ops.png', (30, 445, 445, 480))
    helping = Image('image/helping.png', (30, 45, 270, 290))
    anons = Image('image/anons.png', (430, 455, 175, 205))
    gnomes = Image('image/gnomes.png')

    while count < set.shovels / 5:

        for i in set.coord:
            if rand.random() < 0.01:
                continue
            if key.is_pressed("esc"):
                sys.exit()
            if anons.find_image():
                mouse.rand_click(anons.click)
                print('Обработка анонса')
                t.sleep(rand.randint(2, 4))
            if helping.find_image():
                mouse.rand_click(helping.click)
                print('Обработка хелпа')
                t.sleep(rand.randint(2, 4))
            if ops.find_image():
                mouse.rand_click(ops.click)
                print('Обработка плохого интернет соединения')
                t.sleep(rand.randint(10, 20))
            if gnomes.find_image():
                mouse.rand_click(i)
                mouse.add_move()
            else:
                print("Не могу найти гномов")
                t.sleep(rand.randint(30, 50))

        mouse.rand_event(rand.randint(1, 10))
        mouse.rand_event(0)

        count += 1
        if count % 20 == 0:
            print(f'Потрачено {count * 5} лопат')

    mouse.rand_event(4)
    print('Лимит лопат на сегодня кончился')
