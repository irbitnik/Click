import tkinter as tk
import tkinter.messagebox as messagebox
import random
import logging
from typing import Any


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
    Callback for the 'Run' button.
    """
    try:
        shovels = int(root.entry_shovels.get()) + random.randint(10, 200)
        from engine import main
        main(shovels)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for shovels!")


def create_gui() -> tk.Tk:
    """
    Creates the main GUI window with two sections:
    - Left: Controls (input field and start button)
    - Right: Log output area
    """
    root = tk.Tk()
    root.title("Clicker")
    root.geometry("700x500")
    root.configure(bg="#2e2e2e")

    # === LEFT PANEL: Settings ===
    left_frame = tk.Frame(root, bg="#2e2e2e")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor="nw")

    frame_input = tk.Frame(left_frame, bg="#2e2e2e")
    frame_input.pack(pady=10)

    label = tk.Label(
        frame_input,
        text="Shovels:",
        font=("Arial", 12),
        bg="#2e2e2e",
        fg="white"
    )
    label.grid(row=0, column=0, padx=(0, 10), sticky="w")

    entry_shovels = tk.Entry(
        frame_input,
        font=("Arial", 14),
        width=7,
        justify='center'
    )
    entry_shovels.insert(0, str(3000))
    entry_shovels.grid(row=0, column=1, sticky="e")
    root.entry_shovels = entry_shovels

    button_start = tk.Button(
        left_frame,
        text="Run, Forest",
        font=("Arial", 12),
        bg="#4CAF50",
        fg="white",
        command=lambda: open_clicker(root)
    )
    button_start.pack(pady=10)

    label_info = tk.Label(
        left_frame,
        text="Press 'Esc' to stop the script",
        font=("Arial", 12),
        bg="#2e2e2e",
        fg="white"
    )
    label_info.pack(pady=10)

    # === RIGHT PANEL: Logs ===
    right_frame = tk.Frame(root, bg="#2e2e2e")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

    log_label = tk.Label(
        right_frame,
        text="Logs:",
        font=("Arial", 12, "bold"),
        bg="#2e2e2e",
        fg="white"
    )
    log_label.pack(anchor="nw")

    log_text = tk.Text(
        right_frame,
        state='disabled',
        bg="#1e1e1e",
        fg="lime",
        font=("Consolas", 10),
        wrap=tk.WORD
    )
    log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

    # Scrollbar for log text
    scrollbar = tk.Scrollbar(log_text)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    log_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=log_text.yview)

    root.log_text = log_text

    # === SET UP LOGGING TO TEXT WIDGET ===
    text_handler = TextHandler(log_text)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-6s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    text_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(text_handler)
    logger.setLevel(logging.INFO)

    return root
