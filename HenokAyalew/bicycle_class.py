#Create a Bicycle class with attributes model, speed, 
#serial number and method ChangeSpeed(newSpeed) and Brake()
#then create a list of 6 Bikes accelerate them to odd number of speed (1,3,5,7 or simiar)
#print their status to the console and then apply the brakes for all of them and
#print the status once more to the console



class Bicycle:

    def __init__(self, model,speed,serial_number):
        self.model = model
        self.speed = speed
        self.serial_number = serial_number

    def display_status(self):  
        print("=====Bicycle=====")
        print("=>Model:",self.model)
        print("=>speed:",self.speed)
        print("=>serial num:",self.serial_number)

    def change_speed(self, new_speed):
        self.speed = new_speed




bike1 = Bicycle("Road bike", 3, 93849392)
print("====================")
bike2 = Bicycle("Mountain bike", 6, 283749502)
print("====================")
bike3 = Bicycle("Touring bike", 2, 293485024)
print("====================")
bike4 = Bicycle("Folding bike", 5, 209395023)
print("====================")
bike5 = Bicycle("BMX", 9, 293001934)
print("====================")
bike6 = Bicycle("Cruser", 4, 139384573)


bike1.change_speed(1)
bike2.change_speed(3)
bike3.change_speed(5)
bike4.change_speed(7)
bike5.change_speed(9)
bike6.change_speed(11)


bike1.display_status()
bike2.display_status()
bike3.display_status()
bike4.display_status()
bike5.display_status()
bike6.display_status()