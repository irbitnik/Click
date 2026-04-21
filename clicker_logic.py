from config import Settings
from utils import Image, rand_click, add_move, rand_event
import random as rand
import keyboard as key
import sys
import time as t


def main(shovels: int):
    count = 0

    gnomes = Image('image/gnomes.png')

    while count < shovels / 5:

        for i in Settings.COORD:
            if rand.random() < 0.01:
                continue
            if key.is_pressed("esc"):
                print('FATALITY')
                sys.exit()
            if gnomes.find_image():
                rand_click(i)
                add_move()
            else:
                print("Can't find the gnomes, updating the game")
                t.sleep(rand.randint(2, 6))
                rand_click(Settings.GAME_UPDATE)
                t.sleep(rand.randint(20, 40))

        rand_event(rand.randint(1, 10))
        rand_event(0)

        count += 1
        if count % 20 == 0:
            print(f'{count * 5} shovels wasted')

    rand_event(4)
    print('Shovel limit reached for today')