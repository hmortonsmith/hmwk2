# generic aircraft class
# will have plane and helicopter subclasses

class Aircraft:

    def __init__(self, id):
        self.aircraft_id = int(id)


    def fly(self):
        return 'neeeeooooooooooowwww!'


