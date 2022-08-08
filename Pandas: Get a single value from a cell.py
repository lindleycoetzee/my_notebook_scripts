import pandas as pd

df = pd.read_csv("my_file_path")

cell_value_1 = df["Team"].values[0] # 1st row in "Team" column
cell_value_2 = df["Team"].values[9] # 10th row in "Team" column
cell_value_2 = df["Games"].values[4] # 5th row in "Games" column
