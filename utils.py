import tkinter as tk
import tkinter.messagebox as messagebox
import random
import logging
import threading
import pyautogui
import time as t
from dataclasses import dataclass
from config import Settings


@dataclass
class Image:
    """
    Represents an image file used for screen detection.
    """
    path: str  # Path to the image file

    def find_image(self) -> bool:
        try:
            pyautogui.locateOnScreen(self.path, confidence=0.8, region=Settings.GAME_REGION)
            return True
        except pyautogui.ImageNotFoundException:
            return False


class TextHandler(logging.Handler):
    """
    Custom logging handler that outputs log records to a Tkinter Text widget.
    """

    def __init__(self, text_widget: tk.Text) -> None:
        super().__init__()
        self.text_widget = text_widget
        self.text_widget.tag_configure("INFO", foreground="lime")
        self.text_widget.tag_configure("WARNING", foreground="red")

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        tag = record.levelname

        def append() -> None:
            self.text_widget.configure(state='normal')
            self.text_widget.insert(tk.END, msg + '\n', (tag,))
            self.text_widget.configure(state='disabled')
            self.text_widget.yview(tk.END)

        self.text_widget.after(0, append)


def open_clicker(root: tk.Tk) -> None:
    """
    Starts the farming loop in a separate background thread.
    """

    def run_in_thread():
        try:
            tools = int(root.entry_tools.get()) + random.randint(10, 200)
            from engine import main
            main(tools)
        except ValueError:
            root.after(0, lambda: messagebox.showerror("Invalid Input", "Please enter a valid integer for tools!"))

    thread = threading.Thread(target=run_in_thread, daemon=True)
    thread.start()


def rand_click(coord: tuple) -> None:
    """
    Performs a random click within the specified coordinate bounds.
    """
    x = random.randint(coord[0], coord[1])
    y = random.randint(coord[2], coord[3])
    duration = random.uniform(0.5, 1) if coord == Settings.COORD[0] else random.uniform(0.2, 0.4)
    pyautogui.click(x, y, duration=duration, tween=pyautogui.linear)


def add_move() -> None:
    """
    Simulates human-like micro-movement of the mouse.
    """
    if random.random() < 0.3:
        pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10), duration=random.uniform(0.1, 0.2))
        if random.random() < 0.1:
            pyautogui.click()


def rand_event(number: int) -> None:
    """
    Simulates various human-like behaviors to avoid bot detection.
    Different actions are triggered based on the given number.
    """
    match number:
        case 1:
            pyautogui.moveRel(random.randint(-40, 40), random.randint(-40, 40), duration=random.uniform(0.1, 0.3))
            t.sleep(random.randint(1, 5))
        case 2:
            pyautogui.moveRel(random.randint(-40, 40), random.randint(-40, 40), duration=random.uniform(0.1, 0.3))
            t.sleep(random.randint(10, 20))
        case 3:
            pyautogui.moveTo(random.randint(10, 450), random.randint(300, 600),
                             duration=random.uniform(0.4, 1), tween=pyautogui.linear)
            t.sleep(random.uniform(1, 2))
        case 4:
            pyautogui.moveTo(random.randint(500, 1000), random.randint(400, 700),
                             duration=random.uniform(0.4, 1), tween=pyautogui.linear)
            t.sleep(random.uniform(1, 2))
        case 5:
            pyautogui.click(random.randint(0, 550), random.randint(210, 600),
                            clicks=random.randint(1, 4), interval=random.uniform(0.4, 1),
                            duration=random.uniform(0.4, 1), tween=pyautogui.linear)
            t.sleep(random.uniform(1, 2))
        case _:
            for _ in range(random.randint(1, 4)):
                pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10),
                                  duration=random.uniform(0.2, 0.4))
            t.sleep(random.uniform(1, 2))
