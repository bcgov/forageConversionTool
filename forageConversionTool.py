import sqlite3
import os
import Levenshtein

def connect_to_database(databaseName):
	conn = sqlite3.connect(databaseName) # or use :memory: to put it in RAM
	cursor = conn.cursor()
	return cursor

def delete_db(databaseName):
	try:
		os.remove(databaseName)	
	except Exception as e:
		print("Ran into problem deleting " + databaseName)
		print(e.message)

def validate_input_file_headers(filename):
	return False

def create_table(cursor):
	try:
		sql_statement = """create table forage_data (
					ForageSite varchar,
					Person varchar,
					Date varchar,
					Year_Clipped varchar,
					GPS_ID varchar,
					Plant_Community varchar,
					Year_Logged varchar,
					X_Coord varchar,
					Y_Coord varchar,
					UTM varchar,
					E varchar
					N varchar
					BEC varchar,
					Site_series varchar,
					Elevation varchar,
					Slope varchar,
					Aspect varchar,
					Slope_position varchar,
					Grazed_Pre varchar,
					Picture_2m varchar,
					Picture_10 varchar,
					non_prod varchar,
					reason varchar,
					Weight1gr varchar,
					Weight2gr varchar,
					Weight3gr varchar,
					Weight4gr varchar,
					Weight5gr varchar,
					Average varchar,
					cv varchar,
					Grass1 varchar,
					Grass1cov varchar,
					Grass2 varchar,
					Grass2cov varchar,
					Grass3 varchar,
					Grass3cov varchar,
					Forb1 varchar,
					Forb1cov varchar,
					Forb2 varchar,
					Forb2cov varchar,
					Forb3 varchar,
					Forb3cov varchar,
					Forb4 varchar,
					Forb4cov varchar,
					Forb5 varchar,
					Forb5cov varchar,
					Shrub1 varchar,
					Shrub1cov varchar,
					Shrub2 varchar,
					Shrub2cov varchar,
					Shrub3 varchar,
					Shrub3cov varchar,
					Tree1 varchar,
					Tree1cov varchar,
					Tree2 varchar,
					Tree2cov varchar,
					Tree3 varchar,
					Tree3cov varchar,
					Tree4 varchar,
					Tree4cov varchar,
					Tree5 varchar,
					Tree5cov varchar,
					ExclSpecies varchar,
					Comments varchar,
					DEM_ELEV varchar,
					DEM_Aspect varchar,
					DEM_Slope varchar,
					Kg_per_ha varchar)
					"""
		cursor.execute(sql_statement)
		cursor.execute("PRAGMA table_info(forage_data);")
		rows = cursor.fetchall()
		print("Created columns in forage_data...")
		for row in rows:
			print(row)

	except sqlite3.OperationalError as e:
		print("forage table already exists.. skipping create step")
	except Exception as e:
		print("something else bad happened while creating forage data table")
		print(e.message)


def suggest_word(input_word, word_list):
	word_score_dict = {}

	for word in word_list:
		word_score_dict[Levenshtein.distance(input_word, word)] = word

	sorted_scores = sorted(word_score_dict.keys())
	
	index_of_winning_word = word_list.index(word_score_dict[sorted_scores[0]])
	print('you entered ' + word + ' and maybe you meant ' +  word_list[index_of_winning_word])

	return index_of_winning_word

def suggest_sachins_way(input_word, word_list):
	word_score_dict = {}
	score_list = []
	
	for word in word_list:
		score = Levenshtein.distance(input_word, word)
		word_score_dict[score] = word
		score_list.append(score)

	index_of_winning_word = min(score_list)
	print("you entered " + word + " and maybe you meant " + word_list[index_of_winning_word])
