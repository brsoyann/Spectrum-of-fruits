import pandas as pd
import numpy as np
from fruit_data import fruitData
import srcread

with open('source.txt', 'r') as src:
    lines = src.readlines()

file_path = srcread.findparameterByType(lines, 'path')
readfile = pd.read_csv(file_path, header=None)

Data = fruitData(readfile)
wave_numbers = Data.iloc_func(4, None, 0, 1)
intensity = Data.iloc_func(4, None, 1, None)
fruit = Data.iloc_func(0, 3, 1, None)

fruit_bool = np.array(fruit, dtype=bool)

fruit_names = {
    'Raspberry': 0,
    'Strawberry': 1,
    'Neither': 2
}

def find_column(array, row_index):
    return np.where(array[row_index])[0]

fruit_columns = {}

for fruit_name, row_index in fruit_names.items():
    fruit_columns[fruit_name] = find_column(fruit_bool, row_index)

for fruit_name, columns in fruit_columns.items():
    print(f"{fruit_name}: {columns}")
