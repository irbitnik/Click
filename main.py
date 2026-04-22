import logging
from gui import create_gui


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-6s | %(name)s | %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == '__main__':

    root = create_gui()
    root.mainloop()
