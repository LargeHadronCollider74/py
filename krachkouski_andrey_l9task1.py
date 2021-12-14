import datetime

class TrafficLight:
    __states = ("red", "yellow", "green")
    __delays = (7, 2, 10)
    def __init__(self):
        self.state = 0
        self.lastupdate = datetime.datetime.now()
    def update(self):
        delay =  (datetime.datetime.now() - self.lastupdate).seconds
        while 0 < delay:
            if (delay > TrafficLight.__delays[self.state]):
                delay = delay - TrafficLight.__delays[self.state]
                self.lastupdate = self.lastupdate + datetime.timedelta(0, TrafficLight.__delays[self.state])
                self.state = (self.state + 1) % len(TrafficLight.__states)
            else:
                break
    def __str__(self):
        self.update()
        return TrafficLight.__states[self.state]


x = TrafficLight()
while True:
    print(f"light: {x}")
    print("input any for update")
    try:
        input()
    except KeyboardInterrupt:
        break
