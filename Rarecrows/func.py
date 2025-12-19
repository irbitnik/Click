import random as rand
import pyautogui as pag


def rand_click(coord: tuple) -> None:  # TODO Обернуть в класс

    x = rand.randint(coord[0], coord[1])
    y = rand.randint(coord[2], coord[3])
    pag.click(x, y, duration=rand.uniform(0.2, 0.4), tween=pag.easeInOutCubic)
