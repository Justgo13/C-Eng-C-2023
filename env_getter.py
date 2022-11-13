from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

import Framework
import pandas as pd


def load_data():
    # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    data = pd.read_csv('env1.csv')
    df = pd.DataFrame(data)
    return df


def get_temp(df):
    return df["Temperature"]


def get_precipitation(df):
    return df["Percipitation"]