from aircraft_class import Aircraft


class Helicopter(Aircraft):

    def __init__(self, id, capacity, manufacturer='', operator=''):
        super().__init__(id)
        self.capacity = int(capacity)
        self.operator = operator
        self.manufacturer = manufacturer
        self.number_of_engines = 1

    def hover(self):
        return 'chuck chuck chuck chuck chuck chuck'
