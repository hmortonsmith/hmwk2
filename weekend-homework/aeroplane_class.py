from aircraft_class import Aircraft


class Aeroplane(Aircraft):

    def __init__(self, id, capacity, manufacturer='', operator=''):
        super().__init__(id)
        self.capacity = int(capacity)
        self.operator = operator
        self.manufacturer = manufacturer
        self.number_of_engines = 4


