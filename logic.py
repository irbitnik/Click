print('Для запуска скрипта нажмите "Enter"')
print('Для завершения скрипта нажмите "Esc"')
key.wait('enter', suppress=True)

count = 0
gamer = func.Game()
gnomes = func.Image('image/gnomes.png')

while count < settings.shovels / 5:

    for i in settings.coord:
        if rand.random() < 0.01:
            continue
        if key.is_pressed("esc"):
            print('Завершаю работу')
            sys.exit()
        if gnomes.find_image():
            gamer.rand_click(i)
            gamer.add_move()
        else:
            print("Не могу найти гномов, обновляю игру")
            t.sleep(rand.randint(2, 6))
            gamer.page_update()
            t.sleep(rand.randint(20, 40))

    gamer.rand_event(rand.randint(1, 10))
    gamer.rand_event(0)

    count += 1
    if count % 20 == 0:
        print(f'Потрачено {count * 5} лопат')

gamer.rand_event(4)
print('Лимит лопат на сегодня кончился')