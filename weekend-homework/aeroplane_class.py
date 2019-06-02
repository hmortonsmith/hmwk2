from aircraft_class import Aircraft

class Aeroplane(Aircraft):

    def __init__(self, id, capacity, manufacturer='', operator=''):
        super().__init__(id)  # Run the init of parent class
        self.capacity = int(capacity)
        self.operator = operator
        self.manufacturer = manufacturer

