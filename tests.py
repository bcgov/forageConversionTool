import pytest
import forageConversionTool

def test_can_connect_to_db():
	try:
		forageConversionTool.connect_to_database('nancydb')
		assert True
	except Exception as e:
		assert False

def test_can_create_table():
	assert False

def test_can_load_data():
	assert False

