class Car:
    __directions = ("forward","left","right")
    def __init__(self, speed, color, name, is_police):
        self._is_ride = False
        self._direction = 0
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        self._is_ride = True
        self._direction = 0
    def stop(self):
        self._is_ride = False
    def turn(self, direction):
        if (direction not in (1,2)):
            raise ValueError("Wrong turn direction")
        self._direction = direction
    def turnleft(self):
        self.turn(1)
    def turnright(self):
        self.turn(2)
    def show_speed(self):
        print(f"speed {self.speed if self._is_ride else 0}")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name, False)
    def show_speed(self):
        super(TownCar, self).show_speed()
        if (self._is_ride) and (60 < self.speed):
            print("speed exceed")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name, False)
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if (self._is_ride) and (40 < self.speed):
            print("speed exceed")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)

c1 = TownCar(40, "asd", "1")
c1.go()
c1.show_speed()
c2 = TownCar(70, "asd", "2")
c2.go()
c2.show_speed()
c3 = PoliceCar(90, "asd", "3")
c3.show_speed()
