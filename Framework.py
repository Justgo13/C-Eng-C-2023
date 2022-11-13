from enum import Enum


class Simulator:
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return self.__repr__()


class Environment:
    def __init__(self, temperatures:[], precipitations: [], month:int=0):
        self.month = month
        self.temperatures = temperatures
        self.precipitations = precipitations
        self.set_month(month)
        pass
    def set_month(self, month:int)->None:
        month+=1
        self.temperature = self.temperatures[month%12]
        self.precipitation = self.precipitations[month%12]

    def next_state(self, tiles:dict):
        #todo: Harajp and Kevin check pls
        next_env = Environment(self.temperatures, self.precipitations, self.month)
        next_env.set_month(self.month+1)
        return next_env

    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return self.__repr__()


class PlantType(Enum):
    CONIFEROUS = "CONIFEROUS"
    SHRUB = "SHRUB"
    EVERGREEN = "EVERGREEN"
    WILDFLOWER = "WILDFLOWER"
    PERENNIAL = "PERENNIAL"
    LICHEN = "LICHEN"

class Plant:
    def __init__(self, name:str, type:PlantType, growth_rate:float, max_growth:float, ideal_temp:float, shade_tol:float, seeds_produced:int, seed_dist:int, seed_prod_time:float, life:float):
        # initialize properties of the plant
        self._name = name
        self._type = type
        self._growth_rate = growth_rate
        self._max_growth = max_growth
        self._ideal_temp = ideal_temp
        self._shade_tol = shade_tol
        self._seeds_produced = seeds_produced
        self._seed_dist = seed_dist
        self._seed_prod_time = seed_prod_time
        self._life = life
        # initialize state
        self.init_state()
        pass

    def init_state(self, age:float = 0, height:float=0):
        self.age = age
        self.height = height
        pass

    def next_state(self, tiles:dict):
        #todo: @Harjap and @Kevin
        #yuck thats verbose
        next_plant = Plant(self._name, self._type, self._growth_rate, self._max_growth, self._ideal_temp, self._shade_tol,
              self._seeds_produced, self._seed_dist, self._seed_prod_time, self._life)
        next_plant.init_state(self.age+1, self.height+1)
        return next_plant


    def __repr__(self)->str:
        pass

    def __str__(self)->str:
        return self.__repr__()

    pass


class Tile:
    def __init__(self, plant: Plant, environment: Environment):
        self.plant = plant
        self.environment = environment
        pass

    def next_state(self, tiles:dict):
        next_plant = self.plant.next_state(tiles)
        next_environment = self.environment.next_state(tiles)
        return Tile(next_plant, next_environment)

    def __repr__(self)->str:
        return ""

    def __str__(self)->str:
        return  self.__repr__()
