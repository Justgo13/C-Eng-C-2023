from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

import Framework
import pandas as pd
import os


def load_data_env_1():
    # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    filePath = os.path.abspath(os.path.dirname('env1.csv'))
    data = pd.read_csv(filePath + '/C-Eng-C-2023/env1.csv')
    df = pd.DataFrame(data)
    return df

def load_data_env_2():
    # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    filePath = os.path.abspath(os.path.dirname('env2.csv'))
    data = pd.read_csv(filePath + '/C-Eng-C-2023/env2.csv')
    df = pd.DataFrame(data)
    return df


def get_temp(df):
    return df["Temperature"]


def get_precipitation(df):
    return df["Percipitation"]