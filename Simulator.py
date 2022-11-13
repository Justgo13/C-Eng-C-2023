from Framework import *
from data_getters import *
from env_getter import *
import numpy as np
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

class SimulationState:
    def __init__(self, grid):
        self.__grid = grid
        pass

    def next_month(self)->None:
        # update month
        next_grid = []
        for i in range(0, len(self.__grid)):
            next_grid.append([])
            for j in range(0, len(self.__grid[i])):

                next_grid[-1].append(self.__grid[i][j].next_state(i, j, self.__grid))
            self.__grid = next_grid
        pass

    def to_dict(self, time:int):
        output = {"time":time}
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                output[f'{i},{j}'] = self.__grid[i][j].to_dict()
        return output


class SimulationRunner:
    def __init__(self, state:SimulationState, outputfile:str,start_time:int=0, end_time:int=400*12):
        self.__state = state
        self.__start_time = start_time
        self.__end_time = end_time
        self.__outputfile = outputfile

    def run(self) -> None:
        past_states = [self.__state.to_dict(0)]
        for current_time in range(self.__start_time, self.__end_time):
            self.__state.next_month()
            past_states+=[self.__state.to_dict(current_time)]
            pass
        self.save_state(past_states)

    def save_state(self, past_states:list) -> None:
        with open(self.__outputfile, 'w') as file:
            file.write(json.dumps(past_states,cls=NpEncoder))
            pass
        pass
    pass


if __name__ == '__main__':
    #example
    
    # e = Environment([0,1,2,3,4,5],[2,4,5,78])
    df_env_1 = load_data_env_1()
    df_env_2 = load_data_env_2()
    df = load_data()


    temperatures_1 = get_temp(df_env_1)
    temperatures_2 = get_temp(df_env_2)

    precipitation_1 = get_precipitation(df_env_1)
    precipitation_2 = get_precipitation(df_env_2)

    e = Environment(temperatures_1, precipitation_1)


    

    p = Plant("name", PlantName.BALSAM_FIR, 1, 2, 3, 4, 5, 6, 7, 200)
    t= Tile(p,e)
    # t_list = []
    # t_list_total = [[]]
    # for i in range(0,100):
    #     t_list.append(t)
    matrix = [[0 for x in range(100)] for y in range(100)]
    
    # for i in range(0,100):
    #     t_list_total[i].append(t_list)

    for x in range(0,100):
        for y in range(0,100):
            matrix[x][y] = t


    # print(matrix)
    s = SimulationState(matrix)
    s2 = SimulationRunner(s,'results.json',0,1)
    s2.run()