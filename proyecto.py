import streamlit as st
import pandas as pd
from openpyxl import workbook
from PIL import Image
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title="Mi aplicación", page_icon="smile")

def pagina_principal():
    st.title("Página Principal")
    st.write("Bienvenido a la aplicación de Daniel Siguencia")
    img = Image.open("daniel.jpg")
    st.image(img, use_column_width=True)
    with open("VRAINS.mp3", "rb") as audio_file:
        st.audio(audio_file.read()) 
    st.write("Usa el menú de la izquierda para navegar entre las páginas")
    st.title("Ingreso de Edad")
    edad = st.number_input("Ingresa tu edad", min_value=0, max_value=100, step=1)
    st.write(f"Has ingresado{edad}años")
    st.title("Formulario de ingreso de datos")
    nombre = st.text_input("Ingrese su nombre")
    apellido= st.text_input("Ingrese su apellido")
    if nombre and apellido:
        st.write(f"Nombre: {nombre} {apellido}")
    
    meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}  
    st.title("Seleccionar Mes")                    
    mes_numero = st.slider("Selecciona un mes", 1, 12, 1)    
    mes_nombre = meses[mes_numero]
    st.write(f"Has seleccionado el mes: {mes_nombre}")
    
    st.title("Aceptación de términos y condiciones")
    acepta_terminos = st.checkbox("Acepto los términos y condiciones")
    if acepta_terminos:
        st.write("Gracias por aceptar los términos y condiciones.")
    else:
        st.warning("Debes aceptar los términos y condiciones para continuar.")
    st.title("Selección de Género")
    genero = st.radio("Selecciona tu genero:", ("Masculino", "Femenino", "Homosexual", "Bisexual", "Transexual"))
    st.write(f"Género seleccionado:{genero}")
    
    st.title("Seleccionar país")
    país = st.selectbox("Selecciona tú país:", ("Ecuador", "Colombia", "Perú"))
    st.write(f"País seleccionado: {país}")
    
    st.title("Formulario de Información")
    nombre = st.text_input("Ingresa tú nombre")
    if st.button("Enviar"):
        st.write(f"Nombre Ingresado: {nombre}")
    st.title("Cargar Archivos")
    archivo = st.file_uploader("Selecciona un archivo", type=["csv", "txt", "pdf"])
    if archivo is not None:
        st.write(f"Nombre del archivo: {archivo.name}")
        st.write(f"Tipo de archivo: {archivo.type}")
        st.write(f"Tamaño del archivo: {archivo.size} bytes")
        if archivo.type == "text/csv" or archivo.type == "text/plain":
            contenido = archivo.read().decode("utf-8")
            st.text(contenido)
    st.title("Seleccionar fecha")
    fecha = st.date_input("Selecciona una fecha")
    st.write(f"Fecha seleccionada: {fecha}")
    st.title("Seleccionar hora")
    hora = st.time_input("Selecciona una hora")
    st.write(f"Hora seleccionada: {hora}")
    st.info(f"No olvides dedicar tiempo a tú familia")
    nivel = st.select_slider("Selecciona tu nivel de satisfaccción", options=["Muy Bajo", "Bajo", "Medio", "Alto", "Muy Alto"], value="Medio")
    st.write("Tú nivel de satisfacción es:", nivel)        
    
def visualizar_datos():
    st.title("Visualización de datos")
    st.write("Carga un archivo csv para visualizar los datos")
    archivo_cargado = st.file_uploader("Elije un archivo CSV", type="csv")
    
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        df2 = df.sample(n=20, random_state=20)
        df3 = np.random.rand(10, 10)
        st.write("Datos del archivo CSV:")
        st.write(df)
        st.write("Estadísticas descriptivas")
        st.write(df.describe())
        st.write("Valores Máximos a visualizar en la tabla")
        st.dataframe(df2.style.highlight_max(axis=0))
        st.write("Tabla resumen de datos")
        st.write(df.head())
        st.write("Datos de la cola de registros")
        st.write(df.tail())
        st.write("Muestra de datos")
        st.write(df.sample())
        st.write("Información de datos")
        st.write(df.info())
        st.write("Indicación de valores nulos")
        st.write(df.isnull().sum())
        st.write("Datos por posición de columnas o registros iloc")
        st.write(df.iloc[0:5])
        st.write("Datos por posición de columnas o registros loc")        
        st.write(df.loc[0:5])
        st.write("Mapa de calor")
        st.write(sns.heatmap(df3, cmap='coolwarm', annot=True))
        st.write("Conteo de valores nulos")
        st.write(df.isna().sum())
        st.write("Conteo de datos relleno de celdas vacias")
        df_fill_na_f = df.fillna(method="ffill")
        st.write(df_fill_na_f)
        df_fill_na_f = df_fill_na_f.isna().sum()
        st.write(df_fill_na_f)
        st.write("Vanguard fill")
        df_fill_na_b= df.fillna(method="bfill")
        st.write(df_fill_na_b)
              
        st.write("De cada reporte estadpistico realizado es posible descargar su información")        
                
def graficos_interactivos():
    st.title("Gráficos interactivos")
    st.write("Carga un archivo CSV para crear gráficos interactivos")
    archivo_cargado = st.file_uploader("Elije un archivo CSV", type="csv", key="2")
    
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elije una columna para el eje X:")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Elije una columna para el eje Y:")
        eje_y = st.selectbox("Eje Y", df.columns)
                     
        if st.button("Crear Gráfico"):
            fig_scatter = px.scatter(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig_scatter)
            fig_bar = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig_bar)
            fig_boxe = px.box(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")  
            st.plotly_chart(fig_boxe)
            fig_hist = px.histogram(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")          
            st.plotly_chart(fig_hist)
            fig_ch = px.density_contour(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig_ch)
            
def informe_ejecutivo():
        st.title("Muestra de Datos ejemplo para un informe Ejecutivo")    
        
        data = {
            'Nombre': ['Juan', 'Ana', 'Pedro', 'Luis'],
            'Edad': [25, 30, 22, 35],
            'Ciudad': ['Guayaquil', 'Quito', 'Cuenca', 'Loja']
            }

        bu = pd.DataFrame(data)
        st.title("Informe Ejecutivo")
        st.write("Datos de personas:")
        st.dataframe(bu)

        resumen = {
            'Total de Personas': [bu['Nombre'].count()],
            'Edad Promedio': [bu['Edad'].mean()],
            'Edad Máxima': [bu['Edad'].max()],
            'Edad Mínima': [bu['Edad'].min()]
            }

        bu_resumen = pd.DataFrame(resumen)
        st.write("Resumen Ejecutivo")
        st.dataframe(bu_resumen)

        with pd.ExcelWriter('informe_ejecutivo.xlsx') as writer:
            bu.to_excel(writer, sheet_name='Datos')
            bu_resumen.to_excel(writer, sheet_name='Resumen')
          
                    
st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", "Visualización de Datos", "Gráficos interactivos", "Informe Ejecutivo"])

if pagina == "Página Principal":
    pagina_principal()
elif pagina == "Visualización de Datos":
    visualizar_datos()
elif pagina == "Gráficos interactivos":
    graficos_interactivos()
elif pagina == "Informe Ejecutivo":
    informe_ejecutivo()
    