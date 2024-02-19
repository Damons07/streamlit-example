import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient('mongodb+srv://damons07:mNcsCwuuA8vYuxB9@prediccion2024.htxnzwm.mongodb.net/')
db = client.sample_geospatial
collection = db.shipwrecks

# Obtener datos de la colección
data = pd.DataFrame(list(collection.find()))

# Mostrar dataframe antes de la limpieza
st.write("Dataframe antes de la limpieza:")
st.write(data)

# Proceso de limpieza de datos

# Mostrar dataframe después de la limpieza
st.write("Dataframe después de la limpieza:")
st.write(data)