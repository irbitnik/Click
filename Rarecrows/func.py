import random as rand
import pyautogui as pag
import time as t


# TODO Обернуть в класс


class Image:

    def __init__(self, path: str, region: tuple):
        self.path = path
        self.region = region

    def find_image(self) -> None:
        pag.locateOnScreen(self.path, grayscale=True, confidence=0.8, region=self.region)


class MouseControl:
    @staticmethod
    def first_click() -> None:
        x = rand.randint(85, 140)
        y = rand.randint(195, 240)
        pag.click(x, y, duration=rand.uniform(0.5, 1), tween=pag.easeInOutCubic)

    @staticmethod
    def rand_click(coord: tuple) -> None:
        x = rand.randint(coord[0], coord[1])
        y = rand.randint(coord[2], coord[3])
        pag.click(x, y, duration=rand.uniform(0.1, 0.3), tween=pag.easeInOutCubic)

    @staticmethod
    def add_move() -> None:
        if rand.random() < 0.1:
            pag.moveRel(rand.randint(-10, 10), rand.randint(-10, 10), duration=rand.uniform(0.1, 0.2))
            if rand.random() < 0.2:
                pag.click()

    @staticmethod
    def rand_event(number: int) -> None:
        match number:
            case 1:
                pag.moveRel(rand.randint(-40, 40), rand.randint(-40, 40), duration=rand.uniform(0.1, 0.3))
                t.sleep(rand.randint(1, 5))
            case 2:
                pag.moveRel(rand.randint(-40, 40), rand.randint(-40, 40), duration=rand.uniform(0.1, 0.3))
                t.sleep(rand.randint(10, 20))
            case 3:
                pag.moveTo(rand.randint(10, 450), rand.randint(300, 600), duration=rand.uniform(0.4, 1),
                           tween=pag.easeInOutCubic)
                t.sleep(rand.uniform(1, 2))
            case 4:
                pag.moveTo(rand.randint(500, 1000), rand.randint(400, 700), duration=rand.uniform(0.4, 1),
                           tween=pag.easeInOutCubic)
                t.sleep(rand.uniform(1, 2))
            case 5:
                pag.click(rand.randint(500, 800), rand.randint(200, 700), clicks=rand.randint(1, 4),
                          interval=rand.uniform(0.4, 1),
                          duration=rand.uniform(0.4, 1), tween=pag.easeInOutCubic)
                t.sleep(rand.uniform(1, 2))
            case _:
                for _ in range(rand.randint(1, 4)):
                    pag.moveRel(rand.randint(-10, 10), rand.randint(-10, 10), duration=rand.uniform(0.2, 0.4))
                t.sleep(rand.uniform(1, 2))
