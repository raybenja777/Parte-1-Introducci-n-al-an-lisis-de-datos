import numpy as np
import csv
from datasets import load_dataset



dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

with open('heart_failure_clinical_records_dataset.csv', 'r') as file:
     csv_reader = csv.reader(file)
     next(csv_reader)
     age = [float(row[0]) for row in csv_reader] 
        
     edades_np = np.array(age)

     promedio_edades = np.mean(edades_np)
     print("El promedio de las edades es:", promedio_edades)


