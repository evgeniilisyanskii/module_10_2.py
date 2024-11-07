from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemies):
            if enemies > 0:
                time.sleep(1)
                day += 1
                enemies -= self.power
                print(f'{self.name} сражается {day}-й день, осталось {enemies} врагов.')
                if enemies <= 0:
                    print(f'{self.name} одержал победу спустя {day} дней!')


first_knight = Knight('Илья Муромец', 10)
second_knight = Knight('Добрыня Никитич', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все сражения закончены!")