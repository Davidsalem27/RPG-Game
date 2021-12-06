import pygame as pg
FONT_SIZE=20

class Speech_Bubble:
    def __init__(self, x, y, first_line, sec_line):
        self.base_font = pg.font.Font(None, FONT_SIZE)
        self.name = 'Speech_Bubble'
        self.text_first = first_line
        self.text_sec = sec_line
        self.image = pg.image.load(os.path.join('Isometric', 'text_background.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.width, self.rect.height = 70, 50
        self.rect.x, self.rect.y = x, y
        self.text_surface_first = self.base_font.render(self.text_first, True, (0, 0, 0), )
        self.text_surface_sec = self.base_font.render(self.text_sec, True, (0, 0, 0))

    def render(self):
        self.base_font.render(self.text_first, True, (0, 0, 0))
        self.base_font.render(self.text_sec, True, (0, 0, 0))

    def change_text(self, new_text_first, new_text_sec):
        self.text_first = new_text_first
        self.text_sec = new_text_sec
        self.text_surface_first = self.base_font.render(self.text_first, True, (0, 0, 0))
        self.text_surface_sec = self.base_font.render(self.text_sec, True, (0, 0, 0))

    def set_speech_delayer(self, new_val):
        self.delayer = new_val

    def get_speech_delayer(self):
        return self.delayer
