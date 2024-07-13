import streamlit as st
import pandas as pd
from datetime import datetime 

#Configuração da pagina
st.set_page_config(page_title='Amazon Profit',
layout='centered', 
initial_sidebar_state="auto"
)

df = pd.read_csv("AmazonSalesData.csv")

df.set_index('Sales Channel', inplace=True)

st.image('Logo Youse.png')
st.divider()
st.markdown("<h1 style='text-align: center; color: grey;'>Amazon Sales Analisys</h1>", unsafe_allow_html=True)

st.divider()

#Sidebar
st.sidebar.divider()
st.sidebar.write("YOUSE COMPUTER SOLUTIONS!🚀")
st.sidebar.image('Logo Youse.png')
st.sidebar.divider()

#filter
region = df['Region'].value_counts().index
region1 = st.sidebar.selectbox('Selecione a região desejada:',(region))
df_filtered = df[df['Region'] == region1]


#line chart01
st.markdown("<h3 style='text-align: center; color: white;'>Renda por item vendido!</h3>", unsafe_allow_html=True)
st.line_chart(df_filtered, x='Item Type', y='Total Profit', color='#b6fcd5')

st.divider()

#bar chart01
st.markdown("<h3 style='text-align: center; color: white;'>Unidades vendidas por país!</h3>", unsafe_allow_html=True)
df_filtered2 = df[df['Region'] == region1]
st.bar_chart(df_filtered2, x='Country', y='Units Sold', color= '#8a2be2')

st.divider()

#Toggle creation
on = st.toggle("Mostre a base de dados")
if on:
    df_filtered2
    st.write('Você está visualizando a base de dados original!')


st.sidebar.divider()

st.sidebar.link_button('Acesse nosso Site', 'https://yousesol.github.io/Youse/')
st.sidebar.divider()
st.sidebar.link_button('Entre em contato', 'https://wa.me/5531995518294')
