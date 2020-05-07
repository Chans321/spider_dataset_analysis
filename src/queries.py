import json
import os

def analyse_queries(path,set_name):
	""" to analyse all queries and get the count of queries with different aggregation operators"""
	total_queries=0
	agg_ops = ['', 'MAX', 'MIN', 'COUNT', 'SUM', 'AVG'] # aggregation operators in sql queries
	agg_ops_count=[0 for i in range(6)] # cout of each aggregator operator

	try:
		with open(path) as f:
			all_queries = json.loads(f.read()) # all the queries in the file

		for query in all_queries:
			toks=query["query_toks"] # get all the tokens of sql queries

			for i in range(0,len(agg_ops)): # get count of each aggregator 
				if agg_ops[i] in toks or agg_ops[i].lower() in toks:
					agg_ops_count[i]+=1
		# print results
		print(set_name)
		print("Number of queries")
		print(len(all_queries))
		print("aggregation operators")
		print(agg_ops)
		print("corresponding count of each operator")
		print(agg_ops_count)
		print()
	
	except err:
		print(err)


def main():
	dirname = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(dirname, "../data/train_spider.json")
	analyse_queries(path,'train')
	path = os.path.join(dirname, "../data/train_others.json")
	analyse_queries(path,'train_others')
	path = os.path.join(dirname, "../data/dev.json")
	analyse_queries(path,'dev')
	
if __name__ == '__main__':
	main()