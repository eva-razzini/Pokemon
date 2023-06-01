from Class.Settings import *
from Class.Buttons import Button
from Class.PlayMenu import PlayMenu

class ChoiceMenu:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Attrapez-les tous !")
        self.win = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True

        self.button_play = Button(None, "Play", NORMAL_FONT, (220, 610), None, BLACK, GREY, None)
        self.button_pokedex = Button(None, "Open Pokedex", NORMAL_FONT, (500, 610), None, BLACK, GREY, None)
        self.button_reset = Button(None, "Reset game", NORMAL_FONT, (480, 650), None, BLACK, GREY, None)
        self.button_quit = Button(None, "Quit", NORMAL_FONT, (215, 650), None, BLACK, GREY, None)
    
    def draw(self):
        # Background :
        self.menu_background = pg.image.load("Pictures/Other/background_choice.png")
        self.win.blit(self.menu_background, (0,0))

        # Textbox:
        self.textbox = pg.image.load("Pictures/Other/textbox.png")
        self.textbox = pg.transform.scale(self.textbox, (int(self.textbox.get_width())*3.5, int(self.textbox.get_height())*3.5))
        self.textbox_position = self.textbox.get_rect(center=(WIN_RES[0]/2, 610))
        self.win.blit(self.textbox, self.textbox_position)

        self.text = NORMAL_FONT.render("What do you want to do ?", True, BLACK)
        self.win.blit(self.text, (100, 550))

        # Buttons : 
        self.button_play.draw(self.win)
        self.button_pokedex.draw(self.win)
        self.button_reset.draw(self.win)
        self.button_quit.draw(self.win)
        

    def update(self):
        self.button_play.color_hover(self.mouse_pos)
        self.button_pokedex.color_hover(self.mouse_pos)
        self.button_reset.color_hover(self.mouse_pos)
        self.button_quit.color_hover(self.mouse_pos)

    def events(self):
        self.mouse_pos = pg.mouse.get_pos()
        # self.click = pg.mouse.get_pressed()

        for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.button_play.button_clicked(self.mouse_pos):
                        self.game = PlayMenu()
                        self.game.run()
                    elif self.button_quit.button_clicked(self.mouse_pos):
                        quit()

    
    def run(self):
        while self.running:
            self.draw()
            self.events()
            self.update()
            pg.display.update()
