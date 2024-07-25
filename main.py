import pandas as pd
import numpy as np

file_path = '/Users/tatevikbrsoyan/Desktop/physics_we/Spectrum_of_fruits/Fruit_purees_FTIR.csv'
d = pd.read_csv(file_path, header=None)

wave_numbers = d.iloc[4:, 0].values
intensity = d.iloc[4:, 1:].values
fruit = d.iloc[0:3, 1:].values # shows which fruit it is

fruit_bool = np.array(fruit, dtype=bool)

raspberry_columns = np.where(fruit_bool[0])[0]
strawberry_columns = np.where(fruit_bool[1])[0]
neither_columns = np.where(fruit_bool[2])[0]


print("Raspberry columns:")
for index in raspberry_columns:
    print(f"Column {index + 1}: Raspberry")
    print(intensity[:, index])  

print("\nStrawberry columns:")
for index in strawberry_columns:
    print(f"Column {index + 1}: Strawberry")
    print(intensity[:, index])  

print("\nNeither columns:")
for index in neither_columns:
    print(f"Column {index + 1}: Neither")
    print(intensity[:, index])  


 


    




 