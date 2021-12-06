##resource order = gold,wood,food,metal



class Player:

    def __init__(self,state):
        self.state=state
        self.production=bc.Production(0,[0],0,0,0)
    def build(self,type):
        building=self.what_building(type)#building is an [obj,str]
        self.add_workers(building)
        self.cost(building[1])
    def attack_unit(self,attacker,enemy):
        Battle_system([attacker],[enemy])
    def single_cycle(self):
        self.state.add_resources(self.production.calculate_expenses())
    def what_building(self,type):
        """
        recognisez type and returns the object
        :return: [building,name of building]
        """
        for i in BUILDING_DICT:
            if i==type:
                return [BUILDING_DICT[i],i]
    def add_workers(self,building):
        building_dict={'market':2}
        for i in building_dict:
            if i==building[1]:
                building[0].num_of_workers+=1
                worker=cc.Worker()
                self.state.add_citizen(worker)
                building[0].workers.append(worker)
                self.state.add_building(building[0])
    def cost(self,type):
        building_dict={'market':[-5,-10,-5,-10],'mine':[-5,-10,-5,-10],'lumbermill':[-5,-10,-5,-10],'farm':[-5,-10,-5,-10]}
        for i in building_dict:
            if i ==type:
                self.state.add_resources(building_dict[i])

class State:
    def __init__(self):
        self.buildings=[]
        self.citizens=[]
        self.gold=100
        self.food=100
        self.wood=100
        self.metal=100

    def add_building(self,building):
        self.buildings.append(building)
    def remove_building(self,building):
        self.buildings.remove(building)
    def add_citizen(self,citizen):
        self.citizens.append(citizen)
    def remove_citizen(self,citizen):
        self.citizens.remove(citizen)
    def add_resources(self,resources):#resources=[gold,wood,food,metal]
            self.gold+=resources[0]
            self.wood+=resources[1]
            self.food+=resources[2]
            self.metal+=resources[3]
    def get_buildings(self):
        print(self.buildings)
        print(len(self.buildings))
    def get_citizens(self):
        print(self.citizens)
        print(len(self.citizens))


class Battle_system:

    def __init__(self,team_a,team_b):#teams = [obj,obj...]
        self.team_a=team_a
        self.team_b=team_b
        self.battle()
    def single_exchange(self,fighter_a,fighter_b,ind):
        print(ind)
        fighter_a.take_damage(fighter_b.get_damage())
        fighter_b.take_damage(fighter_a.get_damage())
        if fighter_a.health<0:
            del self.team_a[ind]
        if fighter_b.health<0:
            del self.team_b[ind]
        print(fighter_b.health,fighter_a.health)
    def battle(self):
        while len(self.team_a)>0 and len(self.team_b)>0:
            for ind in range(len(self.team_a)):
                self.single_exchange(self.team_a[ind],self.team_b[ind],ind)
        if len(self.team_a)>0:
            return 
            print ('Victory')
        else:
            print('Defeat')


if __name__ == '__main__':
    import Building_Classes as bc
    import Citizen_Classes as cc
    David=Player(State())
    COST_BUILDING_DICT={'market':[5,10,5,10],'mine':[5,10,5,10],'lumbermill':[5,10,5,10],'farm':[5,10,5,10]}
    BUILDING_DICT={'market':bc.Market([cc.Worker()])}
    x=Battle_system([cc.Warrior()],[cc.Barbarian(),cc.Barbarian()])

