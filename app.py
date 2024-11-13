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


# crear una casilla de verificación
# Crear casillas de verificación para generar gráficos
build_histogram_checkbox = st.checkbox('Construir un histograma')
build_scatter_plot_checkbox = st.checkbox('Construir un diagrama de dispersión')

if build_histogram_checkbox:  # Si la casilla de verificación para el histograma está seleccionada
    st.write('Creando un histograma para la columna "odómetro" del conjunto de datos.')

    try:
        # Crear el histograma con Plotly Express
        fig_histogram = px.histogram(car_data, x="odometer", title="Distribución del odómetro")
        
        # Mostrar el gráfico interactivo en Streamlit
        st.plotly_chart(fig_histogram, use_container_width=True)  # Mostrar el gráfico dentro de Streamlit
    except Exception as e:
        st.error(f"Error al crear el histograma: {e}")

if build_scatter_plot_checkbox:  # Si la casilla de verificación para el diagrama de dispersión está seleccionada
    st.write('Creando un diagrama de dispersión para la relación entre odómetro y precio.')

    try:
        # Crear el diagrama de dispersión con Plotly Express
        fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
        
        # Mostrar el gráfico interactivo en Streamlit
        st.plotly_chart(fig_scatter, use_container_width=True)  # Mostrar el gráfico dentro de Streamlit
    except Exception as e:
        st.error(f"Error al crear el diagrama de dispersión: {e}")