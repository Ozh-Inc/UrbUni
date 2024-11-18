import threading
import time
import random


class Bank():
    __depstep = -1
    lock = None
    def __init__(self, balance: float, lock: threading.Lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            dep = random.randint(50, 500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print('-----------------------------------------------RELEASE')
            self.__depstep = i
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            wd = random.randint(50, 500)
            print(f'Запрос на {wd}')
            if self.balance >= wd:
                self.balance -= wd
                print(f'Снятие: {wd}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств ;)')
                self.lock.acquire()
                print(f'locked thread on step {i} ({self.__depstep})')
            time.sleep(0.001)


Oleg_Value = Bank(0, threading.Lock())

d = threading.Thread(target=Bank.deposit, args=(Oleg_Value,))
t = threading.Thread(target=Bank.take, args=(Oleg_Value,))
d.start()
d.join()
t.start()
t.join()

print(f'------------------------------Итоговый баланс: {Oleg_Value.balance}')