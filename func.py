from dataclasses import dataclass
from typing import Optional, Tuple
import random as rand
import pyautogui
import time as t


class Settings:
    game_region = (0, 85, 680, 635)  # Регион игрового поля: X и Y верхнего левого угла, ширина и высота
    game_update = (50, 70, 50, 70)  # (x1, x2, y1, y2) Координаты обновления веб версии игры
    coord = ((180, 240, 210, 270),  # (x1, x2, y1, y2) Координаты грядок
             (270, 320, 210, 270),
             (350, 410, 210, 270),
             (440, 490, 210, 270),

             (440, 490, 295, 350),
             (350, 410, 295, 350),
             (270, 320, 295, 350),
             (180, 240, 295, 350),

             (180, 240, 380, 435),
             (270, 320, 380, 435),
             (350, 410, 380, 435),
             (440, 490, 380, 435),

             (440, 490, 465, 520),
             (350, 410, 465, 520),
             (270, 320, 465, 520),
             (180, 240, 465, 520),

             (180, 240, 550, 600),
             (270, 320, 550, 600),
             (350, 410, 550, 600),
             (440, 490, 550, 600))


@dataclass
class Image(Settings):
    path: str  # Путь к файлу
    click: Optional[Tuple[int, int, int, int]] = None  # Область для клика (x1, x2, y1, y2)

    def find_image(self) -> bool:
        try:
            pyautogui.locateOnScreen(self.path,
                                     confidence=0.8,
                                     region=self.game_region)
            return True
        except pyautogui.ImageNotFoundException:
            return False


class Game(Settings):

    def rand_click(self, coord: tuple) -> None:
        x = rand.randint(coord[0], coord[1])
        y = rand.randint(coord[2], coord[3])
        if coord == self.coord[0]:
            pyautogui.click(x, y,
                            duration=rand.uniform(0.5, 1),
                            tween=pyautogui.linear)
        else:
            pyautogui.click(x, y,
                            duration=rand.uniform(0.2, 0.4),
                            tween=pyautogui.linear)

    @staticmethod
    def add_move() -> None:
        if rand.random() < 0.3:
            pyautogui.moveRel(rand.randint(-10, 10),
                              rand.randint(-10, 10),
                              duration=rand.uniform(0.1, 0.2))
            if rand.random() < 0.1:
                pyautogui.click()

    @staticmethod
    def rand_event(number: int) -> None:
        match number:
            case 1:
                pyautogui.moveRel(rand.randint(-40, 40),
                                  rand.randint(-40, 40),
                                  duration=rand.uniform(0.1, 0.3))
                t.sleep(rand.randint(1, 5))
            case 2:
                pyautogui.moveRel(rand.randint(-40, 40),
                                  rand.randint(-40, 40),
                                  duration=rand.uniform(0.1, 0.3))
                t.sleep(rand.randint(10, 20))
            case 3:
                pyautogui.moveTo(rand.randint(10, 450),
                                 rand.randint(300, 600),
                                 duration=rand.uniform(0.4, 1),
                                 tween=pyautogui.linear)
                t.sleep(rand.uniform(1, 2))
            case 4:
                pyautogui.moveTo(rand.randint(500, 1000),
                                 rand.randint(400, 700),
                                 duration=rand.uniform(0.4, 1),
                                 tween=pyautogui.linear)
                t.sleep(rand.uniform(1, 2))
            case 5:
                pyautogui.click(rand.randint(0, 550),
                                rand.randint(210, 650),
                                clicks=rand.randint(1, 4),
                                interval=rand.uniform(0.4, 1),
                                duration=rand.uniform(0.4, 1),
                                tween=pyautogui.linear)
                t.sleep(rand.uniform(1, 2))

            case _:
                for _ in range(rand.randint(1, 4)):
                    pyautogui.moveRel(rand.randint(-10, 10),
                                      rand.randint(-10, 10),
                                      duration=rand.uniform(0.2, 0.4))
                t.sleep(rand.uniform(1, 2))

    def page_update(self):
        self.rand_click(self.game_update)
