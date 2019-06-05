import pyodbc


class Conn_ms_sql():
    # when we initialise, make the connection
    def __init__(self, server='localhost,1433', database='Northwind', username='SA', password='Passw0rd2018'):
        # Our variables to create a connection
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
        self.cursor = self.docker_conn.cursor()