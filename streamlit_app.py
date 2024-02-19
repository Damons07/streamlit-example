import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient('mongodb+srv://damons07:mNcsCwuuA8vYuxB9@prediccion2024.htxnzwm.mongodb.net/')
db = client.sample_geospatial
collection = db.shipwrecks

# Obtener datos de la colección
data = pd.DataFrame(list(collection.find()))

# Cambiar los nombres de las columnas al español
nombres_columnas_espanol = {
    'Feature Type': 'Tipo de Característica',
    'Chart': 'Carta',
    'Latitude': 'Latitud',
    'Longitude': 'Longitud',
    'Gazetteer': 'Gazetteer',
    'Depth': 'Profundidad',
    'History': 'Historia',
    'Description': 'Descripción',
    'Accession No.': 'Número de Acceso',
    'Catalog No.': 'Número de Catálogo',
    'Object Name': 'Nombre del Objeto',
    'Vessel Name': 'Nombre del Buque',
    'Event': 'Evento',
    'Year Built': 'Año de Construcción',
    'Year Sunk': 'Año Hundido',
    'Reason Sunk': 'Razón del Hundimiento',
    'Coordinates': 'Coordenadas',
    'Legal Status': 'Estado Legal',
    'Date': 'Fecha',
    'Remarks': 'Observaciones'
}

data.rename(columns=nombres_columnas_espanol, inplace=True)

# Mostrar dataframe antes de la limpieza
st.write("Dataframe antes de la limpieza:")
st.write(data)

# Proceso de limpieza de datos

# Mostrar dataframe después de la limpieza
st.write("Dataframe después de la limpieza:")
st.write(data)
