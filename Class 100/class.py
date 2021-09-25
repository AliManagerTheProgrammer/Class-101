class Car(object):
    def __init__(self,model,company,color,speedLimit):
        self.color = color
        self.company = company
        self.model = model
        self.speedLimit = speedLimit
    def  start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerated")

lamborghini = Car("huracan EVO", "lamborghini", "green", "250")
lamborghini.start  