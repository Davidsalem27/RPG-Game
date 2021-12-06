import World_Gui as wg
import World_Logic as wl
import HomeTown_world as htw
import House_world as hw
import pygame as pg
import os
import Backgrounds
WHITE=(255,255,255)
free_roam_objs={}
free_roam_environment=[]#,htw.Small_House(),htw.Barbarian()]
home_environment=[]
# hometown_map=pg.image.load(os.path.join('Isometric','map2.png')).convert_alpha()
# house_map=pg.image.load(os.path.join('Isometric', 'home.png')).convert_alpha()
Color=pg.Color('white')
house_map = pg.image.load(os.path.join('Isometric', 'home.png')).convert_alpha()
WIDTH,HEIGHT=1536,864
center_x,center_y=400,400
class World:


    def __init__(self,WIN):
        self.WIN=WIN
        self.gui=None
        self.logic=wl.World_L()
        self.hero_logic=wl.Hero(5,5,5,5,5)
        self.text=None
        self.map = pg.image.load(os.path.join('Isometric','bigmap.png')).convert_alpha()
        #self.load_background()
        self.switch_screen('hometown')
        self.map_to_draw=pg.sprite.Group()

        self.border_rect=pg.Rect(0,0,3072,1728)

    def load_background(self):
        self.map=pg.image.load(os.path.join('Isometric','bigmap.png')).convert_alpha()
        #self.map_to_draw.add(self.map)


    def events(self):

        #keys = pg.key.get_pressed()
        switch=self.gui.events()
        if switch != None:
            self.switch_screen(switch)

        self.gui.move_player(self.border_rect)
        print(self.border_rect.x,self.border_rect.y)
    def switch_to_next(self):
        if self.gui.hero.rect.x>0:
            self.WIN.blit(house_map, (WIDTH-self.gui.hero.rect.x, 0))

    def switch_screen(self,world):
        if self.gui:
            self.gui.delete_environment()
        if world == 'house':
            self.border_rect.x,self.border_rect.y=0,0


            self.WIN.fill(WHITE)
            map = pg.image.load(os.path.join('Isometric', 'home.png')).convert_alpha()
            self.map=map

            self.gui=hw.House_World(house_map,home_environment)

            self.gui.hero.rect.x, self.gui.hero.rect.y = 200, 200

        if world == 'hometown':
            self.WIN.fill(WHITE)

            self.gui = htw.HomeTown(self.map, free_roam_environment)
            self.gui.environment.append(htw.Home())
            #self.WIN.blit(self.gui.map,(0,0))

            self.gui.hero.rect.x, self.gui.hero.rect.y = center_x,center_y
