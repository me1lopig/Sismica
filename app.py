import streamlit as st  
import pandas as pd  
  
@st.cache_data  
def load_data():  
    # Cargar el archivo Excel  
    df = pd.read_excel("datos.xlsx", engine="calamine")  
    return df  
  
def main():  
    st.title("Visualización de Datos Sísmicos")  
      
    # Cargar datos  
    df = load_data()  
      
    st.subheader("Filtrar Datos")  
    # Filtro por provincia  
    provincias = sorted(df["PROVINCIA"].unique())  
    provincia_seleccionada = st.selectbox("Selecciona la Provincia", provincias)  
      
    # Filtrar por provincia  
    df_filtrado = df[df["PROVINCIA"] == provincia_seleccionada]  
      
    # Filtro por población basado en la provincia seleccionada  
    poblaciones = sorted(df_filtrado["POBLACION"].unique())  
    poblacion_seleccionada = st.selectbox("Selecciona la Población", poblaciones)  
      
    # Filtrar por población  
    df_final = df_filtrado[df_filtrado["POBLACION"] == poblacion_seleccionada]  
      
    st.subheader("Datos de la Población Seleccionada")  
    st.write("Aceleración Sísmica (ab) y Coeficiente k:", df_final[["ab", "k"]])  
       
  
if __name__ == "__main__":  
    main()  