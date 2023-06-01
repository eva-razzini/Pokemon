from Class.Settings import *
from Class.Buttons import Button

class Pokemon:
    def __init__(self, name, level):
        self.__name = name
        self.__maxHP = 100
        self.defense = 0
        self.level = level
        self.current_HP = int(self.get_hp())

        with open("Json/Complete_Pokedex.json", "r", encoding='utf-8') as file:
            self.pokedex = json.load(file)

        self.get_data()
        self.calcul_stats()
        self.get_sprite()
        self.get_moves()
        self.get_description_moves()

    def get_data(self):
        for i in range(1, len(self.pokedex)+1):
            if str(self.get_name()) == str(self.pokedex[str(i)]["name"]["french"]) or str(self.get_name()) == str(self.pokedex[str(i)]["name"]["english"]):
                self.id = self.pokedex[str(i)]["id"]
                self.type = self.pokedex[str(i)]["type"]
                self.base_hp = self.pokedex[str(i)]["base"]["HP"]
                self.attack = self.pokedex[str(i)]["base"]["Attack"]
                self.defense = self.pokedex[str(i)]["base"]["Defense"]
                self.sp_attack = self.pokedex[str(i)]["base"]["Sp. Attack"]
                self.sp_defense = self.pokedex[str(i)]["base"]["Sp. Defense"]
                self.speed = self.pokedex[str(i)]["base"]["Speed"]
                self.__set_pv(int(self.pokedex[str(i)]["base"]["HP"]))
                break

    # We use IV=31 and EV=0 (neutral) to calculate stat, and a neutral status(= 1)
    def calcul_stats(self):
        self.attack = ((2 * self.attack + 31) * self.level/ 100) + 5
        self.defense = ((2 * self.defense + 31) * self.level/ 100) + 5
        self.sp_attack = ((2 * self.sp_attack + 31) * self.level/ 100) + 5
        self.sp_defense = ((2 * self.sp_defense + 31) * self.level/ 100) + 5
        self.speed = ((2 * self.speed + 31) * self.level/ 100) + 5
        hp = ((2 * int(self.get_hp()) + 31) * self.level/ 100) + self.level + 5
        self.modify_pv(hp)

    def get_sprite(self):
        self.front_sprite = pg.image.load("Pictures/Sprites_Pokemon/front/" + str(self.id) + ".png")
        self.back_sprite = pg.image.load("Pictures/Sprites_Pokemon/back/" + str(self.id) + ".png")

    def get_moves(self):
        with open("Json/pokemon_moves.json", "r", encoding='utf-8') as file:
            self.all_moves = json.load(file)
        self.moves = self.all_moves[str(self.id)]
        self.move_1 = self.moves[0]
        self.move_2 = self.moves[1]
        self.move_3 = self.moves[2]
        self.move_4 = self.moves[3]

    def get_description_moves(self):
        with open("Json/description_moves.json", "r", encoding='utf-8') as file:
            self.description_moves = json.load(file)
        self.move_1 = self.description_moves.get(str(self.move_1))
        self.move_2 = self.description_moves.get(str(self.move_2))
        self.move_3 = self.description_moves.get(str(self.move_3))
        self.move_4 = self.description_moves.get(str(self.move_4))

    def calcul_efficacy(self, enemy, move):
        self.move_type = move["type"]
        with open ("Json/types_advantages.json", "r", encoding = 'utf-8') as file:
            self.types_advantages = json.load(file)
        self.strenght_weak = self.types_advantages.get(str(self.move_type))
        if enemy.type in self.strenght_weak['strengths']:
            self.coef = 2
        elif enemy.type in self.strenght_weak['weaknesses']:
            self.coef = 0.5
        else:
            self.coef = 1
    
    def attack(self, enemy, move):
        # We use Special Attack when the pokemon has the same type as the type of the move
        if self.move_type == self.type:
            self.atk_used = self.sp_attack
        else:
            self.atk_used = self.attack
        
        # We use Special Defense when the attack is super efficient
        if self.coef == 2:
            self.enemy_defense = enemy.sp_defense
        else:
            self.enemy_defense = enemy.defense

        self.power = move["power"]
        if self.power == "null":
            self.power = 0
        else:
            self.power = int(self.power)
        
        # Calcul damage (simplified, we don't use objects or effects like burned): 
        self.damage = ((self.level * 2 / 5) * self.power * self.atk_used) / self.enemy_defense
        
        # Critical Strike and failure :
        self.bonus_damage = random.randint(0, 100)
        if self.bonus_damage <= 8 and self.bonus_damage >= 0:
            self.damage *= 0 #Failure
            print("Failure !")
        if self.bonus_damage < 8 and self.bonus_damage >= 16:
            self.damage *= 1.7 # Critical Strike
            print("Critical Strike !")

        # Damage received : 
        enemy.current_HP -= self.damage

       
    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__maxHP
    
    def modify_pv(self, new_pv):
        return self.__set_pv(new_pv)

    def __set_pv(self, new_pv):
        self.__maxHP = new_pv

    def display(self):
        print(self.attack)
        print(self.defense)
        print(self.move_1)

p1 = Pokemon("Mewtwo", 90)
p1.display()





# with open("Json/Complete_Pokedex.json", "r", encoding='utf-8') as file:
#     POKEDEX = json.load(file)

# def get_pokemon_data(id,language):
#     return {
#         'id':POKEDEX[str(id)]['id'],
#         'name':POKEDEX[str(id)]['name'][language],
#         'type':POKEDEX[str(id)]['type'],
#         'stats':POKEDEX[str(id)]['base']

#     }

# print(get_pokemon_data(150,'french'))