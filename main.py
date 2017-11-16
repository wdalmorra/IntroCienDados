import os
import json
path = './raw_data/'
counter = 0
counter_g = 0
counter_d = 0
for filename in os.listdir(path):
    with open(path+filename) as data_file:
		game = json.load(data_file)
		game_id = filename.split("=")[1]
		if game[game_id]["success"] == True:
			gdata = game[game_id]["data"]
			print game_id
			# Data to be gathered
			gtype = gdata["type"]
			if gtype != "game" and gtype != "dlc":
				continue
			counter += 1
			if gtype == "game":
				counter_g += 1
			if gtype == "dlc":
				counter_d += 1
			gname = gdata["name"]
			gappid = game_id
			if "required_age" in gdata:
				greq_age = gdata["required_age"]
			if "supported_languages" in gdata:
				gsup_lang = gdata["supported_languages"]
			if "price_overview" in gdata:
				gprice_curr = gdata["price_overview"]["currency"]
				gprice_init = gdata["price_overview"]["initial"]
				gprice_final = gdata["price_overview"]["final"]
			gplat_wind = gdata["platforms"]["windows"]
			gplat_mac = gdata["platforms"]["mac"]
			gplat_lin = gdata["platforms"]["linux"]
			gscore = None
			if "metacritic" in gdata:
				gscore = gdata["metacritic"]["score"]
			gcats = []
			if "categories" in gdata:
				for x in gdata["categories"]:
					gcats.append(x["description"])
			ggenres = []
			if "genres" in gdata:
				for x in gdata["genres"]:
					ggenres.append(x["description"])
			if "recommendations" in gdata:
				grecom = gdata["recommendations"]["total"]
			if "achievements" in gdata:
				gachiev = gdata["achievements"]["total"]
				
			grel_date = gdata["release_date"]["date"]

print counter
print counter_g
print counter_d

			