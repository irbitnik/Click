from gui import create_gui
from utils import TextHandler
import logging

if __name__ == '__main__':
    root = create_gui()

    text_handler = TextHandler(root.log_text)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    text_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(text_handler)
    logger.setLevel(logging.INFO)

    root.mainloop()
