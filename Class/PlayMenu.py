from Class.Settings import *
from Class.Buttons import Button
from Class.Fight import Fight

class PlayMenu:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Attrapez-les tous !")
        self.win = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True

        with open("Json/save_player.json", "r", encoding='utf-8') as file:
            self.information = json.load(file)
        self.pokemon_information = self.information.get("team")
        self.pokemon_player = self.pokemon_information[0][0]
        self.level_player = self.pokemon_information[0][2]

        self.button_fight = Button(None, "Fight", NORMAL_FONT, (170, 560), None, BLACK, GREY, None)
        self.button_pokedex = Button(None, "Open my Pokedex", NORMAL_FONT, (265, 590), None, BLACK, GREY, None)
        self.button_save = Button(None, "Save", NORMAL_FONT, (165, 620), None, BLACK, GREY, None)
        self.button_quit = Button(None, "Quit", NORMAL_FONT, (158, 650), None, BLACK, GREY, None)
        
    def draw(self):
        # Background :
        self.win.fill((0,0,0))
        self.pokecenter = pg.image.load("Pictures/Other/background_pokecenter.png")
        self.pokecenter = pg.transform.scale(self.pokecenter, (int(self.pokecenter.get_width()) * 2.9, int(self.pokecenter.get_height()) * 2.9))
        self.pokecenter_position = self.pokecenter.get_rect(center = (WIN_RES[0]/2, 270))
        self.win.blit(self.pokecenter, self.pokecenter_position)

        # Characters :
        if self.information["character"] == "girl":
            self.character = pg.image.load("Pictures/Other/girl.png")
        else:
            self.character = pg.image.load("Pictures/Other/boy.png")
        self.character = pg.transform.scale(self.character, (int(self.character.get_width()) * 2.9, int(self.character.get_height()) * 2.9))
        self.character_position = self.character.get_rect(center = (WIN_RES[0]/2, 300))
        self.win.blit(self.character, self.character_position)

        self.partner = pg.image.load("Pictures/Sprites_Pokemon/overworld/down/" + str(self.pokemon_player) + ".png")
        self.partner = pg.transform.scale(self.partner, (int(self.partner.get_width()) * 2.9, int(self.partner.get_height()) * 2.9))
        self.win.blit(self.partner, (460, 248))

        # Textbox:
        self.textbox = pg.image.load("Pictures/Other/textbox.png")
        self.textbox = pg.transform.scale(self.textbox, (int(self.textbox.get_width())*3.5, int(self.textbox.get_height())*3.5))
        self.textbox_position = self.textbox.get_rect(center=(WIN_RES[0]/2, 610))
        self.win.blit(self.textbox, self.textbox_position)

        # Buttons : 
        self.button_fight.draw(self.win)
        self.button_pokedex.draw(self.win)
        self.button_save.draw(self.win)
        self.button_quit.draw(self.win)


    def event(self):
        self.mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.button_fight.button_clicked(self.mouse_pos):
                        self.game = Fight()
                        self.game.run()

    def update(self):
        self.button_fight.color_hover(self.mouse_pos)
        self.button_pokedex.color_hover(self.mouse_pos)
        self.button_save.color_hover(self.mouse_pos)
        self.button_quit.color_hover(self.mouse_pos)

    def run(self):
        while self.running:
            self.draw()
            self.event()
            self.update()
            pg.display.update()