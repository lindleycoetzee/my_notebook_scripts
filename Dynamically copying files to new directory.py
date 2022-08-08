import pandas as pd
import os
from pathlib import Path
import shutil

source_path = "C:/folder_1"
destination_path = "C:/folder_2"

df pd.read_csv(destination_path + "file.csv")

id_list = df["id"].to_list()

for i in id_list:
  files = Path(source_path).glob(str(i) + "*")
  for file in files:
  destination_file = os.path.jion(destination_path, os.path.basename(file))
  shutil.copyfile(src=file, dst=destination_file)
