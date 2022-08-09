import pandas as pd

df = pd.read_csv(data.csv)

car_model_list = df["model"].unique().to_list()
car_model_number_list = df["model_number"].unique().to_list()

# create a zip object from the two lists
zipObj = zip(car_model_list, car_model_number_list)

# create a dictionary from the zip object
car_model_dict = dict(zipObj)
