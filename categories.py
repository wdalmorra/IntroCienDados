import os
import json
path = './raw_data/'

gcats = []
for filename in os.listdir(path):
    with open(path+filename) as data_file:
		game = json.load(data_file)
		game_id = filename.split("=")[1]
		
		if game[game_id]["success"] == True:
			gdata = game[game_id]["data"]
			gtype = gdata["type"]
			if gtype != "game" and gtype != "dlc":
				continue
			if "categories" in gdata:
				print game_id
				for x in gdata["categories"]:
					if x["description"] not in gcats:
						gcats.append(x["description"])


for x in gcats:
	print x