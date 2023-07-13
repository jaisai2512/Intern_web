

import pandas as pd
import streamlit as st
import plotly.express as px

required_skills = {"Cloud Computing":{
    "Cloud_Platforms":{"AWS":1,"AZURE": 2,"GCP": 1},
    "Networking fundamentals":{"TCP/IP":1,"DNS": 2,"Load balancing":5,"VPN":5 },
    "OS":{"Linux":4, "Windows":5}, 
    "Automation & Scripting":{"Python":2,"Powershell":3,"Bash":4},
    "IAC":{"Terraform":1 ,"AWS cloud formation":2},
    "Containerization":{"Docker":1,"Kubernetes":2},
    "Monitoring & Troubleshooting":{"AWS cloudwatch":1,"Azure monitor":2},
    "Softskills":{"Effective communication":1,"Teamwork":1,"Collaboration skills":1}
}}



st.sidebar.header('Input here')
user_input = st.sidebar.text_input("Enter Register No:")

if user_input :
    df=pd.read_excel('intern21.xlsx')
    user_input=int(user_input)
    df=df[df['Reg_no']==user_input]
    st.markdown('## Report')
    col1, col2= st.columns(2)
    col1.metric("Name", df['Name'][0])
    col2.metric("Reg_No", df['Reg_no'][0])

   
