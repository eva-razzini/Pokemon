from Class.ChoiceMenu import *
from Class.Pokemon import Pokemon
from Class.Settings import *
from Class.Buttons import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Attrapez-les tous !")
        self.win = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True

        # We have to create all the buttons here to have a working hover
        self.button_play = Button(None, "PRESS START", BEGIN_SCREEN, (WIN_RES[0]/2, 620), None, WHITE, BLACK, ChoiceMenu())

    def draw(self):
        # Background :
        self.menu_background = pg.image.load("Pictures/Other/background_menu.png")
        self.win.blit(self.menu_background, (0,0))

        # Title :
        self.title_menu = pg.image.load("Pictures/Other/pokemon_title.png")
        self.title_menu = pg.transform.scale(self.title_menu, (500, 203))
        self.title_rect = self.title_menu.get_rect(center=(WIN_RES[0]/2, 200))
        self.win.blit(self.title_menu, self.title_rect)

        # Buttons :
        self.button_play.draw(self.win)

        pg.display.flip()


    def events(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()

        for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    self.game = ChoiceMenu()
                    self.game.run()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.click:
                        self.game = ChoiceMenu()
                        self.game.run()


    def update(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.button_play.color_hover(self.mouse_pos)
        

    def run(self):
        while self.running:
            self.draw()
            self.update()
            self.events()
            
            pg.display.update()

if __name__ == '__main__':
    menu = Game()
    menu.run()
    