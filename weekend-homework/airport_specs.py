from aircraft_class import *
from people_class import *
from flight_trip_class import *
import pytest

test_passenger1 = Passenger(1,'','')


def test_create_passenger():
    assert isinstance(test_passenger1, Passenger)


def test_check_name_num():
    assert test_passenger1.name != None and test_passenger1.passport_num != None


def test_specific_name_num1():
    test_passenger2 = Passenger('B343123', 'Joana Thompson', '')
    assert test_passenger2.name == 'Joana Thompson' and test_passenger2.passport_num == 'B343123'


def test_specific_name_num3():
    test_passenger3 = Passenger('B13927', 'Birt Kuman', 'B13927')
    assert test_passenger3.name == 'Birt Kuman' and test_passenger3.passport_num == 'B13927'


def test_raises_error():
    with pytest.raises(TypeError):
        test_passenger4 = Passenger()


test_plane = Aeroplane(1, 1, '', '')


def test_create_plane():
    assert isinstance(test_plane, Aeroplane) and test_plane.aircraft_id == 1


test_flight_trip = FlightTrip()


def test_create_flight():
    assert isinstance(test_flight_trip, FlightTrip)


def test_add_plane():
    test_flight_trip.set_aircraft(test_plane)
    assert isinstance(test_flight_trip.aircraft, Aeroplane)


def test_set_origin():
    test_flight_trip.set_origin('test_origin')
    assert test_flight_trip.origin == 'test_origin'


def test_set_destination():
    test_flight_trip.set_destination('test_destination')
    assert test_flight_trip.destination == 'test_destination'


def test_type_passenger():
    test_flight_trip.add_passengers(test_passenger1)
    assert isinstance(test_flight_trip.passenger_list[0], Passenger)

def test_add_passenger():
    test_flight_trip2 = FlightTrip()
    test_flight_trip2.add_passengers(test_passenger1)
    assert len(test_flight_trip.passenger_list) == 1
