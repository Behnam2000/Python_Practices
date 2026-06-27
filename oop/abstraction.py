from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    
    def go(self):
        print('driving the car')

    def stop(self):
        print('Stopig the car')

c1 = Car()

c1.go()

