import pandas as pd

students_csv = pd.read_csv("../unzipDataSets/data.csv", sep=";")
if students_csv.empty:
    print("CSV vacío")
else:
    print(students_csv.head())

students_csv = students_csv.replace({"Dropout": 1, "Graduate": 0})
print(students_csv.head())