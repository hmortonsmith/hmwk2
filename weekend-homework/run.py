from aircraft_class import *
from aeroplane_class import *
from helicopter_class import *
from people_class import *

a380 = Aeroplane(57125, 280, 'Airbus', 'Virgin Atlantic')
print(a380.fly())
print(a380.capacity)
print(a380.manufacturer)

collin = Passenger(55478951, 'Collin Edwards', 'Irish')
hans = Person('Hans Neils', 'German')

collin.greeting
print(collin.name)
print(collin.passport_num)
print(collin.name)
