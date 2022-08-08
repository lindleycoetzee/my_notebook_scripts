import pandas as pd
import os

path = "C:/Users/lindley/files/"
file_names_list = []
df_list = []

# iterate over files in directory and add files names to list
for root, dirs, files in os.walk(path):
  for file in files:
  file_name = str(path) + str(file)
  file_names_list.append(file_name)
  
# create DataFrame for each file append to list
for f in file_names_list:
  df = pd.read_excel(f)
  df_list.append(df)
  
# concatenate all files together and save as a single file
concat_file = pd.concat(df_list)
concat_file.to_excel(path + "concat_file.xlsx")
