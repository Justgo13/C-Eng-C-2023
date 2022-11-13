from Framework import *
from env_getter import get_temp, get_precipitation, load_data
import json
import numpy as np


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

    def next_month(self) -> None:
        # update month
        next_grid = []
        for i in range(0, len(self.__grid)):
            next_grid.append([])
            for j in range(0, len(self.__grid[i])):
                next_grid[-1].append(self.__grid[i][j].next_state(i, j, self.__grid))
            self.__grid = next_grid
        pass

    def to_dict(self, time: int):
        output = {"time": time}
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                output[f'{i},{j}'] = self.__grid[i][j].to_dict()
        return output


class SimulationRunner:
    def __init__(self, state: SimulationState, outputfile: str, start_time: int = 0, end_time: int = 400 * 12):
        self.__state = state
        self.__start_time = start_time
        self.__end_time = end_time
        self.__outputfile = outputfile

    def run(self) -> None:
        past_states = [self.__state.to_dict(0)]
        for current_time in range(self.__start_time, self.__end_time):
            self.__state.next_month()
            past_states += [self.__state.to_dict(current_time)]
            pass
        self.save_state(past_states)

    def save_state(self, past_states: list) -> None:
        with open(self.__outputfile, 'w') as file:
            file.write(json.dumps(past_states, cls=NpEncoder))
            pass
        pass

    pass


if __name__ == '__main__':
    # exampled
    data = load_data()
    env_temps = get_temp(data)
    env_precipitation = get_precipitation(data)

    e = Environment(env_temps, env_precipitation)

    with open('grid_data.json') as f:
        grid_data = json.load(f)

    tiles = []
    for data in grid_data:
        p = Plant(data["name"], data["type"], data["properties"]["growthRate"], data["properties"]["maxHeight"],
                  data["properties"]["temperaturePreference"], data["properties"]["shadeTolerance"],
                  data["properties"]["seedsProduced"], data["properties"]["seedRadius"],
                  data["properties"]["seedProductionTime"], data["properties"]["lifespan"],
                  data["properties"]["precipitationPreference"])
        tiles.append([Tile(p, e)])

    s = SimulationState(tiles)
    s2 = SimulationRunner(s, 'results.json', 0, 1)
    s2.run()