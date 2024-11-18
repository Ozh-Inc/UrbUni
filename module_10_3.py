import threading
import time
import random


class Bank():
    lock = None
    def __init__(self, balance: float, lock: threading.Lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            dep = random.randint(50, 500)
            if not self.lock.locked():
                self.lock.acquire()
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            wd = random.randint(50, 500)
            print(f'Запрос на {wd}')
            if not self.lock.locked():
                self.lock.acquire()
            if self.balance >= wd:
                self.balance -= wd
                print(f'Снятие: {wd}. Баланс: {self.balance}')
                time.sleep(0.001)
            elif self.lock.locked():
                print('Запрос отклонён, недостаточно средств ;)')
                self.lock.release()
                time.sleep(0.001)


Oleg_Value = Bank(0, threading.Lock())

d = threading.Thread(target=Bank.deposit, args=(Oleg_Value,))
t = threading.Thread(target=Bank.take, args=(Oleg_Value,))
d.start()
t.start()
d.join()
t.join()

print(f'Итоговый баланс: {Oleg_Value.balance}')