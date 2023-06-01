import pygame as pg
from Class.Settings import *

class Button:
    def __init__(self, image, text_input, font, pos, size, basic_color, hovering_color, action):
        self.image = image
        self.size = size
        self.text_input = text_input
        self.font = font
        self.basic_color = basic_color
        self.hovering_color = hovering_color
        self.text = font.render(self.text_input, True, self.basic_color)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        
        self.action = action
        if image is None:
            self.image = self.text
        else:
            self.image = pg.transform.scale(image, int(size[0]), int(size[1]))
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw(self, win):
        if self.image is not None:
            win.blit(self.image, self.rect)
        win.blit(self.text, self.text_rect)

    def button_clicked(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
    
    def color_hover(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.basic_color)

    # def button_clicked(self, win):
    #     self.mouse = pg.mouse.get_pos() # It gives us information about the mouse's position
    #     self.click = pg.mouse.get_pressed() # It gives information about the number of click
    #     if self.image == self.text :
    #         if (self.x_pos + self.x_size) > self.mouse[0] > self.x_pos and (self.y_pos + self.y_size) > self.mouse[1] > self.y_pos:
    #             self.basic_color = self.hovering_color
    #             win.blit(self.text, self.rect)
    #             pg.display.update()
    #     if self.click[0] == 1 and self.action != None:
    #         self.action()