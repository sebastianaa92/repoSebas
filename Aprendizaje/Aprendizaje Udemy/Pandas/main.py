# import pandas as pd

# datos = pd.read_csv("weather_data.csv")

# data = datos.values.tolist()

# print(data)

import csv

with open('weather_data.csv') as file:
    content = csv.reader(file) 
    temperature = []
    for row in content:
        print(row[1])