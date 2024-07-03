import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import mag4 as mg
import matplotlib.pyplot as plt

with st.expander("Show Data"):
    st.dataframe(mg.get_data('bastcrat'))

df = mg.get_data('bastcrat')

df2 = df.dropna()

elements = df2.columns.tolist()[27:]

x_axis = st.selectbox("select x-axis", elements)
y_axis = st.selectbox("select y-axis", elements)


fig, ax = plt.subplots()
ax.scatter(df[x_axis], df[y_axis])
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
st.pyplot(fig)
