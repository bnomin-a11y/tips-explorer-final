import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("Restaurant Tips Explorer")

df = px.data.tips()

day = st.selectbox("Choose a day:", df["day"].unique())
value = st.selectbox("Choose what to see:", ["total_bill", "tip", "size"])

filtered = df[df["day"] == day]

fig = px.histogram(filtered, x=value, color="sex", title=f"{value} on {day}")
st.plotly_chart(fig)
st.write("Average", value, "on", day, ":", round(filtered[value].mean(), 2))