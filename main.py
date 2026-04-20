import func
import sys
import keyboard as key
import random as rand
import time as t

if __name__ == '__main__':

    while True:
        try:
            shovels = int(input("Введите количество лопат: ")) + rand.randint(0, 100)
            break
        except ValueError:
            print('Некорректный ввод, введите целое число')

    print('Для запуска скрипта нажмите "Enter"')
    print('Для завершения скрипта нажмите "Esc"')
    key.wait('enter', suppress=True)

    count = 0
    gamer = func.Game()
    gnomes = func.Image('image/gnomes.png')

    while count < shovels / 5:

        for i in gamer.coord:
            if rand.random() < 0.01:
                continue
            if key.is_pressed("esc"):
                print('Завершаю работу')
                sys.exit()
            if gnomes.find_image():
                gamer.rand_click(i)
                gamer.add_move()
            else:
                print("Не могу найти гномов, обновляю игру")
                t.sleep(rand.randint(2, 6))
                gamer.page_update()
                t.sleep(rand.randint(20, 40))

        gamer.rand_event(rand.randint(1, 10))
        gamer.rand_event(0)

        count += 1
        if count % 20 == 0:
            print(f'Потрачено {count * 5} лопат')

    gamer.rand_event(4)
    print('Лимит лопат на сегодня кончился')
