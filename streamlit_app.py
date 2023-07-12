import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import plotly.express as px

st.sidebar.header('Input here')
user_input = st.sidebar.text_input("Enter Register No:")

df=pd.read_excel('intern21.xlsx')
st.write(df)

st.markdown('### Report')
col1, col2= st.columns(2)
col1.metric("Name", df['Name'][0])
col2.metric("Reg_No", df['Reg_no'][0])

col3, col4= st.columns(2)
col3.metric('DOB', str(df['DOB'][0]))
col4.metric("Gender", df['Gender'][0])

  
