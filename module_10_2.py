import threading
import time

class Knight(threading.Thread):
    enemies = 100
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        #global enemies
        days = 0
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.\n')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Pascalus', 13)
second_knight = Knight('Sir Merde', 7)
first_knight.start()
second_knight.start()