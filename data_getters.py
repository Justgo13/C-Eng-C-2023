from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

import Framework
from Framework import PlantName
import pandas as pd


def load_data():
    # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    data = pd.read_csv('plants.csv')
    df = pd.DataFrame(data)
    return df


def get_growth_rate(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Growth Rate'].iloc[0]


def get_max_height(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Maximum Height'].iloc[0]


def get_shade_tolerance(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Shade tolerance'].iloc[0]


def get_precipitation_preference(df, plant_name):
    # convert 500-1000 to [500,1000]
    val = df.loc[df["Plant Name"] == plant_name.value]['Precipitation Preference'].iloc[0]
    val = val.split('-')
    return val


def get_temperature_preference(df, plant_name):
    # convert -10 to 15 to [-10,15]
    val = df.loc[df["Plant Name"] == plant_name.value]['Temperature Preference'].iloc[0]
    val = val.split(' to ')
    return val


def get_seeds_produced(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Seeds produced'].iloc[0]


def get_seed_radius(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Seed radius'].iloc[0]


def get_seed_production_time(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Seed production time'].iloc[0]


def get_lifespan(df, plant_name):
    return df.loc[df["Plant Name"] == plant_name.value]['Lifespan'].iloc[0]