import sqlite3

def connect_to_database(databaseName):
	conn = sqlite3.connect(databaseName) # or use :memory: to put it in RAM
	cursor = conn.cursor()
	return cursor

def create_table(cursor):
	sql_statement = """create table forage_data (site_id varchar, species_name varchar) """
	cursor.execute(sql_statement)
