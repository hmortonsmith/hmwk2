import pyodbc
from people_class import *


class ConnSql:
    # when we initialise, make the connection
    def __init__(self, server='localhost,1433', database='Airport', username='SA', password='Passw0rd2018'):
        # Our variables to create a connection
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
        self.cursor = self.conn.cursor()

    def get_all_passengers(self):
        passenger_query = self.cursor.execute('SELECT * FROM Passengers')
        pass_list = []
        while True:
            row = passenger_query.fetchone()
            if row is None:
                break
            else:

                pass_num = row.PassportNumber
                full_name = row.FullName
                nati = row.Nationality
                passenger_instance = Passenger(pass_num, full_name, nati)
            pass_list.append(passenger_instance)
        for passenger in pass_list:
            print(passenger.name, passenger.passport_num)

    def add_a_passenger(self, pass_num_insert, fullname_insert, nationality_insert):
        passenger_insert = Passenger(pass_num_insert, fullname_insert, nationality_insert)

        self.cursor.execute(f"INSERT INTO [Passengers] ([PassportNumber],[FullName],[Nationality]) VALUES ('{passenger_insert.passport_num}', '{passenger_insert.name}', '{passenger_insert.nationality}')")
        self.conn.commit()
