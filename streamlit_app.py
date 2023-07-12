import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import plotly.express as px

st.sidebar.header('Input here')
user_input = st.sidebar.text_input("Enter Register No:")
