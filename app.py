import streamlit as st
import pandas as pd
import pickle

st.image("http://www.ehtp.ac.ma/images/lo.png")
st.write("""
# MSDE4 
##### Etudiantes:Msahal Maya et ZERROUKI Asmae
## Project:Customer segmentation using RFM analysis and clustering
This app predicts the **Income of online-retail using K-mean Cluster and RFM ** type
""")
st.sidebar.image("https://github.com/MayaMsahal/streamlit-heroku-Online-Retail/raw/main/pic.jpeg",width=300)

st.sidebar.header('User Input Parameters')

def user_input_features():
    online_retail_Recency = st.sidebar.slider('Recency', 1.0, 75.0)
    online_retail_Frequency = st.sidebar.slider('Frequency', 1.0, 10.0)
    online_retail_length = st.sidebar.slider('MonetaryValue', 1.0, 160.8)
    online_cluster = st.sidebar.slider('Cluster', 1, 160)
    
    data = {'Recency': online_retail_Recency,
            'Frequency': online_retail_Frequency,
            'MonetaryValue': online_retail_length,
            'Cluster': online_cluster}
			
			
    features = pd.DataFrame(data,index=[0])
    return features

df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

#K-Means model:

model_km=pickle.load(open("/app/model_df_normalized.pkl", "rb"))
prediction = model_km.predict(df)


st.subheader('Prediction')
st.write(prediction)



