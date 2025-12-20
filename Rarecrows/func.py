import random as rand
import pyautogui as pag
import time as t


def rand_click(coord: tuple) -> None:  # TODO Обернуть в класс

    x = rand.randint(coord[0], coord[1])
    y = rand.randint(coord[2], coord[3])
    pag.click(x, y, duration=rand.uniform(0.2, 0.4), tween=pag.easeInOutCubic) # TODO Добавить еще один клик с небольшим смещением


def rand_event(number):
    match number:
        case 1:
            pag.moveRel(rand.randint(-40, 40), rand.randint(-40, 40), duration=rand.uniform(0.2, 0.4))
            t.sleep(rand.randint(1, 5))
        case 2:
            pag.moveRel(rand.randint(-40, 40), rand.randint(-40, 40), duration=rand.uniform(0.2, 0.4))
            t.sleep(rand.randint(10, 20))
        case 3:
            pag.moveTo(rand.randint(10, 450), rand.randint(300, 600), duration=rand.uniform(1, 3), tween=pag.easeInOutCubic)
        case 4:
            pag.moveTo(rand.randint(10, 1000), rand.randint(400, 750), duration=rand.uniform(1, 3), tween=pag.easeInOutCubic)
        case 5:
            pag.click(rand.randint(500, 800), rand.randint(200, 700), clicks=rand.randint(1, 4), interval=rand.uniform(0.4, 1),
                      duration=rand.uniform(1, 3), tween=pag.easeInOutCubic)
        case _:
            pag.moveRel(rand.randint(-10, 10), rand.randint(-40, 40), duration=rand.uniform(0.2, 0.4))
            pag.moveRel(rand.randint(-10, 10), rand.randint(-40, 40), duration=rand.uniform(0.2, 0.4))
            pag.moveRel(rand.randint(-10, 10), rand.randint(-40, 40), duration=rand.uniform(0.2, 0.4))
            t.sleep(rand.uniform(1, 2))
