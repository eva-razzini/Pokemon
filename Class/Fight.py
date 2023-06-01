from Class.Settings import *
from Class.Buttons import Button

class Fight():
    def __init__(self):
        pg.init()
        pg.display.set_caption("Attrapez-les tous !")
        self.win = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.random = random.randint(1, 6)
        print(self.random)
        self.running = True

        with open("Json/save_player.json", "r", encoding='utf-8') as file:
            self.information = json.load(file)
        self.pokemon_information = self.information.get("team")
        self.pokemon_player = self.pokemon_information[0][0]
        self.level_player = self.pokemon_information[0][2]


    def draw(self):
        # Background :
        self.win.fill((0,0,0))
        self.battle_background = pg.image.load("Pictures/Battle/Backgrounds/" + str(self.random) + ".png")
        self.battle_background = pg.transform.scale(self.battle_background, (int(self.battle_background.get_width()) * 2.4, int(self.battle_background.get_height()) * 2.4))
        self.background_position = self.battle_background.get_rect(center = (WIN_RES[0]/2, 220))
        self.win.blit(self.battle_background, self.background_position)

        # Circles : 
        self.circles = pg.image.load("Pictures/Battle/Circles/" + str(self.random) + ".png")
        self.circles = pg.transform.scale(self.circles, (int(self.circles.get_width()) * 2.4, int(self.circles.get_height()) * 2.4))
        self.circles_position = self.circles.get_rect(center = (WIN_RES[0]/2, 220))
        self.win.blit(self.circles, self.circles_position)

    def event(self):
        self.click = pg.mouse.get_pressed()

        for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()

    def update(self):
        pass

    def run(self):
        while self.running:
            self.draw()
            self.update()
            self.event()
            
            pg.display.update()