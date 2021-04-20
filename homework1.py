from time import sleep

class TrafficLight:
    __color = ['Rad', 'Yellow', 'Green']

    def switching(self):
        i = 0
        while i < 3:
            print(f'Traffic light switches: {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
traffic = TrafficLight()
traffic.switching()
