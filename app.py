import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Datos sobre carros en USA')

#car_data = pd.read_csv('/Users/ramsesenriquefloresgomez/Desktop/DATASCIENTIST/Projecto 5/Project5/vehicles_us.csv')  leer los datos localmente
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



disp_button = st.button('Construir gráfico de dispersión') # crear un botón

if disp_button: 
    
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    st.plotly_chart(fig, use_container_width=True) # crear gráfico de dispersión



# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
