import json
import os

def analyse_tables(path):
	
	""" takes the path to file conatining all dbs stored in json format and returns number of tables, unique colums, text and integer columns"""
	
	table_count=0 # number of tables in dataset
	text_columns=0 # number of text columns
	number_columns=0 # number of integer columns
	unique_columns=[] # unique columns throughout dataset
	type_of={} # type of each unique colums
	try:
		with open(path) as f:
			
			dbs = json.loads(f.read()) # dbs contains all unique dbs of dataset
			
			for db in dbs:
				table_count+=len(db["table_names"]) #increment couter for tables
				columns=db["column_names"]
				types=db["column_types"]
				
				for i in range(0,len(columns)):
					if columns[i][1] not in unique_columns: # to get all unique columns across dataset
						unique_columns.append(columns[i][1])
						type_of[columns[i][1]]=types[i] # setting data type of the column


			for key in type_of.keys():
				if type_of[key] == 'text':
					text_columns+=1
				elif type_of[key] == 'number':
						number_columns+=1

			# print results
			print("Number of text columns")
			print(text_columns)
			print("Number of integer columns")
			print(number_columns)
			print("Number of tables")
			print(table_count)
			print("Number of unique columns")
			print(len(unique_columns))
	except err:
		print(err)


def main():
	dirname = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(dirname, "../data/tables.json")
	analyse_tables(path)

	


if __name__ == '__main__':
	main()
