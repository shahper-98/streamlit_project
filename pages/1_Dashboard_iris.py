import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR,os.pardir)

dir_of_interest = os.path.join(PARENT_DIR,"resources")

IMAGE_PATH =os.path.join( dir_of_interest,"images","Iris.jpg")

DATA_PATH=os.path.join(dir_of_interest,"data","Iris.csv")

st.title("Dashboard- Titanic DataSet")
img=image.imread(IMAGE_PATH)
st.image(img)

df=pd.read_csv(DATA_PATH)
st.dataframe(df)

species=st.selectbox("Select the species:",df['Species'].unique())
col1, col2 = st.columns(2)

fig_1=px.histogram(df[df['Species']==species], x= "PetalLengthCm")
col1.plotly_chart(fig_1,use_container_width=True)

fig_2=px.box(df[df['Species']==species],y="SepalLengthCm")
col2.plotly_chart(fig_2, use_container_width=True)