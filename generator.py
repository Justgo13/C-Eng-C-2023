from data_getters import load_data
from random import choice
from Framework import PlantName
from data_getters import get_lifespan, get_seed_radius, get_seed_production_time, get_seeds_produced, \
    get_precipitation_preference, get_temperature_preference, get_max_height, get_shade_tolerance, get_growth_rate
import json
import numpy as np


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


if __name__ == '__main__':
    plant_data = load_data()
    environment = 1
    grid_data = []

    """
    each object is

    {
        time: "",
        x: "",
        y: "",
        environment: "",
        plant_data: {
            height: "",
            age: "",
            properties: {
                growthRate: "",
                maxHeight: "",
                shadeTolerance: "",
                precipitationPreference: "",
                temperaturePreference: "",
                seedsProduced: "",
                seedRadius: "",
                seedProductionTime: "",
                lifespan: ""
            }
        }        
    }
    """
    time = 0
    for x in range(100):
        for y in range(100):
            filtered_plant_types = list(PlantName)
            filtered_plant_types.remove(PlantName.NO_TREE)
            bar = choice(filtered_plant_types)

            # get plant values
            lifespan = get_lifespan(plant_data, bar)
            seed_radius = get_seed_radius(plant_data, bar)
            seed_prod_time = get_seed_production_time(plant_data, bar)
            seeds_produced = get_seeds_produced(plant_data, bar)
            precip_peference = get_precipitation_preference(plant_data, bar)
            temp_preference = get_temperature_preference(plant_data, bar)
            max_height = get_max_height(plant_data, bar)
            growth_rate = get_growth_rate(plant_data, bar)
            shade_tolerance = get_shade_tolerance(plant_data, bar)

            grid_data.append({
                "time": time,
                "type": bar.value,
                "name": bar.value,
                "x": x,
                "y": y,
                "environment": environment,
                "properties": {
                    "growthRate": growth_rate,
                    "maxHeight": max_height,
                    "shadeTolerance": shade_tolerance,
                    "precipitationPreference": precip_peference,
                    "temperaturePreference": temp_preference,
                    "seedsProduced": seeds_produced,
                    "seedRadius": seed_radius,
                    "seedProductionTime": seed_prod_time,
                    "lifespan": lifespan
                }
            })

    with open("grid_data.json", "w") as outfile:
        json.dump(grid_data, outfile, cls=NpEncoder, indent=4)
