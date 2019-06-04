from aircraft_class import *
from people_class import *
from flight_trip_class import *

#  create aircraft
a380 = Aeroplane(57125, 280, 'Airbus', 'British Airways')
aw778 = Helicopter(47890, 8, 'Augusta Westland', 'EasyJet')

# create passengers and pilots
collin = Passenger(55478951, 'Collin Edwards', 'Irish')
ben = Passenger(58463248, 'Benjamin Sanders', 'Canadian')
pippa = Passenger(478996215, 'Pippa Aldrich', 'Australian')
jeff = Passenger(899774452, 'Jeff Wayne', 'British')
sara = Passenger(48996652, 'Sara Roster', 'American')

chuck = Staff('Pilot', 'Chuck Yeager', 'American')
hans = Staff('Pilot', 'Hans Neils', 'German')

flight_trip_BA1016 = FlightTrip(1016)
flight_trip_BA1016.set_aircraft(a380)
#flight_trip_BA1016.add_passengers(collin)
#flight_trip_BA1016.add_passengers(ben)
#flight_trip_BA1016.add_passengers(pippa)
flight_trip_BA1016.set_destination('Glasgow')
flight_trip_BA1016.set_origin('Heathrow')

flight_trip_EJ2514 = FlightTrip(2514, 'Glasgow')
flight_trip_EJ2514.set_aircraft(aw778)
#flight_trip_EJ2514.add_passengers(sara)
#flight_trip_EJ2514.add_passengers(jeff)
print('\n')
# Add pilots
flight_trip_EJ2514.set_pilot(chuck)
flight_trip_BA1016.set_pilot(hans)
print('\n')


#tuesday_schedule = [flight_trip_BA1016, flight_trip_EJ2514]
#for flight in tuesday_schedule:
#    print(flight.flight_num, 'from', flight.origin, 'to', flight.destination)

print('\n')
#print('BA1016')
#print(flight_trip_BA1016.aircraft.manufacturer)
#print(flight_trip_BA1016.aircraft.operator)
#print(flight_trip_BA1016.aircraft.aircraft_id, '\n')

#print('BA1016 Passengers:')
#passenger_list = flight_trip_BA1016.passenger_list
#for passenger in passenger_list:
#    print(passenger.name, 'passport number:', passenger.passport_num)
#print('\n')

#print(aw778.hover())
#print(aw778.fly())
#print(collin.greeting())

