class Horse:
    def __init__(self, x_distance = 0, sound = 'HS'):
        self.x_distance = x_distance
        self.sound = sound
    def run(self, dx: int):
        self.x_distance += dx

#H1 = Horse()
#print(H1.run(15))

class Eagle:
    def __init__(self, y_distance = 0, sound='ES'):
        self.y_distance = y_distance
        self.sound = sound
    def fly(self, dy: int):
        self.y_distance += dy
        return self.y_distance

#E1 = Eagle()
#print(E1.fly(17))

class Pegasus(Horse, Eagle):
    def __init__(self):
        #for c in Pegasus.mro()[1:]: # Шизокодинг
        #    c.__init__(self)
        Horse.__init__(self)
        Eagle.__init__(self)
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)
    def voice(self):
        print(self.sound)

print(Pegasus.mro())

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()