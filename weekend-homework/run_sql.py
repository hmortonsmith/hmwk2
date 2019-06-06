import pyodbc
from people_class import *

# Our variables to create a connection
server = 'localhost,1433'
database = 'Airport'
username = 'SA'
password = 'Passw0rd2018'

# Making a connection
docker_airport_cc = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')

# Creating a cursor allowing us to execute SQL functions on connected db
cursor = docker_airport_cc.cursor()

passenger_query = cursor.execute('SELECT * FROM Passengers')
pass_list = []
while True:
    row = passenger_query.fetchone()
    if row is None:
        break
    else:
        print(row.PassportNumber, row.FullName, row.Nationality)
        pass_num = row.PassportNumber
        full_name = row.FullName
        nati = row.Nationality
        passenger_instance = Passenger(pass_num, full_name, nati)
        pass_list.append(passenger_instance)

print(pass_list)
for passenger in pass_list:
    print(passenger.name)


# passenger_insert = Passenger('B897465132', 'Sarah Goodall', 'British')
#
# passenger_query2 = cursor.execute(f"INSERT INTO [Passengers] ([PassportNumber],[FullName],[Nationality]) VALUES ('{passenger_insert.passport_num}', '{passenger_insert.name}', '{passenger_insert.nationality}')")
#
# docker_airport_cc.commit()
