import pandas as pd
import numpy as np

file_path = '/Users/tatevikbrsoyan/Desktop/physics_we/Spectrum_of_fruits/Fruit_purees_FTIR.csv'
readfile = pd.read_csv(file_path, header=None)

def iloc_func(file, row_start, row_end, column_start, column_end):
   if column_end == None and row_end == None:
      value = file.iloc[row_start:, column_start:]
   elif column_end == None:
    value = file.iloc[row_start:row_end, column_start:]
   elif row_end == None:
    value = file.iloc[row_start:, column_start:column_end]
   return value
  
wave_numbers = iloc_func(readfile, 4, None, 0, 1)
intensity = iloc_func(readfile, 4, None, 1, None)
fruit = iloc_func(readfile, 0,3,1,None)

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
