from config import Settings
from utils import Image, rand_click, add_move, rand_event
import random as rand
import keyboard as key
import logging
import sys
import time as t

logger = logging.getLogger(__name__)


def main(shovels: int):

    count = 0
    gnomes = Image('image/gnomes.png')
    logger.info(f'Farming starts at {shovels} shovels')

    while count < shovels / 5:

        for i in Settings.COORD:
            if rand.random() < 0.01:
                continue
            if key.is_pressed("esc"):
                logger.warning('FATALITY')
                sys.exit()
            if gnomes.find_image():
                rand_click(i)
                add_move()
            else:
                logger.warning("Can't find the gnomes, updating the game")
                t.sleep(rand.randint(2, 6))
                rand_click(Settings.GAME_UPDATE)
                t.sleep(rand.randint(20, 40))

        rand_event(rand.randint(1, 10))
        rand_event(0)

        count += 1
        if count % 20 == 0:
            logger.info(f'{count * 5} shovels wasted')

    rand_event(4)
    logger.info('Shovel limit reached for today')
