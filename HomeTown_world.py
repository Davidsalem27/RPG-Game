import pygame as pg
import os
import World_Gui as wg
DELAY_TIME=1

class HomeTown(wg.World_Gui):

    def __init__(self,map,environment):
        super().__init__(map,environment)
        self.house_interaction_first=['Go in?','great']
        self.house_interaction_sec = ['Go in?', 'great']
        self.npc_interaction_first = ['The Age of Exploration','it is not knowledge']
        self.npc_interaction_sec=['is Upon Us!','we lack']
        self.house_interaction_ind=0
        self.enter_house=1#number of 'e' to enter house
        #self.exit_rect=pg.Rect(700,350,5,5)

        #650, 450
    def what_interaction(self,interaction,x,y):
        name = interaction
        for event in pg.event.get():
            if name == 'Home':

                if not self.speech_bubble:
                    self.create_speech_bubble(x, y - 100,
                                            self.house_interaction_first[self.house_interaction_ind],
                                           self.house_interaction_sec[self.house_interaction_ind])

                if event.type==pg.KEYDOWN and event.key==pg.K_e:

                    if self.house_interaction_ind == self.enter_house:
                         return True
                    self.interaction_manager()

            if name == 'Small_House':
                pass
            if name == 'Barbarian':
                self.create_speech_bubble(x,y-100,self.npc_interaction_first[self.house_interaction_ind],
                                           self.npc_interaction_sec[self.house_interaction_ind])
                if event.type==pg.KEYDOWN and event.key==pg.K_e:

                    if self.house_interaction_ind == self.enter_house:
                         return True
                    self.interaction_manager()

    def interaction_manager(self):
        #print(self.house_interaction_ind,len(self.house_interaction_first))
        #print(self.speech_bubble.text_first,self.house_interaction_ind)
        if self.house_interaction_ind == len(self.house_interaction_first):
            self.house_interaction_ind = 0
            #return True ##event should happen

        else:
            self.house_interaction_ind += 1
            if self.house_interaction_ind==len(self.house_interaction_first):
                return
            self.speech_bubble.change_text(self.house_interaction_first[self.house_interaction_ind],
                                       self.house_interaction_sec[self.house_interaction_ind])




    def events(self):

        interaction = self.can_player_interact()  # interaction=(bool,obj.name,x,y)
        if interaction:

            world = self.what_interaction(interaction[1], interaction[2], interaction[3])  # checks what obj and
            # updates the speech bubble to first window
            if self.speech_bubble:

                #print('asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd')
                self.speech_bubble.render()
                self.update_speech_bubble()  # updates speech bubble

            if world:
                return 'house'




class Home(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.name = 'Home'
        # self.image=pg.image.load(os.path.join('Isometric', 'red_house.png')).convert_alpha()
        # self.mask=pg.mask.from_surface(self.image)
        #self.mask=pg.mask.Mask(size=(219,185))
        self.start_x=1320
        self.start_y=580
        self.rect=pg.Rect(1320,580,200,140)
        #print(self.rect.width,self.rect.height,'house')




class Small_House(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.name = 'Small_House'
        self.image = pg.image.load(os.path.join('Isometric', 'little_house.png')).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        # self.mask=pg.mask.Mask(size=(219,185))
        self.rect = self.mask.get_rect()
        self.rect.x, self.rect.y = 550, 540

class Barbarian(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.name='Barbarian'
        self.image = pg.image.load(os.path.join('Isometric', 'L1E.png')).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        # self.mask=pg.mask.Mask(size=(219,185))
        self.rect = self.mask.get_rect()
        self.rect.x, self.rect.y = 800, 400

class Tree(pg.sprite.Sprite):

    def __init__(self,pos_x, pos_y):
        super().__init__()
        self.image=pg.image.load(os.path.join('Isometric','treeHigh_W.png')).convert_alpha()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.rect.update((pos_x, pos_y),(1,1))
        self.location = [pos_x, pos_y]





