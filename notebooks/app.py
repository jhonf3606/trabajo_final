import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')  # Usa la ruta correcta dependiendo de tu estructura de carpetas

# Encabezado de la aplicación
st.header('Análisis de vehículos de segunda mano')  # Puedes poner cualquier título que quieras

# Botón para construir el histograma
hist_button = st.button('Construir histograma')  # Crear un botón en Streamlit

if hist_button:  # Si el usuario hace clic en el botón
    # Mostrar un mensaje al hacer clic
    st.write('Creando un histograma para la columna "odómetro" del conjunto de datos.')

    # Crear el histograma con Plotly Express
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)  # Mostrar el gráfico de manera interactiva

import streamlit as st

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
        ...
