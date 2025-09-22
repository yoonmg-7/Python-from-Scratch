class Car:
    # class level attributes
    sterrringWheel = 1
    def __init__(self,name,wheels):
        self.name = name
        self.wheels = wheels

    def drive (self):
        print (f"{self.name} is driving........")

    # class level method
    @classmethod
    def common(cls):
        print(f"All car have only {cls.sterrringWheel} sterring wheells." )

# lambo = Car("lamboghini", 4)
# lambo.common()        # //All car have only 1 sterring wheells.
# lambo.drive()

# Suzuki = Car("Suzuki",4)
# Suzuki.drive()

# Car.common()            # //All car have only 1 sterring wheells.
