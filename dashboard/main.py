import pandas as pd
import numpy as np
import streamlit as st
import csv

st.title('Dashboard')

file = open('satellite.csv')
data = pd.read_csv(file)
st.dataframe(data)
# csvreader = csv.reader(file)
# header = next(csvreader)

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(header)

# st.dataframe
