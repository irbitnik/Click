from config import Settings
from utils import Image, rand_click, add_move, rand_event
import random
import keyboard as key
import logging
import sys
import time as t

logger = logging.getLogger(__name__)


def main(tools: int):
    count = 0
    work_image = Image('image/work_image.png')
    logger.info(f'Farming starts at {tools} tools')

    while count < tools / 5:
        for coord in Settings.COORD:
            if random.random() < 0.01:
                continue
            if key.is_pressed("esc"):
                logger.warning('FATALITY')
                sys.exit()
            if work_image.find_image():
                rand_click(coord)
                add_move()
            else:
                logger.warning("Can't find the image, updating the game")
                t.sleep(random.randint(2, 6))
                rand_click(Settings.GAME_UPDATE)
                t.sleep(random.randint(20, 40))

        rand_event(random.randint(1, 10))
        rand_event(0)

        count += 1

    rand_event(4)
    logger.info('Tools limit reached for today')
