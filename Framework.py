from enum import Enum
import json


class Environment:
    def __init__(self, temperatures:list, precipitations: list, month: int = 1):
        self.month = month
        self.temperatures = temperatures
        self.precipitations = precipitations
        self.set_month(month)
        pass

    def set_month(self, month:int)->None:
        month -= 1
        self.temperature = self.temperatures[month % len(self.temperatures)]
        self.precipitation = self.precipitations[month % len(self.temperatures)]

    def next_state(self, x:int, y:int, tiles:list):
        #todo: Harajp and Kevin check pls
        next_env = Environment(self.temperatures, self.precipitations, self.month)
        next_env.set_month(self.month+1)
        return next_env

    def to_dict(self):
        output = {"temperature": self.temperature,
                  "precipitation": self.precipitation}
        return output


class PlantName(Enum):
    BLACK_SPRUCE = "Black Spruce"
    SUGAR_MAPLE = "Sugar Maple"
    BIGTOOTH_ASPEN = "Bigtooth Aspen"
    BALSAM_POPLAR = "Balsam Poplar"
    JACK_PINE = "Jack Pine"
    BALSAM_FIR = "Balsam Fir"
    SPECKLED_ALDER = "Speckled Alder"
    HOBBLE_BUSH = "Hobblebush"
    SHEEP_LAUREL = "Sheep Laurel"
    RED_ELDERBERRY = "Red Elderberry"
    LEATHER_LEAF = "Leatherleaf"
    BLACK_MEDIC = "Black Medic"
    BUNCH_BERRY = "BunchBerry"
    REINDEER_LICHEN = "Reindeer Lichen"
    GROUND_CEDAR = "Ground Cedar"
    BRACKEN_FERN = "Bracken Fern"
    NO_TREE = ""


class Plant:
    def __init__(self, name:str, type:PlantName, growth_rate:float, max_growth:float, ideal_temp:float, shade_tol:float, seeds_produced:int, seed_dist:int, seed_prod_time:float, life:float):
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

    def next_state(self, x,y, tiles:dict):
        #todo: @Harjap and @Kevin
        #yuck thats verbose
        next_plant = Plant(self._name, self._type, self._growth_rate, self._max_growth, self._ideal_temp, self._shade_tol,
              self._seeds_produced, self._seed_dist, self._seed_prod_time, self._life)
        next_plant.init_state(self.age+1, self.height+1)
        return next_plant


    def to_dict(self):
        output = {
            "name": self._name,
            "age": self.age,
            "height": self.height
        }
        return output
    pass


class Tile:
    def __init__(self, plant: Plant, environment: Environment):
        self.plant = plant
        self.environment = environment
        pass

    def next_state(self, x:int, y:int, tiles:dict):
        next_plant = self.plant.next_state(x,y,tiles)
        next_environment = self.environment.next_state(x,y,tiles)

        return Tile(next_plant, next_environment)

    def to_dict(self):
        output = {"plant": self.plant.to_dict(),
                  "environment": self.environment.to_dict()}
        return output

