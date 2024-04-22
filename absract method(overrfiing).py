from abc import ABC,abstractmethod
class Car(ABC):
    def mileage(self):
        pass
    def bitm_mileage(self):
        print("abs method")
        
class tesla(Car):
    def mileage(self):
        print("abs method with spedd 30kmph")
        
class BMW (Car):
    def mileage(self):
        print("abs method with speed 35kmph")
        
class suzuki(Car):
    def mileage(self):
        print("abs method with speed 25kmph")
        
t=tesla()
t.mileage()

b=BMW()
b.mileage()

s=suzuki()
s.mileage()