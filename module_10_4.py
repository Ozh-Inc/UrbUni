import threading
import queue
import time
import random

class Guest(threading.Thread):
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self.thread = None
        self.name = name
    def run(self):
        time.sleep(random.randint(3, 10))

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None



class Cafe:
    def __init__(self, tables: list, q:queue.Queue = queue.Queue()):
        self.tt = []
        self.q = q
        self.tables = tables
    def guest_arrival(self, *guests:Guest):
        for g in guests:
            seated = False
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    g.thread = threading.Thread(target=g.run, daemon=True)
                    g.thread.start()
                    self.tt.append(t)
                    seated = True
                    print(f'{g.name} сел(-а) за стол номер {t.number}')
                    break
            if not seated:
                self.q.put(g)
                print(f'{g.name} в очереди')
    def serve_guests(self):
        while not self.q.empty() and len(self.tt) > 0:
            for ti in range(len(self.tt)):
                if not self.tt[ti].guest.thread.is_alive():
                    print(f'{self.tt[ti].guest.name} покушал(-а) и ушёл(ушла)')
                    self.tt[ti].guest = None
                    self.tt.pop(ti)
                    print(f'Стол номер {self.tt[ti].number} свободен')
                    if not self.q.empty():
                        self.tt[ti].guest = self.q.get()
                        print(f'{self.tt[ti].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tt[ti].number}')
                        self.tt[ti].guest.thread = threading.Thread(target=self.tt[ti].guest.run, daemon=True )
                        self.tt[ti].guest.thread.start()
                        self.tt.append(self.tt[ti])


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.serve_guests()