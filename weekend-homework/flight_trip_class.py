
class FlightTrip:

    def __init__(self, flight_num='', destination='', origin=''):
        self.passenger_list = []
        self.pilot = ''
        self.destination = destination
        self.origin = origin
        self.aircraft = ''
        self.flight_num = flight_num

    def set_aircraft(self, aircraft):
        self.aircraft = aircraft
        return'Aircraft set'

    def set_destination(self, destination):
        self.destination = destination
        print(self.destination, 'set as destination')

    def set_origin(self, origin):
        self.origin = origin
        print(self.origin, 'set as origin')

    def set_pilot(self, pilot):
        self.pilot = pilot
#        return f"{self.name} is your pilot"
        print(pilot.name, 'assigned as pilot to flight', self.flight_num)

    def add_passengers(self, passenger):
        self.passenger_list.append(passenger)
        print(passenger.name, 'has been added to flight', self.flight_num)
