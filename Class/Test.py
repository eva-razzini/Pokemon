import json


with open("Json/save_player.json", "r", encoding='utf-8') as file:
    information = json.load(file)
pokemon_information = information.get("team")
print(pokemon_information)
pokemon_name = pokemon_information[0][2]
print(pokemon_name)

# with open("Json/save_player.json", "r", encoding='utf-8') as file:
#     information = json.load(file)
#     pokemon_information = information.get("team")
#     pokemon_player = pokemon_information[0][0]
#     level_player = pokemon_information[0][2]

# with open("Json/save_player.json", "r", encoding='utf-8') as file:
#     information = json.load(file)

# if information["character"] == "boy":
#     print("yes")
# else:
#     print("no")

# with open("Json/description_moves.json", "r", encoding='utf-8') as file:
#     description_moves = json.load(file)
# for i in range(1, len(description_moves)+1):
#     if "pay-day" == str(description_moves["i"]):
#         print("Yes")

# moves_1 = description_moves.get("pay-day")
# moves_1["pp"] -= 1
# move_power = moves_1.get("power")
# # print(moves_1)
# move_type = moves_1["type"]
# print(move_type)

# with open("Json/types_advantages.json", "r", encoding='utf-8') as file:
#     type_strenght = json.load(file)

# move_type = "flying"
# move_explain = type_strenght.get(str(move_type))
# print(move_explain)
# if move_type in move_explain['weaknesses']:
#     coef = 2
# elif move_type in move_explain['strengths']:
#     coef = 0.5
# else:
#     coef = 1
# print(coef)
# type_advantage = type_used.get()
# print(type_advantage)




# # if "Herbizarre" == str(pokedex[1]["name"]["french"]) or str("Herbizarre" == pokedex[1]["name"]["english"]):
# #     print("yes")

# # print(pokedex[1]["name"]["french"])

# # def find_pokemon_by_name(name):
# #     return


# # def dump(pokedex):
# #     with open("Json/Complete_Pokedex.json", "w") as file:
# #         pokedex = json.dump(file, indent=4)

# # dump(convert_to_dict(pokedex))

# def get_pokedex(name):
#     with open("Json/"+f"{name}.json") as f:
#         pokedex = json.load(f)
#     return pokedex


# def dump_pokedex(name, pokedex):
#     with open("Json/"+f"{name}.json", "w") as f:
#         json.dump(pokedex, f, indent=4)

# def convert_to_dict(pokedex):
#     new_pokedex = {}
#     for i in range(len(pokedex)):
#         new_pokedex[str(i+1)] = pokedex[i]
#     return new_pokedex

# # pokedex=get_pokedex('Complete_Pokedex')

# pokedex=convert_to_dict(pokedex)

# dump_pokedex('new_pokedex',pokedex)
