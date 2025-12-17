import random as rand
import pyautogui as pag


def rand_click(coord: tuple) -> None:

    x = rand.randint(coord[0], coord[1])
    y = rand.randint(coord[2], coord[3])
    pag.click(x, y, interval=rand.uniform(0.2, 0.7), duration=rand.uniform(0.4, 0.8), tween=pag.easeInOutCubic)
