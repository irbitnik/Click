from func import Image, MouseControl
import set
import sys
import keyboard as key
import random as rand
import time as t

if __name__ == '__main__':

    print('Для запуска скрипта нажмите "Enter"')
    print('Для завершения скрипта нажмите "Esc"')
    key.wait('enter', suppress=True)

    count = 0
    mouse = MouseControl()
    ops = Image('image/ops.png', (50, 500, 465, 500))
    anons = Image('image/anons.png', (480, 520, 200, 240))
    gnomes = Image('image/gnomes.png')

    while count < set.shovels / 5:

        for i in set.coord:
            if rand.random() < 0.01:
                continue
            if key.is_pressed("esc"):
                sys.exit()
            if anons.find_image():
                t.sleep(rand.randint(2, 6))
                mouse.rand_click(anons.click)
                t.sleep(rand.randint(20, 40))
                print('Обработка анонса')
            if ops.find_image():
                t.sleep(rand.randint(2, 6))
                mouse.rand_click(ops.click)
                t.sleep(rand.randint(20, 40))
                print('Обработка плохого интернет соединения')
            if gnomes.find_image():
                mouse.rand_click(i)
                mouse.add_move()
            else:
                print("Не могу найти гномов, обновляю игру")
                mouse.rand_click(set.game_update_1)
                t.sleep(rand.randint(2, 6))
                mouse.rand_click(set.game_update_2)
                t.sleep(rand.randint(30, 50))

        mouse.rand_event(rand.randint(1, 10))
        mouse.rand_event(0)

        count += 1
        if count % 20 == 0:
            print(f'Потрачено {count * 5} лопат')

    mouse.rand_event(4)
    print('Лимит лопат на сегодня кончился')
