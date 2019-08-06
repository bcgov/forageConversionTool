import sqlite3

def connect_to_database(databaseName):
	conn = sqlite3.connect(databaseName) # or use :memory: to put it in RAM
	cursor = conn.cursor()
	return cursor
	
