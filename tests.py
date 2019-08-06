import forageConversionTool
import os

def test_can_connect_to_db():
	try:
		forageConversionTool.connect_to_database('nancydb')
		assert True
	except Exception as e:
		assert False


def test_can_create_table():
	forageConversionTool.delete_db('nancydb')
	# write some code that creates a table in forageConversionTool and then 
	aCursor = forageConversionTool.connect_to_database('nancydb')
	forageConversionTool.create_table(aCursor)

	# write some code here that checks for it using this sql:
	aCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='forage_data';")
	rows = aCursor.fetchall()
	assert len(rows) == 1

def test_can_load_data():
	assert False

def test_can_delete_old_db():
	# write some code that creates a table in forageConversionTool and then 
	aCursor = forageConversionTool.connect_to_database('nancydb')
	forageConversionTool.create_table(aCursor)
	forageConversionTool.delete_db('nancydb')
	
	assert (os.path.isfile('nancydb')) == False


def test_input_file_has_all_the_right_headers()
	assert False

def test_can_get_all_input_file_headers_in_list():
	assert False

def test_can_get_all_db_columns_in_list():
	assert False
