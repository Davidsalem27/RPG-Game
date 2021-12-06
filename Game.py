import pygame as pg
import os
import Environment_Classes as ec
import Human_Classes as hc
import random
import World_Gui as wg
pg.font.init()

WIDTH, HEIGHT = 800, 800
pg.display.set_caption('Age of Expansion')
WHITE=(255,255,255)
FPS=60
STEP=5
base_font = pg.font.Font(None,40)

def main():

    clock = pg.time.Clock()
    menu=Main_Menu(WIN,clock)
    game = Game(WIN, clock)
    while menu.soft_run:
        menu.run()

        if menu.start:
            game.playing=True
            while game.playing:
                print('ehe')
                game.run()
                menu.start=False
    # game=Game(WIN,clock)
    #

class Main_Menu:

    def __init__(self,background,clock):
        self.background = background
        self.clock = clock
        self.menu_background = pg.image.load(os.path.join('Isometric','main_menu_background2.png')).convert_alpha()
        self.soft_run=True
        self.start=False
        self.button1_text='Play'
        self.button2_text='Quit'
        self.button1_img = pg.image.load(os.path.join('Isometric', 'text_background.png')).convert_alpha()
        self.button2_img = pg.image.load(os.path.join('Isometric', 'text_background.png')).convert_alpha()
        self.button1_rect = self.button1_img.get_rect()
        self.button2_rect = self.button2_img.get_rect()
        #self.rect.width, self.rect.height = 70, 50
        self.button1_surf = base_font.render(self.button1_text, True, (0, 0, 0), )
        self.button2_surf = base_font.render(self.button2_text, True, (0, 0, 0), )
        pg.mouse.set_pos([750, 200])
    def run(self):
        pg.font.init()

        self.clock.tick(60)
        WIN.fill(WHITE)
        WIN.blit(self.menu_background, (0, 0))
        self.menu_background.blit(self.button1_img, (750,200))
        self.menu_background.blit(self.button1_surf, (750,200))
        self.menu_background.blit(self.button2_img, (750,400))
        self.menu_background.blit(self.button2_surf, (750,400))


        self.events()
        pg.display.update()

    def events(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s]:
            pg.mouse.set_pos(750,400)
        if keys[pg.K_w]:
            pg.mouse.set_pos(750,200)
        if pg.mouse.get_pos()==(750,200) and keys[pg.K_e]:

            self.start = True
        if pg.mouse.get_pos()==(750,400) and keys[pg.K_e]:

            self.soft_run = False
        self.quit(keys)
    def quit(self,keys):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.soft_run = False
        if keys[pg.K_t]:
            self.soft_run = False



class Game:

    def __init__(self,background,clock):
        self.background=background
        self.clock=clock
        self.map_blit=0
        self.playing = True
        self.fighting = False
        self.current_state='world'

        self.world_map=World.World(WIN)

    def run(self):
        pg.font.init()
        while self.playing:
            self.clock.tick(60)
            if self.fighting:
                self.switch_screen('battle')
            else:

                self.switch_screen('world')


            self.events()
            self.update()
            #self.draw()


    def events(self):
        self.quit()

        #
        # if pg.sprite.collide_rect(self.hero,self.enemy):
        #     self.start_battle()


    # def start_battle(self):
    #     self.fighting = True
    #     Battle=Battle_System(self.hero_team,self.enemy_team)
    #     self.screen.switch_screen('battle')

    def update(self):
        pass
        #mouse = pg.mouse.get_pressed()##########create tree with mouse click
        # if mouse[0]:
        #     current = pg.mouse.get_pos()

        #     everything_to_draw.add(ec.Tree(current[0], current[1]))
    def quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            # if event.type==pg.KEYDOWN:
            #
            #     if event.key==pg.K_ESCAPE:
            #         self.playing = False
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            self.playing = False



    def world_screen(self):
        WIN.fill(WHITE)
        WIN.blit(self.world_map.map,(self.world_map.border_rect.x,self.world_map.border_rect.y))
        self.world_map.gui.environment_to_draw.draw(WIN)
        self.world_map.gui.humans_to_draw.draw(WIN)
        self.world_map.events()

        pg.display.update()



    def battle_screen(self):
        WIN.fill(WHITE)##restarts the screen
        WIN.blit(battle_img, (0, 0))
        team_a.draw(WIN)
        team_b.draw(WIN)
        pg.display.flip()

    def switch_screen(self,new_state):
        self.current_state=new_state
        #print(new_state,self.fighting)
        if self.current_state == 'world':
            self.world_screen()
        if self.current_state == 'battle':
            self.battle_screen()


if __name__ == '__main__':
    pg.font.init()
      # size of window
    WIN = pg.display.set_mode((0,0),pg.FULLSCREEN)  # opens window
    print(WIN.get_size())
    import World

    pg.mouse.set_visible(True)
    pg.key.set_repeat()
    main()