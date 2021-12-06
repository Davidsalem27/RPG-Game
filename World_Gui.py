import pygame as pg
import os
import speech
FONT_SIZE=20
STEP=5
DELAY_TIME=7
#main_map=pg.image.load(os.path.join('Isometric','map2.png')).convert_alpha()



class World_Gui:

    def __init__(self,map,environment):
        self.map=map
        self.environment_to_draw=pg.sprite.Group()
        self.humans_to_draw=pg.sprite.Group()
        self.speech_bubble=0
        self.environment=[]
        self.hero=Hero()
        self.obj_created={}
        self.create_human()
        self.create_environment(environment)
        self.hero_direction='w'
        self.speech_bubble=None

    def create_environment(self,environment):

        for i in environment:

            self.obj_created[i.name]=id(i)
            self.environment.append(i)
            self.environment_to_draw.add(i)

    def delete_environment(self):
        self.environment_to_draw.empty()
        self.environment = []
        self.speech_bubble=None
    def create_human(self):
        self.humans_to_draw.add(self.hero)
    def change_map(self,new_map):
        self.map=new_map

    def move_player(self,map_rect):

        keys = pg.key.get_pressed()
        if True in keys:
            self.get_input_vertical(keys)
            self.can_move_vertical(map_rect)
            if self.hero.direction.y>0:
                if map_rect.y > 0:

                    self.hero.direction.y = 0

            if self.hero.direction.y<0:
                if abs(map_rect.y)>map_rect.y+(map_rect.height):
                    self.hero.direction.y = 0

            map_rect.y += self.hero.direction.y
            self.environment[0].rect.y+=self.hero.direction.y

            # self.hero.rect.y += self.hero.direction.y
            # self.hero.direction.y=0
            self.get_input_horizontal(keys)
            self.can_move_horizontal(map_rect)
            if self.hero.direction.x>0:
                if map_rect.x > 0:

                    self.hero.direction.x = 0

            if self.hero.direction.x<0:
                if abs(map_rect.x)>map_rect.x+(map_rect.width)-50:
                    self.hero.direction.x = 0

            map_rect.x += self.hero.direction.x
            self.environment[0].rect.x += self.hero.direction.x
            self.hero.direction.x = 0

            self.hero.direction.y = 0

    def get_input_vertical(self,keys):
        if keys[pg.K_w] and self.hero.rect.y > 0:
            self.hero.direction.y+=STEP
            self.hero_direction = 'w'
        if keys[pg.K_s] and self.hero.rect.y < 800:
            self.hero.direction.y -= STEP
            self.hero_direction += 's'



    def get_input_horizontal(self,keys):
        if keys[pg.K_d] and self.hero.rect.x < 1500:
            self.hero.direction.x -= STEP
            self.hero_direction = 'd'
        if keys[pg.K_a] and self.hero.rect.x > 0:
            self.hero.direction.x += STEP
            self.hero_direction = 'a'

    def can_move_vertical(self,first_background):
        offset=0
        for obj in self.environment:

            # print(obj.rect.x, '1')
            # print(self.hero.rect.x, '2')
            # print(obj.rect.x+obj.rect.width,'3')
            # print(self.hero.rect.y,'a')
            # print(obj.rect.y,'b')
            # print(obj.rect.height)
            # print(self.hero.direction.y)
            # print(obj.rect.y + obj.rect.height,'c')
            if obj.rect.x<self.hero.rect.x:
                if obj.rect.x<self.hero.rect.x+self.hero.rect.width-STEP<obj.rect.x+obj.rect.width:
                    if self.hero.direction.y<0:

                        if obj.rect.y<=self.hero.rect.y+self.hero.rect.height+self.hero.direction.y<obj.rect.y+obj.rect.height:
                            self.hero.direction.y = 0
                    if self.hero.direction.y > 0:

                        if obj.rect.y<self.hero.rect.y+self.hero.direction.y<=obj.rect.y+obj.rect.height:
                            self.hero.direction.y = 0
            if obj.rect.x>self.hero.rect.x:

                if obj.rect.x<=self.hero.rect.x-STEP<obj.rect.x+obj.rect.width:

                    if self.hero.direction.y<0:
                        if obj.rect.y<self.hero.rect.y+self.hero.rect.height+self.hero.direction.y<obj.rect.y+obj.rect.height:
                            self.hero.direction.y = 0
                    if self.hero.direction.y > 0:
                        if obj.rect.y<self.hero.rect.y+self.hero.direction.y<obj.rect.y+obj.rect.height:
                            self.hero.direction.y = 0



    def can_move_horizontal(self,first_background):
        offset=0
        for obj in self.environment:

            if obj.rect.y < self.hero.rect.y+self.hero.rect.height:
                if obj.rect.y<self.hero.rect.y+self.hero.rect.height-STEP<obj.rect.y+obj.rect.height :

                    if self.hero.direction.x<0:

                        if obj.rect.x<=self.hero.rect.x+self.hero.rect.width+self.hero.direction.x<obj.rect.x+obj.rect.width:
                            self.hero.direction.x = 0
                    if self.hero.direction.x > 0:

                        if obj.rect.x<self.hero.rect.x+self.hero.direction.x<=obj.rect.x+obj.rect.width:
                            self.hero.direction.x = 0
            if obj.rect.y > self.hero.rect.y:

                if obj.rect.y<self.hero.rect.y+self.hero.direction.y<obj.rect.y+obj.rect.height:

                    if self.hero.direction.x<0:
                        if obj.rect.x<self.hero.rect.x+self.hero.rect.width+self.hero.direction.x<obj.rect.x+obj.rect.width:
                            self.hero.direction.x = 0
                    if self.hero.direction.x > 0:
                        if obj.rect.x<self.hero.rect.x+self.hero.direction.x<obj.rect.x+obj.rect.width:
                            self.hero.direction.x = 0


    def can_player_interact(self):

        for obj in self.environment:

            if obj.rect.y+obj.rect.height+65>self.hero.rect.y+self.hero.rect.height>obj.rect.y-50:
                if obj.rect.x-50<self.hero.rect.x+self.hero.rect.width<obj.rect.x+obj.rect.width+50:

                    return (True,obj.name,obj.start_x,obj.start_y)

    def update_speech_bubble(self):
        """
        inorder to change text we need to blit over the old one
        :return:
        """

        self.map.blit(self.speech_bubble.image, (self.speech_bubble.rect.x, self.speech_bubble.rect.y))

        self.map.blit(self.speech_bubble.text_surface_first, (self.speech_bubble.rect.x, self.speech_bubble.rect.y))
        self.map.blit(self.speech_bubble.text_surface_sec, (self.speech_bubble.rect.x, self.speech_bubble.rect.y+25))

    def create_speech_bubble(self,x,y,first_line,sec_line):

        self.speech_bubble=speech.Speech_Bubble(x,y,first_line,sec_line)






class Hero(pg.sprite.Sprite):

    def __init__(self):
        self.name = 'Hero'
        super().__init__()
        self.walkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'),
                     pg.image.load('R5.png'), pg.image.load('R6.png'), pg.image.load('R7.png'), pg.image.load('R8.png'),
                     pg.image.load('R9.png')]
        self.walkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'),
                    pg.image.load('L5.png'), pg.image.load('L6.png'), pg.image.load('L7.png'), pg.image.load('L8.png'),
                    pg.image.load('L9.png')]
        self.current_sprite=0
        self.image=self.walkRight[self.current_sprite]
        self.mask = pg.mask.from_surface(self.image)
        self.rect=self.mask.get_rect()
        self.rect.width,self.rect.height=10,35
        self.direction=pg.math.Vector2(0, 0)
        self.last_pos_x,self.last_pos_y = 0,0
        self.go_right = False
        self.go_left = False


    # def animate(self,d):
    ###to deal with later
    #     if d == 'r':
    #         self.go_right = True
    #     else:
    #         self.go_left = True
    # def update(self):
    #     if self.go_right:
    #         if self.current_sprite>=len(self.walkRight)-1:
    #             self.current_sprite=-1
    #             self.go_right = False
    #         self.current_sprite+=.4
    #         self.image=self.walkRight[int(self.current_sprite)]
    #     if self.go_left:
    #         if self.current_sprite>=len(self.walkLeft)-1:
    #             self.current_sprite=-1
    #             self.go_left = False
    #         self.current_sprite+=.4
    #         self.image=self.walkLeft[int(self.current_sprite)]
    def move(self,new_loc):
        self.rect.x = self.rect.x + new_loc[0]
        self.rect.y = self.rect.y + new_loc[1]



