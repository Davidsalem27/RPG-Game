import pygame as pg
import os
FONT_SIZE=30
class In_game_menu(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_font = pg.font.Font(None, FONT_SIZE)
        self.image=pg.image.load(os.path.join('Isometric', 'pause_menu.png')).convert_alpha()
        self.rect=self.image.get_rect()
        self.party='Party'
        self.inventory='Inventory'
        self.skills='Skills'
        self.exit='Exit'
        self.party_surface = self.base_font.render(self.party, True, (0, 0, 0), )
        self.inventory_surface = self.base_font.render(self.inventory, True, (0, 0, 0), )
        self.skills_surface = self.base_font.render(self.skills, True, (0, 0, 0), )
        self.exit_surface = self.base_font.render(self.exit, True, (0, 0, 0), )
        self.menu_options={0:'Party',1:'Inventory',2:'Skills',3:'Exit to main menu'}
        self.ind=0
        self.cursor=Menu_Cursor(self.rect.x,self.rect.y)
        self.blit_options()
    def blit_options(self):
        self.image.blit(self.party_surface,(self.rect.x+50,self.rect.y+90))
        self.image.blit(self.inventory_surface, (self.rect.x+50, self.rect.y + 160))
        self.image.blit(self.skills_surface, (self.rect.x+50, self.rect.y + 230))
        self.image.blit(self.exit_surface, (self.rect.x+50, self.rect.y + 300))
        #self.image.blit(self.cursor.image,(self.cursor.rect.x,self.cursor.rect.y+90))
    def update_cursor(self,keys):
        if keys[pg.K_w]:
            self.cursor.rect.y+=70
        if keys[pg.K_s]:
            self.cursor.rect.y-=70


class Menu_Cursor(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pg.image.load(os.path.join('Isometric', 'cursor_img.png')).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=x,y
    def set_rect(self,x,y):
        self.rect.x,self.rect.y=x,y
