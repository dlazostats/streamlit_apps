import streamlit as st 
import numpy as np
import pandas as pd

df = pd.read_csv("bd_price.csv")
st.line_chart(data=df,x="date",y="price")
