import os
import json
path = './raw_data/'

ggenres = []
for filename in os.listdir(path):
    with open(path+filename) as data_file:
		game = json.load(data_file)
		game_id = filename.split("=")[1]
		
		if game[game_id]["success"] == True:
			gdata = game[game_id]["data"]
			gtype = gdata["type"]
			if gtype != "game" and gtype != "dlc":
				continue
			if "genres" in gdata:
				for x in gdata["genres"]:
					if x["description"] not in ggenres:
						ggenres.append(x["description"])


for x in ggenres:
	print x