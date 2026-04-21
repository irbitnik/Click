import tkinter as tk


def open_clicker(root):

    while True:
        try:
            shovels = int(root.entry_shovels.get())
            print(f'Farming starts at {shovels} shovels')
            break
        except ValueError:
            print("Error: Please enter an integer!")

    from clicker_logic import main
    main(shovels)


def create_gui():

    root = tk.Tk()
    root.title("Clicker")
    root.geometry("300x200")
    root.configure(bg="#2e2e2e")

    frame_input = tk.Frame(root, bg="#2e2e2e")
    frame_input.pack(pady=10)

    label = tk.Label(
        frame_input,
        text="Shovels :",
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
        root,
        text="Run, Forest",
        font=("Arial", 12),
        bg="#4CAF50",
        fg="white",
        command=open_clicker
    )
    button_start.pack(pady=10)

    label = tk.Label(
        root,
        text="Press 'Esc' to stop the script",
        font=("Arial", 12),
        bg="#2e2e2e",
        fg="white"
    )
    label.pack(pady=10)
    return root


