import matplotlib.pyplot as plt
from Simulator import *
from Framework import *
import json

def read_sim_data(output):
    snapshots = []

    with open(output) as f:
        data = json.load(f)
        for frame in data:
            x_vals = []
            y_vals = []
            info = []
            for key, value in frame.items():
                if key == 'time':
                    continue
                x, y=key.split(',')
                print(x,y)
                x_vals.append(int(x))
                y_vals.append(int(y))
                tile = value
                plant = tile['plant']
                name = plant['name']
                age = plant['age']
                height = plant['height']
                info.append({'name': name, 'age': age, 'height': height})
                pass
            snapshots.append({'info':info, 'x':x_vals, 'y':y_vals})
            break
    return snapshots


snapshots = read_sim_data("results.json")


cm = plt.get_cmap('rainbow')

info = snapshots[-1]['info']
x = snapshots[-1]['x']
y= snapshots[-1]['y']

names = []
name_set = set()
for i in info:
    names.append(i['name'])
    name_set.add(i['name'])
    pass

color_map = {}
for i, entry in zip(range(len(name_set)), name_set):
    color_map[entry]=cm(int(255*i/len(name_set)))
    pass

c = []
for name in names:
    c.append(color_map[name])


norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn

fig,ax = plt.subplots()
sc = plt.scatter(x, y, c=c, s=1, norm=norm)


plt.show()