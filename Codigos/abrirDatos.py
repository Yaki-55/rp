import pandas as pd
import xml.etree.ElementTree as ET

catalog_csv = pd.read_csv("../Datos/Catalog_v2.csv")
if(catalog_csv.empty):
    print("csv vacio")
else:
    catalog_csv.head()

tree = ET.parse("../Datos/xml.xml")
root = tree.getroot()

data = []

for data in root.findall("Data"):
    category = root.find("Category")
    quantity = root.find("Quantity")
    price = root.find("Price")
    data.append({"Category": category, "Quantity": quantity, "Price": price})

df = pd.DataFrame(data)
print(df)