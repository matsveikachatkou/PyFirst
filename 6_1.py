import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        print(TrafficLight.__color[0])
        time.sleep(7)
        print(TrafficLight.__color[1])
        time.sleep(2)
        print(TrafficLight.__color[2])
        time.sleep(5)


example = TrafficLight()
example.running()
