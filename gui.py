import tkinter as tk

def start_script():
    global shovels
    try:
        value = int(entry_shovels.get())  # Считываем значение из поля
        shovels = value
        print(f"Количество лопат обновлено: {shovels}")  # Можно заменить на реальный код запуска
        # Здесь можно вызвать основную функцию бота, например: run_bot()
    except ValueError:
        print("Ошибка: введите целое число!")

root = tk.Tk()
root.title("Кликер")
root.geometry("300x200")
root.configure(bg="#2e2e2e")

label = tk.Label(
    root,
    text="Введите количество лопат:",
    font=("Arial", 12),
    bg="#2e2e2e",
    fg="white"
)
label.pack(pady=10)

entry_shovels = tk.Entry(
    root,
    font=("Arial", 14),
    width=15,
    justify='center'  # Текст по центру
)
entry_shovels.insert(0, str(3000))
entry_shovels.pack(pady=10)

button_start = tk.Button(
    root,
    text="Старт",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    command=start_script
)
button_start.pack(pady=20)

shovels = int(entry_shovels.get())
print(type(shovels))
root.mainloop()


