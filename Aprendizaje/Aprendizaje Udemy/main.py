import pandas as pd
import csv

ruta = '/home/sebastian/Downloads/weather_data.csv'

# dataframe = pd.read_csv(ruta) 
#print(dataframe)

# with open(ruta) as archivo:
#     lineas = archivo.readlines()

# data = []
# for linea in lineas:
#     elementos = linea.strip().split(',')
#     data.append(elementos)
# print  (data)

with open(ruta) as archivo:
    data = csv.reader(archivo)
    for row in data:
        print(row)