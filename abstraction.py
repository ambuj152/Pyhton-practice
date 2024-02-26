class Car:
    def __init__(self):
        self.accelarator=False
        self.clutch=False
        self.brake=False
    def Start(self):
        self.accelarator=True
        self.cluth=True
        print("my Car is Started")
car=Car()
car.Start()

      
