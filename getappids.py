import json
from pprint import pprint
with open("listaappids.json") as data_file:
	list_ids = json.load(data_file)

full_list = list_ids['applist']['apps']

for game in full_list:
	print game['appid']