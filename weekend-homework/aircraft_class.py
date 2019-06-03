# generic aircraft class
# will have plane and helicopter subclasses

class Aircraft:

    def __init__(self, id):
        self.aircraft_id = int(id)
        self.description = ''

    def fly(self):
        return 'neeeeooooooooooowwww!'


class Aeroplane(Aircraft):

    def __init__(self, id, capacity, manufacturer='', operator=''):
        super().__init__(id)
        self.capacity = int(capacity)
        self.operator = operator
        self.manufacturer = manufacturer
        self.number_of_engines = 4
        self.description = 'plane with wings'


class Helicopter(Aircraft):

    def __init__(self, id, capacity, manufacturer='', operator=''):
        super().__init__(id)
        self.capacity = int(capacity)
        self.operator = operator
        self.manufacturer = manufacturer
        self.number_of_engines = 1
        self.description = 'helicopter with rotor'

    def hover(self):
        return ('chuck chuck chuck chuck chuck chuck')


