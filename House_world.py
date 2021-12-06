import pygame as pg
import os
import World_Gui as wg
DELAY_TIME=7
class House_World(wg.World_Gui):

    def __init__(self,map,environment):
        super().__init__(map,environment)
        self.house_interaction_first = ['Go in?', 'great']
        self.house_interaction_sec = ['Go in?', 'great']
        self.bed_interaction=['take a nap?','good night!']
        self.house_interaction_ind = 0
        self.exit_house = 1  # number of 'e' to exit house
        self.chest_ind = 1 # number of 'e' to open chest
        self.bed_ind = 1
        self.environment.append(Exit_house())
        self.environment.append(Bed())

    def what_interaction(self,interaction,x,y):
        name = interaction
        for event in pg.event.get():
            if name == 'exit':
                if not self.speech_bubble:
                    self.create_speech_bubble(x, y - 100,
                                              self.house_interaction_first[self.house_interaction_ind],
                                              self.house_interaction_sec[self.house_interaction_ind])

                if event.type == pg.KEYDOWN and event.key == pg.K_e:

                    if self.house_interaction_ind == self.exit_house:
                        return True
                    self.interaction_manager()
            if name == 'bed':
                if not self.speech_bubble:
                    self.create_speech_bubble(x, y - 100,
                                              self.house_interaction_first[self.house_interaction_ind],
                                              self.house_interaction_sec[self.house_interaction_ind])

                if event.type == pg.KEYDOWN and event.key == pg.K_e:

                    if self.house_interaction_ind == self.exit_house:
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

                self.speech_bubble.render()
                self.update_speech_bubble()#blits on screen
            if world:

                return 'hometown'

class Exit_house:
    def __init__(self):
        self.name='exit'
        self.rect = pg.Rect(900, 350, 10, 10)


class Chest(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name='Chest'
        #self.image = pg.image.load(os.path.join('Isometric', 'chest.png')).convert_alpha()
        #self.mask = pg.mask.from_surface(self.image)
        # self.mask=pg.mask.Mask(size=(219,185))
        self.rect = pg.Rect(700,450,35,32)
        # self.rect.x, self.rect.y = 700, 450
        # self.rect.width,self.rect.height=35,32




class Bed:
    def __init__(self):
        super().__init__()
        self.name='bed'
        #self.image = pg.image.load(os.path.join('Isometric','bed.png')).convert_alpha()
        self.rect = pg.Rect(485,505,65,85)
