import pandas as pd
import numpy as np

file_path = '/Users/tatevikbrsoyan/Desktop/physics_we/Spectrum_of_fruits/Fruit_purees_FTIR.csv'
readfile = pd.read_csv(file_path, header=None)

# Trying to define a custom iloc function to not repeat the code in the lines 15-17

# def iloc_func(row_start, row_end, column_start, column_end):
#    if column_end == None:
#     column_end = len(readfile.columns)
#    return readfile.iloc[row_start:row_end, column_start:column_end].values
  
# wave_numbers1 = iloc_func(4,None,0,None)

wave_numbers = readfile.iloc[4:, 0].values
intensity = readfile.iloc[4:, 1:].values
fruit = readfile.iloc[0:3, 1:].values # shows which fruit it is

fruit_bool = np.array(fruit, dtype=bool)

fruit_names = {
    'Raspberry': 0,
    'Strawberry':1,
    'Neither':2
}

def find_column(array, row_index):
    return np.where(array[row_index])[0]

fruit_columns = {}

for fruit_name, row_index in fruit_names.items():
    fruit_columns[fruit_name] = find_column(fruit_bool, row_index)

# for fruit_name, columns in fruit_columns.items():
#     print(f"{fruit_name}: {columns}")


 


    




 