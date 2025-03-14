import pandas as pd
import xml.etree.ElementTree as ET

# Cargar el archivo CSV
catalog_csv = pd.read_csv("../Datos/Catalog_v2.csv")
if catalog_csv.empty:
    print("CSV vacío")
else:
    print(catalog_csv.head())

# Parsear el archivo XML
tree = ET.parse("../Datos/xml.xml")
root = tree.getroot()

# Inicializar la lista de datos
data = []

# Iterar sobre cada elemento 'Data' en el XML
for item in root.findall("Data"):
    category = item.find("Category").text if item.find("Category") is not None else None
    quantity = item.find("Quantity").text if item.find("Quantity") is not None else None
    price = item.find("Price").text if item.find("Price") is not None else None
    data.append({"Category": category, "Quantity": quantity, "Price": price})

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
