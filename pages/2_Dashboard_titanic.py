import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px
from matplotlib import image

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR,os.pardir)

dir_of_interest = os.path.join(PARENT_DIR,"resources")

IMAGE_PATH =os.path.join( dir_of_interest,"images","th.jpg")

DATA_PATH=os.path.join(dir_of_interest,"data","titanic.csv")

st.title("Dashboard- Titanic DataSet")
img=image.imread(IMAGE_PATH)
st.image(img)

df=pd.read_csv(DATA_PATH)
st.dataframe(df)

embark_town=st.selectbox("Select the embark_town: ", df['Embarked'].unique())
col1,col2,col3=st.columns(3)
fig_1=px.histogram(df[df['Embarked']==embark_town], x= "Survived")
col1.plotly_chart(fig_1,use_container_width=True)

fig_2=px.box(df[df['Embarked']==embark_town],y="Pclass")
col2.plotly_chart(fig_2, use_container_width=True)







