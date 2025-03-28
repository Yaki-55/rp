import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../unzipDataSets/data.csv', sep=";")
print(df.head())
