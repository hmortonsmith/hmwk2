from aircraft_class import *
from people_class import *
from flight_list_class import *

#  create aircraft
a380 = Aeroplane(57125, 280, 'Airbus', 'British Airways')
# print(a380.fly())
# print(a380.capacity)
# print(a380.manufacturer)

# create passengers and pilot
collin = Passenger(55478951, 'Collin Edwards', 'Irish')
hans = Staff('Pilot','Hans Neils', 'German')
ben = Passenger(58463248, 'Benjamin Sanders', 'Canadian')
pippa = Passenger(478996215, 'Pippa Aldrich', 'Australian')

# print(collin.name)
# print(collin.passport_num)
# print(collin.nationality)

flight_list_BA1016 = FlightList(1016, 'JFK')

flight_list_BA1016.set_aircraft(a380)

flight_list_BA1016.add_passengers(collin)
flight_list_BA1016.add_passengers(ben)
flight_list_BA1016.add_passengers(pippa)

flight_list_BA1016.set_pilot(hans)
print('\n')

print(flight_list_BA1016.aircraft)
print(flight_list_BA1016.aircraft.manufacturer)
print(flight_list_BA1016.aircraft.operator)
print(flight_list_BA1016.aircraft.aircraft_id, '\n')

passenger_list = flight_list_BA1016.passenger_list

for passenger in passenger_list:
    print(passenger.name, 'passport number:',passenger.passport_num)

#print(collin.greeting)

