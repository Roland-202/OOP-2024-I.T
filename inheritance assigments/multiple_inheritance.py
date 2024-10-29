class Camera:
    def take_photo(self):
        print("Taking a photo...")

class Phone:
    def make_call(self):
        print("Making a phone call...")

class Smartphone(Camera, Phone):
    pass
smartphone = Smartphone()
smartphone.take_photo()
smartphone.make_call()