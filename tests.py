import pytest
import forageConversionTool

def test_can_connect_to_db():
	try:
		forageConversionTool.connect_to_database('nancydb')
		assert True
	except Exception as e:
		assert False

def test_can_create_table():
	# write some code that creates a table in forageConversionTool and then 
	aCursor = forageConversionTool.connect_to_database('nancydb')
	forageConversionTool.create_table(aCursor)

	# write some code here that checks for it using this sql:
	aCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='forage_data';")
	rows = aCursor.fetchall()
	assert len(rows) == 1

def test_can_load_data():
	assert False

