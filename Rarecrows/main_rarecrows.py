import func
import set
import keyboard as key
import random as rand
import time as t


if __name__ == '__main__':
    print('Для запуска скрипта нажмите "Enter"')
    key.wait('enter', suppress=True)
    while True:
        for i in set.coord:
            func.rand_click(i)
        t.sleep(rand.randint(5, 10))


