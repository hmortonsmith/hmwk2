
class FlightList:

    def __init__(self, flight_num, destination, origin='Heathrow'):
        self.passenger_list = []
        self.pilot = ''
        self.destination = destination
        self.origin = origin
        self.aircraft = ''
        self.flight_num = int(flight_num)

    def set_aircraft(self, aircraft):
        self.aircraft = aircraft
        return'Aircraft set'

    def set_pilot(self, pilot):
        self.pilot = pilot
#        return f"{self.name} is your pilot"
        print(pilot.name, 'assigned as pilot')

    def add_passengers(self, passenger):
        self.passenger_list.append(passenger)
        print(passenger.name, 'has been added to flight', self.flight_num)
 #       return f"{passenger} has been added to the flight"
 #       print(passenger.fullname, ': passenger added')