import streamlit as st
from vega_datasets import data
import pandas as pd
import altair as alt
import sys

@st.cache
def load_data():
    dataframe = data.iris()
    return dataframe

def instrucoes():
    st.markdown(
    """
    Página de exemplo do streamlit utilizando o dataset Iris.
    Esta biblioteca é interessante para a apresentação dos resultados, pois gera uma página web.
    
    ### Perguntas? Comentários?
    
    Streamlit community  -> https://discuss.streamlit.io
    """)

def analise_dataset(df):
    species = ["Todas"]
    species.extend(df["species"].unique())
    tipo = st.selectbox("Species:", species)
    if tipo == "Todas":
        st.write('## Dataset Iris', df)
    else:
        st.write('## Dataset Iris', df[df["species"] == tipo])
    
    if st.checkbox("Mostrar Gráfico", False):
        st.subheader("Gráfico Representação do Dataset")
        
        st.markdown("""
                  ### Aplicar filtros em relação a pétala
                  """)
        var_filtro = "petalWidth"
        var_filtro2 = "petalLength"
        petalWidth = st.slider("Filtrar largura da pétala maior ou igual ", min(df[var_filtro].unique()), max(df[var_filtro].unique()), step=0.1, format="%f")
        petalLength = st.slider("Filtrar comprimento da pétala maior ou igual ", min(df[var_filtro2].unique()), max(df[var_filtro2].unique()), step=0.1, format="%f")
        
        df_filter = df[(df[var_filtro] >= petalWidth) & (df[var_filtro2] > petalLength) ]
        
        st.altair_chart(alt.Chart(df_filter).mark_circle().encode(
                        alt.X('sepalLength', scale=alt.Scale(zero=False)),
                        alt.Y('sepalWidth', scale=alt.Scale(zero=False, padding=1)),
                        color='species',
                        size='petalWidth',
                        tooltip=['species','sepalLength', 'sepalWidth', 'petalLength', 'petalWidth'],
                    ).interactive(), use_container_width=True)
    if st.checkbox("Mostrar Summay", False):
        st.write(df.describe())

def main(): 
    st.title("Dataset Iris")
    
    df = load_data()
        
    st.sidebar.title("What to do")
    menu = ["Instruções", "Exploração DataSet"]
    app_mode = st.sidebar.selectbox("Escolha uma  opção:",
        menu)
    
    if app_mode == menu[0]:
        st.sidebar.success('Para continuar selecione "'+menu[1]+'".')
        instrucoes()
    elif app_mode == menu[1]:
        st.sidebar.success('Para continuar selecione "'+menu[2]+'".')
        analise_dataset(df)
            

if __name__ == "__main__":
    main()


