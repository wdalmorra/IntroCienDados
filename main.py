import os
import json
import csv

path = './raw_data/'
counter = 0
counter_g = 0
counter_d = 0

final_row = []

all_genres = ["Action","Free to Play", "Indie", "Strategy", "Casual", "Adventure", "Simulation", "Sports", "Racing", "RPG", "Education", "Violent", "Gore", "Massively Multiplayer", "Early Access", "Audio Production", "Software Training", "Utilities", "Video Production", "Sexual Content", "Nudity", "Animation & Modeling", "Design & Illustration", "Photo Editing", "Web Publishing", "Accounting", "Ação", "Aventura"]
all_categories = ["Single-player", "Multi-player", "Online Multi-Player", "Co-op", "Online Co-op", "Downloadable Content", "Steam Achievements", "In-App Purchases", "Steam Leaderboards", "Steam Trading Cards", "Steam Cloud", "Full controller support", "Partial Controller Support", "Shared/Split Screen", "Cross-Platform Multiplayer", "Local Multi-Player", "Local Co-op", "Stats", "MMO", "Steam Workshop", "Captions available", "Valve Anti-Cheat enabled", "Includes level editor", "Steam Turn Notifications", "VR Support", "SteamVR Collectibles", "Includes Source SDK", "Commentary available", "Um jogador", "Compatibilidade total com controle", "Mods"]
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
			greq_age=None
			if "required_age" in gdata:
				greq_age = gdata["required_age"]
			gsup_lang = None
			if "supported_languages" in gdata:
				gsup_lang = gdata["supported_languages"]
			gprice_curr = None
			gprice_init = None
			gprice_final = None
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
			grecom = None
			if "recommendations" in gdata:
				grecom = gdata["recommendations"]["total"]
			gachiev = None
			if "achievements" in gdata:
				gachiev = gdata["achievements"]["total"]
				
			grel_date = gdata["release_date"]["date"]

			final_row.append(gappid)
			final_row.append(gname)
			final_row.append(gtype)
			final_row.append(greq_age)
			final_row.append(gsup_lang)
			final_row.append(gprice_curr)
			final_row.append(gprice_init)
			final_row.append(gprice_final)
			final_row.append(gplat_wind)
			final_row.append(gplat_mac)
			final_row.append(gplat_lin)
			final_row.append(gscore)
			for x in all_categories:
				if x in gcats:
					final_row.append(True)
				else:
					final_row.append(False)
			for x in all_genres:
				if x in ggenres:
					final_row.append(True)
				else:
					final_row.append(False)
			final_row.append(grecom)
			final_row.append(gachiev)
			final_row.append(grel_date)

	with open("output.csv", 'wb') as myfile:
    	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    	wr.writerow(final_row)

    break


print counter
print counter_g
print counter_d

			