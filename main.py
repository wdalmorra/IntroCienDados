import os
import json
import csv

path = './raw_data/'
counter = 0
counter_g = 0
counter_d = 0


columns = ["id", "nome", "tipo", "idade_min", "n_ling_sup", "moeda", "preco_orig", "preco_desc", "windows", "mac", "linux", "score_metac","score_rank", "n_positive_reviews", "n_negative_reviews", "n_owners", "n_owners_variance", "n_players_forever", "n_players_forever_variance", "n_players_2weeks", "n_players_2weeks_variance", "time_average_forever", "time_average_2weeks", "time_median_forever", "time_median_2weeks", "n_generos", "Action","Free to Play", "Indie", "Strategy", "Casual", "Adventure", "Simulation", "Sports", "Racing", "RPG", "Education", "Violent", "Gore", "Massively Multiplayer", "Early Access", "Audio Production", "Software Training", "Utilities", "Video Production", "Sexual Content", "Nudity", "Animation & Modeling", "Design & Illustration", "Photo Editing", "Web Publishing", "Accounting", "n_categorias", "Single-player", "Multi-player", "Online Multi-Player", "Co-op", "Online Co-op", "Downloadable Content", "Steam Achievements", "In-App Purchases", "Steam Leaderboards", "Steam Trading Cards", "Steam Cloud", "Full controller support", "Partial Controller Support", "Shared/Split Screen", "Cross-Platform Multiplayer", "Local Multi-Player", "Local Co-op", "Stats", "MMO", "Steam Workshop", "Captions available", "Valve Anti-Cheat enabled", "Includes level editor", "Steam Turn Notifications", "VR Support", "SteamVR Collectibles", "Includes Source SDK", "Commentary available", "Mods", "n_recomendacoes", "n_achievements", "data_lancamento"]
with open("output.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(columns)

all_genres = ["Action","Free to Play", "Indie", "Strategy", "Casual", "Adventure", "Simulation", "Sports", "Racing", "RPG", "Education", "Violent", "Gore", "Massively Multiplayer", "Early Access", "Audio Production", "Software Training", "Utilities", "Video Production", "Sexual Content", "Nudity", "Animation & Modeling", "Design & Illustration", "Photo Editing", "Web Publishing", "Accounting"]
all_categories = ["Single-player", "Multi-player", "Online Multi-Player", "Co-op", "Online Co-op", "Downloadable Content", "Steam Achievements", "In-App Purchases", "Steam Leaderboards", "Steam Trading Cards", "Steam Cloud", "Full controller support", "Partial Controller Support", "Shared/Split Screen", "Cross-Platform Multiplayer", "Local Multi-Player", "Local Co-op", "Stats", "MMO", "Steam Workshop", "Captions available", "Valve Anti-Cheat enabled", "Includes level editor", "Steam Turn Notifications", "VR Support", "SteamVR Collectibles", "Includes Source SDK", "Commentary available", "Mods"]
for filename in os.listdir(path): 
	final_row = []
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
			gplat_wind = 1 if gdata["platforms"]["windows"] else 0
			gplat_mac = 1 if gdata["platforms"]["mac"] else 0
			gplat_lin = 1 if gdata["platforms"]["linux"] else 0
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

			gscore_rank = None
			gpositive = None
			gnegative = None
			gowners = None
			gowners_v = None
			gplayers_f = None
			gplayers_f_v = None
			gplayers_2w = None
			gplayers_2w_v = None
			gaverage_f = None
			gaverage_2w = None
			gmedian_f = None
			gmedian_2w = None

			with open("raw_data_spy/api.php?request=appdetails&appid="+str(game_id)) as data_file_spy:
				game_spy = json.load(data_file_spy)

				gscore_rank = game_spy["score_rank"]
				gpositive = game_spy["positive"]
				gnegative = game_spy["negative"]
				gowners = game_spy["owners"]
				gowners_v = game_spy["owners_variance"]
				gplayers_f = game_spy["players_forever"]
				gplayers_f_v = game_spy["players_forever_variance"]
				gplayers_2w = game_spy["players_2weeks"]
				gplayers_2w_v = game_spy["players_2weeks_variance"]
				gaverage_f = game_spy["average_forever"]
				gaverage_2w = game_spy["average_2weeks"]
				gmedian_f = game_spy["median_forever"]
				gmedian_2w = game_spy["median_2weeks"]



			final_row.append(gappid)
			final_row.append(gname.encode("utf-8"))
			print gname.encode("utf-8")
			final_row.append(gtype)
			final_row.append(greq_age)
			if gsup_lang != None:
				final_row.append(len(gsup_lang.split(",")))
			else:
				final_row.append(0)
			final_row.append(gprice_curr)
			final_row.append(gprice_init)
			final_row.append(gprice_final)
			final_row.append(gplat_wind)
			final_row.append(gplat_mac)
			final_row.append(gplat_lin)
			final_row.append(gscore)
			final_row.append(gscore_rank)
			final_row.append(gpositive)
			final_row.append(gnegative)
			final_row.append(gowners)
			final_row.append(gowners_v)
			final_row.append(gplayers_f)
			final_row.append(gplayers_f_v)
			final_row.append(gplayers_2w)
			final_row.append(gplayers_2w_v)
			final_row.append(gaverage_f)
			final_row.append(gaverage_2w)
			final_row.append(gmedian_f)
			final_row.append(gmedian_2w)
			final_row.append(len(ggenres))
			for x in all_genres:
				if x in ggenres:
					final_row.append(1)
				else:
					final_row.append(0)
			final_row.append(len(gcats))
			for x in all_categories:
				if x in gcats:
					final_row.append(1)
				else:
					final_row.append(0)
			final_row.append(grecom)
			final_row.append(gachiev)
			final_row.append(grel_date.encode("utf-8"))



			with open("output.csv", 'a') as myfile:
				wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
				# print final_row
				wr.writerow(final_row)			