import pandas as pd
import numpy as np


file_path = '/Users/tatevikbrsoyan/Desktop/physics_we/Spectrum_of_fruits/Fruit_purees_FTIR.csv'
d = pd.read_csv(file_path, header=None)


wave_numbers = d.iloc[4:, 0].values
intensity = d.iloc[4:, 1:].values
fruit = d.iloc[0:3, 1:].values


fruit_bool = np.array(fruit, dtype=bool)


raspberry_columns = np.where(fruit_bool[0])[0]
strawberry_columns = np.where(fruit_bool[1])[0]
neither_columns = np.where(fruit_bool[2])[0]


print("Raspberry columns:")
for col_idx in raspberry_columns:
    print(f"Column {col_idx + 1}: Raspberry")
    print(intensity[:, col_idx])  

print("\nStrawberry columns:")
for col_idx in strawberry_columns:
    print(f"Column {col_idx + 1}: Strawberry")
    print(intensity[:, col_idx])  

print("\nNeither columns:")
for col_idx in neither_columns:
    print(f"Column {col_idx + 1}: Neither")
    print(intensity[:, col_idx])  


 


    




 