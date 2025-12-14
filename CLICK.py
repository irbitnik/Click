import keyboard
import mouse
import time
import random

work = int(input('Work second = '))
amount = int(input('Amount = '))
clicking = False
count = 0
collect = 5


def set_clicker():
    global clicking
    if clicking:
        clicking = False
        print('Кликер отключен')
    else:
        clicking = True
        print('Кликер включен')


keyboard.add_hotkey('Enter', set_clicker)


while count < amount:
    if clicking:
        mouse.click('left')
        time.sleep(work + random.randint(0,10))
        mouse.click('left')
        time.sleep(collect + random.randint(0,10))
        count += 1
