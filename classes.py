#b
# class Java:
#     pass
#c
# class Transport:
#     def __init__(self, max_vel, distance):
#         self.vel = max_vel
#         self.dis = distance
#     def display(self):
#         print("Max velocity is ", self.vel, ", the distance is", self.dis)
# parameters = Transport(180, 1000)
# parameters.display()
#d
class Transport:
    def __init__(self, max_vel, distance):
        self.vel = max_vel
        self.dis = distance
    def writevelocity(self):
        print("velocity is: ", self.vel * 1.5)
    def writedistance(self):
        print("distance is: ", self.dis - self.dis * 0.2)

class YengilAvto(Transport):
    def __init__(self, max_vel, distance):
        self.vel = max_vel
        self.dis = distance

car = YengilAvto(120, 500)
car.writevelocity()
car.writedistance()  